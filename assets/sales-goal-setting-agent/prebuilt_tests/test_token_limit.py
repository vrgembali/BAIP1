"""Verifies that the system message (prompt + all tool schemas) fits within the token limit."""
# pyright: reportMissingImports=false

import pytest

_SYSTEM_MESSAGE_TOKEN_LIMIT = 100_000


@pytest.mark.structure
class TestCheckSystemMessageTokens:

    @pytest.mark.asyncio
    async def test_token_limit_with_all_mcp_tools(self, add_agent_to_path):
        """All MCP tools must fit within the system message token limit.

        If this test fails, there are too many or too verbose tools or system prompt.
        Prune the translation file or raise _SYSTEM_MESSAGE_TOKEN_LIMIT in this test to fix it.
        """
        from langchain_core.messages import SystemMessage
        from langchain_core.messages.utils import count_tokens_approximately
        from agent import get_system_prompt
        from mcp_providers.agw import get_mcp_tools

        tools = await get_mcp_tools()
        system_prompt = get_system_prompt()

        estimated_tokens = count_tokens_approximately(
            [SystemMessage(content=system_prompt)],
            tools=list(tools),
        )

        if estimated_tokens > _SYSTEM_MESSAGE_TOKEN_LIMIT:
            prompt_tokens = count_tokens_approximately([SystemMessage(content=system_prompt)])
            tool_tokens = estimated_tokens - prompt_tokens
            if prompt_tokens > tool_tokens:
                hint = (
                    f"The system prompt alone accounts for {prompt_tokens:,} tokens."
                    " Consider shortening the system prompt."
                )
            else:
                hint = (
                    f"{len(tools)} tools account for {tool_tokens:,} tokens."
                    " Consider reducing the number of tools (e.g. by pruning the tools according to the mcp-translation-file skill)."
                )
            pytest.fail(
                f"System message too large: estimated {estimated_tokens:,} tokens"
                f" exceeds the limit of {_SYSTEM_MESSAGE_TOKEN_LIMIT:,} tokens. {hint}"
            )
