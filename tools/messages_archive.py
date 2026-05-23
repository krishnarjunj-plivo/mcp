@mcp.tool()
def messages_archive(message_uuid: Any) -> None:
    """Archive a message thread so it no longer appears in default lists."""
    try:
        response = plivo.RestClient().messages.archive(message_uuid=message_uuid)
        return getattr(response, "__dict__", response)
    except plivo.exceptions.PlivoRestError as e:
        return {"error": str(e)}
