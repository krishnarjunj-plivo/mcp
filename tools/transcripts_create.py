@mcp.tool()
def transcripts_create(call_uuid: Any, transcription_url: Any = None, language: Any = 'en-US') -> None:
    """Request a transcript for a completed call recording.

    Args:
        call_uuid: UUID of the call to transcribe.
        transcription_url: Optional webhook URL to POST the transcript to.
        language: BCP-47 language code; defaults to 'en-US'.
    """
    try:
        response = plivo.RestClient().transcripts.create(call_uuid=call_uuid, transcription_url=transcription_url, language=language)
        return response.__dict__
    except plivo.exceptions.PlivoRestError as e:
        return {"error": str(e)}
