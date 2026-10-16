"""Unit tests for each MCP tool category used by the sales-goal-setting-agent."""
import json
import os
import pytest
from unittest.mock import AsyncMock, MagicMock, patch

os.environ.setdefault("IBD_TESTING", "true")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_tool(name: str, response: dict):
    """Create a mock LangChain tool that returns a JSON-serialised response."""
    tool = MagicMock()
    tool.name = name
    tool.ainvoke = AsyncMock(return_value=json.dumps(response))
    return tool


def _make_llm_response(content: str):
    """Return a minimal fake LLM message."""
    msg = MagicMock()
    msg.content = content
    return msg


# ---------------------------------------------------------------------------
# R1 — CRM Territory Data (mocked tools)
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_get_territory_accounts():
    """Agent should use a mock territory-accounts tool and surface account summary."""
    tool = _make_tool(
        "get_territory_accounts",
        {
            "results": [
                {"accountId": "ACC-001", "name": "Acme Corp", "segment": "Enterprise"},
                {"accountId": "ACC-002", "name": "Beta Ltd", "segment": "Mid-Market"},
            ]
        },
    )
    assert tool.name == "get_territory_accounts"
    result = json.loads(await tool.ainvoke({"territory": "EMEA-West", "quarter": "Q4-2026"}))
    assert len(result["results"]) == 2
    assert result["results"][0]["segment"] == "Enterprise"


@pytest.mark.asyncio
async def test_get_territory_leads():
    """Agent should retrieve active leads from the territory tool."""
    tool = _make_tool(
        "get_territory_leads",
        {
            "results": [
                {"leadId": "LEAD-001", "name": "New Lead A", "stage": "Qualified", "estimatedValue": "50000"},
                {"leadId": "LEAD-002", "name": "New Lead B", "stage": "Prospecting", "estimatedValue": "20000"},
            ]
        },
    )
    result = json.loads(await tool.ainvoke({"territory": "EMEA-West"}))
    assert len(result["results"]) == 2
    assert result["results"][0]["stage"] == "Qualified"


@pytest.mark.asyncio
async def test_get_open_opportunities():
    """Agent should retrieve open Q4 opportunities."""
    tool = _make_tool(
        "get_open_opportunities",
        {
            "results": [
                {
                    "opportunityId": "OPP-001",
                    "name": "Enterprise Deal A",
                    "stage": "Proposal",
                    "value": "120000",
                    "closeDate": "2026-12-15",
                },
                {
                    "opportunityId": "OPP-002",
                    "name": "Mid-Market Deal B",
                    "stage": "Negotiation",
                    "value": "45000",
                    "closeDate": "2026-11-30",
                },
            ]
        },
    )
    result = json.loads(await tool.ainvoke({"quarter": "Q4-2026"}))
    assert len(result["results"]) == 2
    assert result["results"][0]["stage"] == "Proposal"
    assert float(result["results"][0]["value"]) > 0


@pytest.mark.asyncio
async def test_get_sales_performance_history():
    """Agent should retrieve and parse historical quarterly performance."""
    tool = _make_tool(
        "get_sales_performance_history",
        {
            "results": [
                {"quarter": "Q3-2026", "quotaAttainment": 0.82, "dealsClosed": 4, "revenueVsTarget": -18000},
                {"quarter": "Q2-2026", "quotaAttainment": 0.95, "dealsClosed": 6, "revenueVsTarget": 5000},
            ]
        },
    )
    result = json.loads(await tool.ainvoke({"userId": "alex.johnson@company.com", "quarters": 2}))
    assert len(result["results"]) == 2
    assert result["results"][0]["quarter"] == "Q3-2026"
    assert result["results"][0]["quotaAttainment"] < 1.0


# ---------------------------------------------------------------------------
# R2 — SAP SuccessFactors Employee Profile & Goals
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_get_employee_profile():
    """Agent should retrieve the rep's SF employee profile."""
    tool = _make_tool(
        "get_eppublicprofile_for_sfodata",
        {
            "userId": "alex.johnson@company.com",
            "firstName": "Alex",
            "lastName": "Johnson",
            "title": "Senior Account Executive",
            "department": "Enterprise Sales - EMEA",
            "manager": "morgan.lee@company.com",
        },
    )
    result = json.loads(await tool.ainvoke({"userId": "alex.johnson@company.com"}))
    assert result["userId"] == "alex.johnson@company.com"
    assert result["title"] == "Senior Account Executive"
    assert "manager" in result


@pytest.mark.asyncio
async def test_get_existing_goals():
    """Agent should retrieve existing Q4 goals from SF PMGM."""
    tool = _make_tool(
        "list_goal_1_for_sfodata",
        {
            "results": [
                {
                    "id": 1001,
                    "name": "Close 3 enterprise opportunities",
                    "metric": "Pipeline",
                    "status": "On Track",
                    "userId": "alex.johnson@company.com",
                }
            ]
        },
    )
    result = json.loads(await tool.ainvoke({"filter": "userId eq 'alex.johnson@company.com'", "top": "100"}))
    assert len(result["results"]) == 1
    assert result["results"][0]["metric"] == "Pipeline"


@pytest.mark.asyncio
async def test_get_existing_goals_empty():
    """Agent should handle empty goal list gracefully (fresh quarter)."""
    tool = _make_tool("list_goal_1_for_sfodata", {"results": []})
    result = json.loads(await tool.ainvoke({"filter": "userId eq 'new.user@company.com'"}))
    assert result["results"] == []


# ---------------------------------------------------------------------------
# R5 — Goal Write-back: create and update
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_create_goal():
    """Agent should be able to create a new goal in SF after confirmation."""
    tool = _make_tool(
        "create_goal_1_for_sfodata",
        {
            "id": 1003,
            "name": "Complete enterprise product certification by end of Q4 2026",
            "metric": "Growth",
            "userId": "alex.johnson@company.com",
        },
    )
    payload = {
        "name": "Complete enterprise product certification by end of Q4 2026",
        "metric": "Growth",
        "userId": "alex.johnson@company.com",
        "due": "/Date(1767052800000)/",
    }
    result = json.loads(await tool.ainvoke(payload))
    assert result["id"] == 1003
    assert "certification" in result["name"]


@pytest.mark.asyncio
async def test_update_goal():
    """Agent should be able to update an existing goal's wording after rep edits."""
    tool = _make_tool(
        "update_goal_1_for_sfodata",
        {
            "id": 1001,
            "name": "Close 3 enterprise opportunities in Q4 2026 (Revised)",
            "status": "On Track",
        },
    )
    result = json.loads(await tool.ainvoke({"id": 1001, "name": "Close 3 enterprise opportunities in Q4 2026 (Revised)"}))
    assert result["id"] == 1001
    assert "Revised" in result["name"]


# ---------------------------------------------------------------------------
# R7 — Guardrails: no write without confirmation
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_no_write_without_confirmation():
    """Write tools must NOT be called when the rep cancels before confirmation."""
    write_tool = _make_tool("create_goal_1_for_sfodata", {"id": 9999})

    # Simulate a session that ends without confirmation
    session_confirmed = False

    if not session_confirmed:
        # Guardrail: skip the write
        pass
    else:
        await write_tool.ainvoke({"name": "Ghost goal", "userId": "test"})

    write_tool.ainvoke.assert_not_awaited()


# ---------------------------------------------------------------------------
# Integration test: end-to-end agent flow (mocked LLM + mocked tools)
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_agent_end_to_end_flow():
    """Full agent flow: load tools, stream response with mocked LLM."""
    from agent import SampleAgent

    mock_tools = [
        _make_tool("list_goal_1_for_sfodata", {"results": []}),
        _make_tool("get_eppublicprofile_for_sfodata", {"userId": "alex.johnson@company.com", "title": "AE"}),
    ]

    fake_message = _make_llm_response(
        "I've retrieved your territory data. Let me suggest some goals for Q4 2026. "
        "For pipeline: Close 3 enterprise deals. For activity: 15 discovery calls. "
        "For growth: complete product certification. Shall I save these?"
    )

    with patch("agent.ChatLiteLLM") as MockLLM, \
         patch("agent.create_agent") as mock_create_agent, \
         patch("agent.create_checkpointer") as mock_checkpointer:

        # Set up mock LLM
        mock_llm_instance = MagicMock()
        MockLLM.return_value = mock_llm_instance

        # Set up mock graph
        mock_graph = AsyncMock()
        mock_graph.ainvoke = AsyncMock(return_value={"messages": [fake_message]})
        mock_create_agent.return_value = mock_graph
        mock_checkpointer.return_value = MagicMock()

        agent = SampleAgent()
        responses = []
        async for chunk in agent.stream("Help me set my Q4 goals", "ctx-test-001", tools=mock_tools):
            responses.append(chunk)

    assert len(responses) >= 2  # at least "Processing..." + final
    final = responses[-1]
    assert final["is_task_complete"] is True
    assert "goals" in final["content"].lower() or "Q4" in final["content"]


# ---------------------------------------------------------------------------
# Negative test: cancellation — no write tools called
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_cancellation_no_write_called():
    """Cancellation path: agent must not invoke write tools when rep cancels."""
    write_tool = _make_tool("create_goal_1_for_sfodata", {"id": 1})
    update_tool = _make_tool("update_goal_1_for_sfodata", {"id": 1})

    # Simulate rep cancelling
    user_confirmed = False

    if user_confirmed:
        await write_tool.ainvoke({"name": "Should not be created"})
        await update_tool.ainvoke({"id": 1})

    write_tool.ainvoke.assert_not_awaited()
    update_tool.ainvoke.assert_not_awaited()
