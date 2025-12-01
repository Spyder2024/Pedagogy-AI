Here is a professional, submission-ready README.md file. It is structured to help judges instantly understand the architecture, run the code locally, and see how it deploys to the cloud.

🎓 Pedagogy AI

An Autonomous Multi-Agent System for Educational Content Auditing & Quiz Generation.

<img width="2816" height="1536" alt="Gemini_Generated_Image_5bpwvr5bpwvr5bpw" src="https://github.com/user-attachments/assets/dbf447f4-db60-486f-86e0-1235de774b53" />

Pedagogy AI uses a Hub-and-Spoke architecture to ingest raw educational text, analyze its structure using deterministic tools, and generate verified quiz content using specialized AI agents. It is built in Pure Python to demonstrate deep understanding of Agent primitives without external frameworks.

🏗️ Architecture

The system follows a strict Object-Oriented design pattern:

The Hub (Orchestrator): The central controller that manages the workflow and SessionState.

Spoke 1 (Custom Tool): A deterministic Python Regex tool extracts keywords to ground the AI in facts.

Spoke 2 (The Analyst): An AI agent that summarizes content based only on the extracted keywords.

Spoke 3 (The Quiz Master): An AI agent that generates JSON questions based only on the Analyst's summary (preventing hallucination from raw text).

<img width="2816" height="1536" alt="Gemini_Generated_Image_9stub59stub59stu" src="https://github.com/user-attachments/assets/265dd9aa-3e8f-4dc8-ba35-b8cf2ae43213" />

📂 File Structure
File	Responsibility
main.py	Entry Point. Handles CLI execution and exposes the Flask app factory.
orchestrator.py	The Hub. Manages logic flow and error handling.
agents.py	The Brains. Defines AnalystAgent and QuizMasterAgent (Inheritance).
tools.py	The Tools. Deterministic functions (Regex/NLP) for factual data extraction.
state.py	The Memory. A SessionState dataclass for persistence and logging.
🚀 Key Features (Rubric Implementation)

Multi-Agent Orchestration: Implements a coordinator pattern where agents pass data via a shared state, not direct chat.

Hybrid Intelligence: Combines Symbolic AI (Regex for keywords) with Generative AI (Gemini 1.5 Pro) for optimal accuracy.

State Management: A robust SessionState class persists the context, logs, and results across the lifecycle of a request.

Observability: Built-in tracing logs (state.log) allow developers to see exactly why an agent made a decision.

🛠️ Installation & Setup
Prerequisites

Python 3.10+

A Google Cloud Project with Gemini API enabled.

1. Clone & Install
code
Bash
download
content_copy
expand_less
git clone https://github.com/your-repo/pedagogy-ai.git
cd pedagogy-ai
pip install google-generativeai flask
2. Set API Key

You must set your Gemini API key as an environment variable.

code
Bash
download
content_copy
expand_less
# Linux/Mac
export GEMINI_API_KEY="your_actual_api_key_here"

# Windows (PowerShell)
$env:GEMINI_API_KEY="your_actual_api_key_here"
💻 Usage
Option A: Run Locally (CLI Mode)

Perfect for testing the agents' logic immediately.

code
Bash
download
content_copy
expand_less
python main.py

Output: You will see the step-by-step logs, the extracted keywords, the analyst summary, and the final JSON quiz printed to the console.

Option B: Run as a Web Server (API Mode)

The project includes a Flask wrapper for API access.

code
Bash
download
content_copy
expand_less
# Start the server
export FLASK_APP=main.py
flask run --port 8080

Test with cURL:

code
Bash
download
content_copy
expand_less
curl -X POST http://127.0.0.1:8080/audit \
     -H "Content-Type: application/json" \
     -d '{"text": "Photosynthesis turns light into chemical energy using Chlorophyll."}'
☁️ Deployment (Google Cloud Run)

Since the application is stateless (using SessionState per request) and container-ready, it can be deployed easily.

Create a Procfile (for gunicorn):

code
Text
download
content_copy
expand_less
web: gunicorn "main:create_app()" --bind 0.0.0.0:$PORT

Deploy Command:

code
Bash
download
content_copy
expand_less
gcloud run deploy pedagogy-ai \
  --source . \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars GEMINI_API_KEY="your_key"
⚠️ Limitations & Guidelines

Strict Typing: The codebase uses typing.List and typing.Dict to ensure data integrity.

No Hardcoded Keys: Security best practices are followed by using os.environ.

Error Handling: The JSON parser includes try/except blocks to handle potential LLM formatting errors gracefully.
