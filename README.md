# 📞 ElevenLabs x Twilio Voice Integration

This project integrates **Twilio** and **ElevenLabs Conversational AI** to enable real-time voice conversations using a custom WebSocket-based audio interface. It allows you to route Twilio voice calls to an ElevenLabs AI agent using a Flask server and a WebSocket-compatible audio bridge.

## 🚀 Features

- Redirect incoming Twilio calls to an ElevenLabs "Talk-To" agent.
- Stream audio between Twilio and ElevenLabs via a custom audio interface.
- Real-time audio processing with base64 encoding and WebSocket communication.
- Clean Flask API endpoint for handling Twilio webhook events.

---

## 🧰 Requirements

Install all Python dependencies using pip:

```bash
pip install fastapi uvicorn python-dotenv twilio elevenlabs websockets
```
You will also need:

Ngrok: To expose your local server to the public internet for Twilio to reach it.

Setup Instructions
1. Start Flask App
```bash
python app.py
By default, it runs on http://localhost:5000.

2. Start Ngrok
```bash
ngrok http 5000
Copy the generated HTTPS URL (e.g., https://abc123.ngrok.io).

3. Configure Twilio Webhook
Set your Twilio number's Voice Webhook to point to:

arduino
```bash
https://your-ngrok-url.ngrok.io/voice
Replace with your actual ngrok URL.
