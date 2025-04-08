from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse
import requests

app = Flask(__name__)

# Your ElevenLabs Talk-To Agent Link
ELEVENLABS_TALK_URL = "https://elevenlabs.io/app/talk-to?agent_id=D28wQbkStWEYLBjOng7L"


@app.route("/voice", methods=["POST"])
def voice():
    """Handle incoming calls and redirect to ElevenLabs Talk-To"""
    response = VoiceResponse()

    # Use <Dial> to connect the call to ElevenLabs AI
    response.dial(ELEVENLABS_TALK_URL)

    return Response(str(response), mimetype="text/xml")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
