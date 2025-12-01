# Pedagogy-AI
Transforming static study material into intelligent dialogue using T5 Transformers and Semantic Analysis.

This is a comprehensive, professional, and visually engaging README designed to stand out, particularly for a portfolio or competition submission like Kaggle.

It leverages the assets and technical details we've developed in the previous steps.

-----

<img width="2816" height="1536" alt="Gemini_Generated_Image_qeondrqeondrqeon (1)" src="https://github.com/user-attachments/assets/40d2e375-be7e-448b-99ad-c9b1811ba5c5" />

# 🎓 Pedagogy AI: The Autonomous Active Learning Agent

[](https://www.python.org/)
[](https://flask.palletsprojects.com/)
[](https://huggingface.co/)
[](https://opensource.org/licenses/MIT)

> **Transforming passive reading into active mastery using state-of-the-art NLP.**

-----

\<p align="center"\>
\<img src="image\_1.png" alt="Pedagogy AI Conceptual Header Image" width="800"\>
\</p\>

## 📖 About The Project

### The Problem: The "Illusion of Competence"

Students often read textbooks passively, nodding along and feeling like they understand the material. This is the "illusion of competence." True learning requires **active recall**—struggling to retrieve information from memory. However, self-learners face a critical bottleneck: creating high-quality practice questions is tedious, and grading your own open-ended answers objectively is impossible.

### The Solution: An On-Demand AI Tutor

**Pedagogy AI** acts as an autonomous educational agent to bridge this gap. It ingests any raw text—a chapter, an article, or study notes—and immediately transforms it into an interactive assessment loop.

By using advanced Large Language Models (LLMs) to generate relevant questions and semantic search models to evaluate answers based on *meaning* rather than keywords, it provides the immediate, objective feedback necessary for deep learning.

## ✨ Key Features

  * **🤖 Intelligent Question Generation:** Uses a fine-tuned T5 Transformer to generate factually accurate questions conditioned specifically on your provided text.
  * **🧠 Semantic Answer Evaluation:** Grades answers based on conceptual similarity using Sentence-BERT, not brittle keyword matching. It understands synonyms and phrasing differences.
  * **⚡ Instant Feedback Loop:** Provides an immediate score (0-100) and qualitative feedback to reinforce learning.
  * **🖥️ Distraction-Free UI:** A clean, modern interface built with Tailwind CSS designed to focus the user on the study material.

-----

## ⚙️ How It Works: The Architecture

The agent mimics the cognitive workflow of a human tutor using a two-stage machine learning pipeline.

<img width="2816" height="1536" alt="Gemini_Generated_Image_n884upn884upn884" src="https://github.com/user-attachments/assets/fd3e4a92-a3ef-428e-99bc-9afce9a76ad7" />

\<p align="center"\>
\<img src="image\_3.png" alt="Pedagogy AI Conceptual Flowchart" width="800"\>
\</p\>

### Stage 1: The "Teacher" (Question Generation)

We utilize a **T5 (Text-to-Text Transfer Transformer)** model specifically fine-tuned for the task of question generation.

  * Unlike generic LLMs that might hallucinate external facts, this model is conditioned strictly on the input context.
  * We prepend the prefix `generate question:` to the user's text.
  * The model uses **beam search** to explore multiple potential outputs, selecting the most logically sound and grammatically fluent question derived from the text.

### Stage 2: The "Grader" (Semantic Evaluation)

This is the core innovation. Standard regex or keyword-based graders fail when a student uses different phrasing than the textbook. We solve this using **Sentence-BERT (SBERT)** for Semantic Textual Similarity (STS).

1.  The system takes the **Student's Answer** and the **Reference Source Text**.
2.  It passes both through the SBERT model to generate dense, high-dimensional vector embeddings. These vectors represent the *meaning* of the text in numerical space.
3.  It calculates the **Cosine Similarity** between these two vectors. A high similarity score means the student's answer and the source text share the same semantic meaning, even if the words differ.

-----

## 📂 Project Structure

The project is organized for modularity and ease of deployment.

\<p align="center"\>
\<img src="image\_2.png" alt="Pedagogy AI Project File Structure" width="500"\>
\</p\>

  * `app.py`: The Flask backend API that serves the frontend and orchestrates the ML models.
  * `question_generator.py`: Encapsulates the T5 model logic for loading weights and generating questions.
  * `answer_evaluator.py`: Encapsulates the Sentence-BERT logic for embedding text and calculating cosine similarity scores.
  * `templates/index.html`: The single-page frontend interface.

-----

## 🛠️ Tech Stack

  * **Backend Framework:** Python (Flask)
  * **Machine Learning Libraries:** PyTorch, Hugging Face Transformers, Sentence-Transformers
  * **ML Models:**
      * QG: `valhalla/t5-base-qg-hl`
      * Eval: `sentence-transformers/all-MiniLM-L6-v2`
  * **Frontend:** HTML5, Vanilla JavaScript, Tailwind CSS (via CDN)

-----

## 🚀 Getting Started

Follow these steps to set up the project locally.

### Prerequisites

  * Python 3.8 or higher installed.
  * Git (optional, for cloning).

### Installation

1.  **Clone the repository** (or download the source files into a folder named `pedagogy-ai`):

    ```bash
    git clone https://github.com/yourusername/pedagogy-ai.git
    cd pedagogy-ai
    ```

2.  **Create and activate a virtual environment** (Recommended):

    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    *Note: The first time you run this, it will download the pre-trained ML models from Hugging Face (approx. 500MB - 1GB total). This is a one-time process.*

### Running the Application

1.  Start the Flask server:

    ```bash
    python app.py
    ```

2.  Wait for the output confirming the server is running:
    `* Running on http://127.0.0.1:5000`

3.  Open your web browser and navigate to **[http://127.0.0.1:5000](https://www.google.com/url?sa=E&source=gmail&q=http://127.0.0.1:5000)**.

-----

## 🛣️ Future Roadmap

  * [ ] **Adaptive Difficulty:** Implement logic where the agent generates harder analytical questions if the student scores well on factual questions.
  * [ ] **Precise Answer Extraction:** Integrate a QA model (like RoBERTa trained on SQuAD) to extract the exact "gold standard" answer span from the text for even more precise grading comparison.
  * [ ] **Database Integration:** Add SQLite or PostgreSQL to save user progress, generated questions, and scores.
  * [ ] **Docker Support:** Containerize the application for easy deployment to cloud platforms like AWS or Render.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome\! Feel free to check the [issues page](https://www.google.com/search?q=https://github.com/yourusername/pedagogy-ai/issues).



*Developed with ❤️ for active learners everywhere.*
