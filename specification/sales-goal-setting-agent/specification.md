# Specification: sales-goal-setting-agent

> **Guidelines**: Read all applicable guidelines before executing ANY tasks below:
> - [guidelines.md](../guidelines.md) — Universal execution rules
> - [guidelines-agent.md](../guidelines-agent.md) — Universal agent patterns
> - [guidelines-agent-python.md](../guidelines-agent-python.md) — Python implementation details
> - [guidelines-agent-skills.md](../guidelines-agent-skills.md) — Runtime skills patterns
> - [guidelines-agent-mcp.md](../guidelines-agent-mcp.md) — MCP integration patterns

---

## API Integrations

### SAP SuccessFactors — Performance & Goal Management (PMGM)

- **API ORD ID**: `sap.sf:apiResource:PerformanceandGoalsPMGM:v1`
- **API Type**: OData
- **Spec file**: `specification/sales-goal-setting-agent/api-specs/PerformanceandGoalsPMGM.edmx`
- **MCP tool scope**: read-write
- **Resources in scope**: Goal, GoalPlan, GoalTemplate

### SAP SuccessFactors — Employee Profile

- **API ORD ID**: `sap.sf:apiResource:ECEmployeeProfile:v1`
- **API Type**: OData
- **Spec file**: `specification/sales-goal-setting-agent/api-specs/ECEmployeeProfile.edmx`
- **MCP tool scope**: read-only
- **Resources in scope**: EmployeeProfile, PerPerson, PerPersonal, PerJob

### SAP Sales Cloud — CRM Territory Data (Custom MCP)

- **Status**: No standard MCP server or OData API available in the connected landscape
- **Approach**: Custom MCP server wrapping SAP Sales Cloud APIs for territory accounts, leads, open opportunities, and historical sales performance
- **Custom tools to implement** (within the custom MCP server):
  - `get_territory_accounts` — retrieves managed accounts for the rep's territory, current quarter
  - `get_territory_leads` — retrieves active leads in the rep's territory
  - `get_open_opportunities` — retrieves open opportunities for the current quarter
  - `get_sales_performance_history` — retrieves historical quarterly performance metrics

---

## Basic Setup

- [ ] Read `product-requirements-document.md` and `intent.md` thoroughly before proceeding
- [ ] Bootstrap agent code in `assets/sales-goal-setting-agent/` using the `sap-agent-bootstrap` instructions from the `agent` skill (run bootstrap from inside `assets/sales-goal-setting-agent/`, use copy commands — do NOT create files manually)
- [ ] Install dependencies, validate the agent starts and responds at `/.well-known/agent.json`

---

## Runtime Skills

- [ ] Create a runtime skill for **CRM territory context summarisation**: `assets/sales-goal-setting-agent/app/skills/crm-territory-context/SKILL.md`
  - Purpose: instructs the agent how to read and summarise raw CRM data (accounts, leads, opportunities, performance) into a concise territory snapshot for the rep
  - Include: summarisation format, key metrics to highlight (e.g., total accounts, active leads count, top open deal by value, QoQ performance trend)

- [ ] Create a runtime skill for **goal recommendation logic**: `assets/sales-goal-setting-agent/app/skills/goal-recommendation/SKILL.md`
  - Purpose: step-by-step instructions for translating the territory snapshot + SuccessFactors profile into goal recommendations across pipeline, activity, and growth dimensions
  - Include: definition of each dimension, rules for mapping CRM data points to goal suggestions, traceability requirement (each suggestion must reference its source data point), minimum one recommendation per dimension

- [ ] Create a runtime skill for **goal refinement flow**: `assets/sales-goal-setting-agent/app/skills/goal-refinement/SKILL.md`
  - Purpose: instructions for the conversational loop — presenting goals, accepting edits, re-presenting updated goals, and reaching explicit rep confirmation before write-back
  - Include: confirmation protocol (exact phrasing for seeking confirmation), cancellation handling (no write if session ends without confirmation), re-edit rules (allow re-edit until confirmed), policy compliance check (validate required SuccessFactors fields before calling write tools)

---

## Project-Specific Tasks

### R1 — CRM Territory Data Retrieval

- [ ] Wire `get_territory_accounts` MCP tool: retrieve managed accounts for the authenticated rep's territory, scoped to the current quarter; present a concise summary to the rep (account name, segment, status)
- [ ] Wire `get_territory_leads` MCP tool: retrieve active leads in the rep's territory; include lead name, stage, and estimated value in the summary
- [ ] Wire `get_open_opportunities` MCP tool: retrieve open opportunities for the current quarter; include opportunity name, stage, expected close date, and value
- [ ] Wire `get_sales_performance_history` MCP tool: retrieve historical quarterly performance metrics (e.g., quota attainment %, deals closed, revenue vs. target) for at least the prior 2 quarters
- [ ] Implement fallback: if any CRM tool returns an error or empty result, the agent must surface the issue clearly to the rep in plain language and offer to continue with manually provided context (do NOT silently skip)
- [ ] After all CRM data is retrieved, invoke the `crm-territory-context` runtime skill to produce a structured territory snapshot before proceeding to SuccessFactors data retrieval

### R2 — SAP SuccessFactors Employee Profile & Goals Retrieval

- [ ] Wire `get_employee_profile` MCP tool (from SuccessFactors Employee Profile MCP server): fetch the authenticated rep's profile including name, role, department, manager, and tenure
- [ ] Wire `get_existing_goals` MCP tool (from SuccessFactors PMGM MCP server): fetch the rep's current goal plan entries for the active quarter; if none exist, note this clearly to the rep
- [ ] Implement fallback: if either SuccessFactors call fails, inform the rep and continue with partial context (do NOT abort the session)

### R3 — Goal Recommendation Generation

- [ ] After both CRM and SuccessFactors data are loaded, invoke the `goal-recommendation` runtime skill
- [ ] Generate at least one goal recommendation per dimension: **pipeline** (e.g., close X opportunities, achieve Y% of quota), **activity** (e.g., conduct Z customer visits, complete N demos), **growth** (e.g., complete a specific training, develop expertise in a product line)
- [ ] Each recommendation must include: proposed goal title, proposed goal description, and the specific data point from CRM or SuccessFactors that informed it (traceability requirement from PRD R3)
- [ ] Present the recommendations to the rep in a structured, readable format grouped by dimension
- [ ] If the rep asks why a goal was suggested, the agent must explain the data rationale without hallucinating

### R4 — Conversational Goal Refinement

- [ ] Invoke the `goal-refinement` runtime skill to manage the refinement loop
- [ ] Support rep-initiated wording edits: when the rep requests a change to a goal's title or description, update the goal text and re-present the revised version for review
- [ ] Allow re-editing at any point prior to final confirmation — the rep can revise previously approved goals until the final confirmation step
- [ ] Implement dimension completeness check: before proceeding to confirmation, verify at least one goal is selected from each of the three dimensions; if a dimension is empty, prompt the rep to add one or explicitly confirm they want to skip it
- [ ] Present the final confirmed goal list in a summary view before asking for write-back confirmation

### R5 — Human-Confirmed Goal Write-Back

- [ ] Implement a hard confirmation gate: the agent must receive explicit confirmation from the rep (e.g., "yes, confirm", "save my goals") before calling any write MCP tools
- [ ] On confirmation, call `create_goal` MCP tool for each new goal that does not exist in the current goal plan
- [ ] On confirmation, call `update_goal` MCP tool for each goal that already exists in the current goal plan (update/replace, do NOT duplicate)
- [ ] Implement cancellation: if the rep says "cancel", "stop", or ends the session without confirming, no write operations are performed; the agent acknowledges this clearly
- [ ] After successful write-back, confirm to the rep how many goals were created and how many were updated, and suggest they review their goals in SAP SuccessFactors

### R6 — Policy Compliance Enforcement

- [ ] Before calling any write MCP tools, validate that all required SuccessFactors PMGM goal plan fields are populated (as enforced by the API's entity schema)
- [ ] If the PMGM API returns a validation error (missing required field, invalid picklist value, etc.), surface the error to the rep in plain language and request the missing or corrected information before retrying — do NOT silently swallow API errors
- [ ] Ensure goal write-back operations include all mandatory fields from the `GoalPlan` and `Goal` entity definitions in the PMGM EDMX spec

### R7 — Guardrails & Safety

- [ ] Add system prompt instruction: the agent must never fabricate, guess, or invent CRM data or SuccessFactors profile data — all data must come from tool calls
- [ ] Add system prompt instruction: no goal write operation is permitted without an explicit rep confirmation in the current session
- [ ] Add system prompt instruction: the agent must never impersonate a manager or claim that goals have been approved by a manager
- [ ] Add system prompt instruction: if a goal write-back fails after confirmed, the agent must report the failure and provide the rep with the full text of the confirmed goals so they can submit manually if needed
- [ ] Add system prompt instruction: set page size (top / limit) to a maximum of 100 on all tool calls that support pagination

---

## Business Instrumentation

- [ ] Implement structured logging and OpenTelemetry spans for all 5 PRD milestones:

  - **M1 — CRM Data Retrieved**
    - `M1.achieved: CRM territory data retrieved successfully for rep {rep_id}, quarter {quarter}`
    - `M1.missed: CRM territory data retrieval failed or returned empty for rep {rep_id} — proceeding with manual context or aborting`

  - **M2 — Employee Context Loaded**
    - `M2.achieved: SAP SuccessFactors profile and goals loaded for rep {rep_id}`
    - `M2.missed: SuccessFactors profile or goals retrieval failed for rep {rep_id}`

  - **M3 — Goal Recommendations Generated**
    - `M3.achieved: goal recommendations generated for rep {rep_id} — pipeline: {n}, activity: {n}, growth: {n}`
    - `M3.missed: goal recommendation generation failed or produced incomplete dimensions for rep {rep_id}`

  - **M4 — Goals Refined and Confirmed by Rep**
    - `M4.achieved: rep {rep_id} confirmed {n} goals for write-back to SuccessFactors`
    - `M4.missed: rep {rep_id} did not confirm goals — session ended without write-back`

  - **M5 — Goals Written to SAP SuccessFactors**
    - `M5.achieved: {n} goals written to SAP SuccessFactors for rep {rep_id}, quarter {quarter}`
    - `M5.missed: goal write-back to SAP SuccessFactors failed for rep {rep_id} — {error_detail}`

- [ ] Extract business logic from `stream()` into plain async helpers to avoid `GeneratorExit` context errors when using OpenTelemetry spans (see `guidelines-agent-python.md`)
- [ ] Verify `bootstrap(app)` is called after `app = server.build()` in `main.py`

---

## MCP Tool Integration

- [ ] Invoke `mcp-translation-file` skill for `specification/sales-goal-setting-agent/api-specs/PerformanceandGoalsPMGM.edmx`
  - Scope: read-write; resources: `Goal`, `GoalPlan`, `GoalTemplate`
  - Tools needed: list goal plan, get goal, create goal, update goal
- [ ] Invoke `mcp-translation-file` skill for `specification/sales-goal-setting-agent/api-specs/ECEmployeeProfile.edmx`
  - Scope: read-only; resources: `EmployeeProfile`, `PerPerson`, `PerPersonal`, `PerJob`
  - Tools needed: get employee profile
- [ ] Invoke `setup-solution` skill to register both generated MCP server assets in `solution.yaml`
- [ ] Wire MCP tool loading in `app/agent.py` using `get_mcp_tools()` from the `mcp_tools` module — NEVER import directly from `sap_cloud_sdk.agentgateway`; NEVER create direct HTTP clients for SAP APIs
- [ ] Read the generated `asset.yaml` files for both MCP servers and copy the exact `ordId` values into the agent's `asset.yaml` under `requires`
- [ ] For the SAP Sales Cloud custom MCP server: add a placeholder `requires` entry in `asset.yaml` with a clear comment that the ORD ID must be updated once the custom server is deployed (custom MCP server is out of scope for this spec — flagged as an integration dependency)
- [ ] After all MCP servers are wired, generate `mcp-mock.json` using the `mcp-mock-config` skill

---

## Testing

- [ ] `conftest.py` must only set `IBD_TESTING=true` — this triggers mock MCP tool results during tests
- [ ] Write one unit test per MCP tool:
  - `test_get_territory_accounts` — mock CRM tool, verify territory summary output
  - `test_get_territory_leads` — mock CRM tool, verify leads summary output
  - `get_open_opportunities` — mock CRM tool, verify opportunities summary output
  - `test_get_sales_performance_history` — mock CRM tool, verify performance history parsing
  - `test_get_employee_profile` — mock SuccessFactors Employee Profile tool, verify profile extraction
  - `test_get_existing_goals` — mock SuccessFactors PMGM tool, verify existing goal parsing (including empty result case)
  - `test_create_goal` — mock PMGM write tool, verify goal creation payload and confirmation gate
  - `test_update_goal` — mock PMGM write tool, verify goal update payload and deduplication logic
- [ ] Write one integration test: end-to-end agent flow — initiate session, mock all CRM and SuccessFactors tool responses, verify agent produces goal recommendations, handles one wording edit, reaches confirmation, and calls write tools with correct payloads; test must run offline
- [ ] Write one negative test: verify the agent does NOT call any write tools when the rep cancels before confirmation
- [ ] Run `pytest` from `assets/sales-goal-setting-agent/` (no args — `pytest.ini` configures everything); if coverage < 70%, add tests until threshold met
- [ ] Run `pytest` again from `assets/sales-goal-setting-agent/` to generate final `test_report.json`
- [ ] Verify `test_report.json` exists in `assets/sales-goal-setting-agent/`
