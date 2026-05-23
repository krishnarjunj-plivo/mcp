@mcp.tool()
def calls_transcribe(call_uuid: Any, language: Any = None, callback_url: Any = None, callback_method: Any = 'POST') -> None:
    """"""
    try:
        response = plivo.RestClient().calls.transcribe(call_uuid=call_uuid, language=language, callback_url=callback_url, callback_method=callback_method)
        return getattr(response, "__dict__", response)
    except plivo.exceptions.PlivoRestError as e:
        return {"error": str(e)}
