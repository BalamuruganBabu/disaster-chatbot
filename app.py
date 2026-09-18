from flask import Flask, request, jsonify, render_template
from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

SYSTEM_PROMPT = """You are DISHA (Disaster Information and Safety Help Assistant), 
an AI-powered early warning and emergency communication assistant developed to support 
disaster preparedness and response in India.

Your responsibilities:
- Provide clear, calm, and actionable guidance during natural disasters (floods, earthquakes, 
  cyclones, landslides, heatwaves, tsunamis, wildfires)
- Share emergency contact numbers (NDMA: 1078, Police: 100, Ambulance: 108, Fire: 101)
- Explain evacuation procedures and safe shelter guidelines
- Describe first-aid steps for disaster-related injuries
- Provide early warning signs for different disaster types
- Guide users on emergency kit preparation and family safety plans
- Answer questions in simple, easy-to-understand language
- If the user seems to be in immediate danger, always prioritise directing them to call emergency services first

Always be concise, reassuring, and practical. If you don't know specific local details, 
say so clearly and direct the user to official sources like NDMA (ndma.gov.in) or 
state disaster management authorities."""

# Store conversation per session (simple in-memory for demo)
conversations = {}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        user_message = data.get("message", "").strip()
        session_id = data.get("session_id", "default")

        if not user_message:
            return jsonify({"error": "Empty message"}), 400

        if session_id not in conversations:
            conversations[session_id] = []

        conversations[session_id].append({
            "role": "user",
            "content": user_message
        })

        history = conversations[session_id][-10:]

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[{"role": "system", "content": SYSTEM_PROMPT}] + history,
            max_tokens=600,
            temperature=0.7,
        )

        reply = response.choices[0].message.content

        conversations[session_id].append({
            "role": "assistant",
            "content": reply
        })

        return jsonify({"reply": reply})

    except Exception as e:
        print("FULL BACKEND ERROR:", str(e))
        return jsonify({"error": str(e)}), 500

@app.route("/reset", methods=["POST"])
def reset():
    session_id = request.json.get("session_id", "default")
    conversations.pop(session_id, None)
    return jsonify({"status": "cleared"})

@app.route("/health")
def health():
    return jsonify({"status": "ok", "model": "openai/gpt-oss-20b"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
