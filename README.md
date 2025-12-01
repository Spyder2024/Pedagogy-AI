
# **🎓 Pedagogy AI**

### An Autonomous Multi-Agent System for Educational Content Auditing & Quiz Generation.

<img width="2816" height="1536" alt="Gemini_Generated_Image_5bpwvr5bpwvr5bpw" src="https://github.com/user-attachments/assets/b8e11ce2-a51a-4cd5-a047-d2f993a58264" />

Pedagogy AI uses a Hub-and-Spoke architecture to ingest raw educational text, analyze its structure using deterministic tools, and generate verified quiz content using specialized AI agents. It is built in Pure Python to demonstrate deep understanding of Agent primitives without external frameworks.


## 🏗️ Architecture

The system follows a strict Object-Oriented design pattern:
The Hub (Orchestrator): The central controller that manages the workflow and SessionState.

Spoke 1 (Custom Tool): A deterministic Python Regex tool extracts keywords to ground the AI in facts.

Spoke 2 (The Analyst): An AI agent that summarizes content based only on the extracted keywords.

Spoke 3 (The Quiz Master): An AI agent that generates JSON questions based only on the Analyst's summary (preventing hallucination from raw text).

<img width="2816" height="1536" alt="Gemini_Generated_Image_9stub59stub59stu" src="https://github.com/user-attachments/assets/ea0b08d0-063a-4fb5-b0fa-c69ff7ea416e" />

### 📂 File Structure

File	Responsibility

**main.py**	Entry Point. Handles CLI execution and exposes the Flask app factory.

**orchestrator.py**	The Hub. Manages logic flow and error handling.

**agents.py**	The Brains. Defines AnalystAgent and QuizMasterAgent (Inheritance).

**tools.py**	The Tools. Deterministic functions (Regex/NLP) for factual data extraction.
**
state.py**	The Memory. A SessionState dataclass for persistence and logging.

### 🚀 Key Features (Rubric Implementation)

Multi-Agent Orchestration: Implements a coordinator pattern where agents pass data via a shared state, not direct chat.

Hybrid Intelligence: Combines Symbolic AI (Regex for keywords) with Generative AI (Gemini 1.5 Pro) for optimal accuracy.

State Management: A robust SessionState class persists the context, logs, and results across the lifecycle of a request.

Observability: Built-in tracing logs (state.log) allow developers to see exactly why an agent made a decision.

<img width="2816" height="1536" alt="Gemini_Generated_Image_9stub59stub59stu (2)" src="https://github.com/user-attachments/assets/5b853e2e-2739-401c-ba93-acd86b9d4847" />

🛠️ Installation & Setup
Prerequisites
Python 3.10+
A Google Cloud Project with Gemini API enabled.

1. Clone & Install
code
Bash
git clone https://github.com/your-repo/pedagogy-ai.git
cd pedagogy-ai
pip install google-generativeai flask

2. Set API Key
You must set your Gemini API key as an environment variable.
code
Bash

# Linux/Mac
export GEMINI_API_KEY="your_actual_api_key_here"

# Windows (PowerShell)
$env:GEMINI_API_KEY="your_actual_api_key_here"

💻 Usage
Option A: Run Locally (CLI Mode)
Perfect for testing the agents' logic immediately.
code
Bash
python main.py
Output: You will see the step-by-step logs, the extracted keywords, the analyst summary, and the final JSON quiz printed to the console.

Option B: Run as a Web Server (API Mode)
The project includes a Flask wrapper for API access.
code
Bash

# Start the server
export FLASK_APP=main.py

flask run --port 8080

Test with cURL:

code
Bash
curl -X POST http://127.0.0.1:8080/audit \
     -H "Content-Type: application/json" \
     -d '{"text": "Photosynthesis turns light into chemical energy using Chlorophyll."}'

☁️ Deployment (Google Cloud Run)
Since the application is stateless (using SessionState per request) and container-ready, it can be deployed easily.
Create a Procfile (for gunicorn):
code
Text
web: gunicorn "main:create_app()" --bind 0.0.0.0:$PORT

Deploy Command:
code
Bash
gcloud run deploy pedagogy-ai \
  --source . \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars GEMINI_API_KEY="your_key"

### ⚠️ Limitations & Guidelines

Strict Typing: The codebase uses typing.List and typing.Dict to ensure data integrity.

No Hardcoded Keys: Security best practices are followed by using os.environ.

Error Handling: The JSON parser includes try/except blocks to handle potential LLM formatting errors gracefully.
