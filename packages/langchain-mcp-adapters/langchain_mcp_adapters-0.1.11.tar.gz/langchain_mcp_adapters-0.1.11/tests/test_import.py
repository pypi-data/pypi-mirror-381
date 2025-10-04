def test_import() -> None:
    """Test that the code can be imported"""
    from langchain_mcp_adapters import (  # noqa: F401, PLC0415
        client,
        prompts,
        resources,
        tools,
    )
