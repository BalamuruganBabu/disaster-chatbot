# 🆘 DISHA — Disaster Information & Safety Help Assistant

**An AI-powered chatbot for disaster early warning and emergency communication, built with Python, Flask, and Groq's Llama 3 LLM.**

> Developed as part of research alignment with IIT Delhi Project RP05119G:  
> *Generative AI-Enhanced Chatbot for Customer Support in Disaster Early Warning and Emergency Communication*

---

## Overview

DISHA (Disaster Information and Safety Help Assistant) is a conversational AI chatbot designed to assist users during natural disaster scenarios. It provides real-time, actionable guidance on flood evacuation, earthquake response, cyclone preparedness, tsunami warnings, emergency kit preparation, and more.

The system demonstrates how Large Language Models (LLMs) can be applied to critical public safety communication — a domain that demands higher reliability, clarity, and accessibility standards than conventional commercial chatbots.

---

## Features

- **Multi-turn conversation** with context memory across the session
- **Domain-tuned system prompt** for disaster safety and emergency response (India-specific)
- **Quick topic buttons** — flood, earthquake, cyclone, wildfire, tsunami, emergency kits
- **Emergency contacts bar** always visible (NDMA 1078, Police 100, Ambulance 108, Fire 101)
- **Typing indicator** with smooth UI for a responsive feel
- **Session reset** — start a new conversation anytime
- **Containerised** with Docker for easy deployment
- **REST API** with `/chat`, `/reset`, and `/health` endpoints

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.11, Flask 3.0 |
| LLM | Llama 3 (8B) via Groq API |
| LLM Client | `groq` Python SDK |
| Frontend | Vanilla HTML/CSS/JS (no framework) |
| Containerisation | Docker, Docker Compose |
| Deployment | Gunicorn WSGI server |

---

## Project Structure

```
disaster-chatbot/
├── app.py                 # Flask app — routes, LLM integration, session management
├── templates/
│   └── index.html         # Chat UI (single-page, no framework)
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
└── .gitignore
```

---

## Getting Started

### Prerequisites
- Python 3.10+
- A free Groq API key from [console.groq.com](https://console.groq.com) (no credit card needed)

### 1. Clone the repo
```bash
git clone https://github.com/BalamuruganBabu/disaster-chatbot.git
cd disaster-chatbot
```

### 2. Set up environment
```bash
cp .env.example .env
# Edit .env and add your GROQ_API_KEY
```

### 3. Run locally (without Docker)
```bash
pip install -r requirements.txt
export GROQ_API_KEY=your_key_here   # or set in .env
python app.py
```
Open [http://localhost:5000](http://localhost:5000)

### 4. Run with Docker
```bash
docker compose up --build
```
Open [http://localhost:5000](http://localhost:5000)

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET  | `/` | Chat UI |
| POST | `/chat` | Send message, get LLM response |
| POST | `/reset` | Clear conversation history for session |
| GET  | `/health` | Health check |

### Example `/chat` request
```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What should I do if a flood is approaching?", "session_id": "user_1"}'
```

### Response
```json
{
  "reply": "If a flood is approaching, act immediately: 1) Move to higher ground ..."
}
```

---

## System Prompt Design

The chatbot uses a carefully engineered system prompt that:
- Defines the assistant's identity (DISHA) and domain scope
- Prioritises emergency service referrals for life-threatening situations
- Uses India-specific emergency numbers and authority references (NDMA)
- Keeps responses concise, calm, and actionable
- Handles uncertainty gracefully (redirects to official sources like ndma.gov.in)

This prompt design approach is central to building reliable AI systems for high-stakes public safety applications.

---

## Relevance to Disaster Communication Research

This project directly addresses core challenges in AI-assisted emergency communication:

1. **Context retention** — multi-turn memory ensures users don't repeat information mid-crisis
2. **Domain grounding** — system prompt constrains the LLM to disaster safety scope
3. **Accessibility** — simple, fast UI designed for stressed users on any device
4. **Extensibility** — architecture supports future integration of STT/TTS for IVRS-style voice interfaces

---

## Future Enhancements

- [ ] Speech-to-text input (Web Speech API) for voice queries
- [ ] Text-to-speech output for IVRS-style voice responses
- [ ] Multilingual support (Hindi, Tamil, Telugu) for broader reach
- [ ] RAG pipeline with NDMA guidelines as knowledge base
- [ ] Fine-tuned model on disaster response datasets
- [ ] Redis-backed session storage for production scalability

---

## Author

**Balamurugan Babu**  
B.Tech Information Technology, Adithya Institute of Technology, Coimbatore  
[LinkedIn](https://linkedin.com/in/balamurugan1011) · [GitHub](https://github.com/BalamuruganBabu)

---

## License

MIT License — free to use, modify, and distribute.
