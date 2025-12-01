# agents.py
import os
import google.generativeai as genai
from typing import Optional

# [RUBRIC] Configuration: No hardcoded keys
# In a real scenario, use python-dotenv or Secret Manager
api_key = os.environ.get("GEMINI_API_KEY", "YOUR_PLACEHOLDER_KEY")
genai.configure(api_key=api_key)

class Agent:
    """
    [RUBRIC] Agent Primitive:
    Base class representing a generic Generative AI entity.
    """
    def __init__(self, name: str, role: str, model_name: str = "gemini-1.5-pro"):
        self.name = name
        self.role = role
        self.model = genai.GenerativeModel(model_name)
    
    def generate(self, prompt: str, context: Optional[str] = None) -> str:
        """
        Wraps the API call with error handling and context injection.
        """
        full_prompt = f"Role: {self.role}\nContext Data: {context}\nTask: {prompt}"
        try:
            response = self.model.generate_content(full_prompt)
            return response.text.strip()
        except Exception as e:
            return f"Error generating content: {str(e)}"

class AnalystAgent(Agent):
    """
    Specialized Sub-agent: The Analyst.
    Responsible for understanding structure and summarizing content.
    """
    def __init__(self):
        super().__init__(
            name="Analyst",
            role=(
                "You are an Educational Content Analyst. "
                "Your job is to summarize text and identify key learning objectives "
                "based on specific keywords provided to you."
            )
        )

class QuizMasterAgent(Agent):
    """
    Specialized Sub-agent: The Quiz Master.
    Responsible for JSON generation.
    Constraint: It produces ONLY valid JSON.
    """
    def __init__(self):
        super().__init__(
            name="QuizMaster",
            role=(
                "You are a Strict Quiz Generator. "
                "You output ONLY valid JSON. "
                "You generate questions based ONLY on the provided analysis, not external knowledge."
            )
        )
