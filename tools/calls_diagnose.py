@mcp.tool()
def calls_diagnose(call_uuid: Any) -> None:
    """Run a network diagnostic on the call leg."""
    try:
        response = plivo.RestClient().calls.diagnose(call_uuid=call_uuid)
        return getattr(response, "__dict__", response)
    except plivo.exceptions.PlivoRestError as e:
        return {"error": str(e)}
