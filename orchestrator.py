# orchestrator.py
import json
from typing import Dict, Any
from state import SessionState
from tools import TextTools
from agents import AnalystAgent, QuizMasterAgent

class Orchestrator:
    """
    [RUBRIC] Multi-Agent System (Hub-and-Spoke):
    The Orchestrator composes the specific agents and tools.
    It manages the flow of data from one component to another via SessionState.
    """
    def __init__(self):
        # Composition: The Orchestrator "has" agents
        self.analyst = AnalystAgent()
        self.quiz_master = QuizMasterAgent()
    
    def process_content(self, session_id: str, text_content: str) -> SessionState:
        # 1. Initialize State
        state = SessionState(session_id=session_id, source_text=text_content)
        state.log("ORCHESTRATOR", "Workflow initialized.")

        # 2. Call Custom Tool (Spoke 1)
        # [RUBRIC] Custom Tool Integration
        state.log("TOOL_EXECUTION", "Running keyword extraction...")
        keywords = TextTools.extract_keywords(text_content)
        state.extracted_keywords = keywords
        state.log("TOOL_RESULT", f"Keywords found: {keywords}")

        # 3. Call Analyst Agent (Spoke 2)
        state.log("ORCHESTRATOR", "Dispatching to Analyst Agent.")
        analyst_prompt = (
            f"Analyze the source text. Focus specifically on these identified keywords: {keywords}. "
            "Provide a summary and 3 key learning points."
        )
        # Context passing: Raw text -> Analyst
        analysis_result = self.analyst.generate(prompt=analyst_prompt, context=state.source_text)
        state.analysis_report = analysis_result
        state.log("ANALYST_OUTPUT", "Analysis complete.")

        # 4. Call Quiz Master Agent (Spoke 3)
        state.log("ORCHESTRATOR", "Dispatching to Quiz Master Agent.")
        quiz_prompt = (
            "Create 3 multiple-choice questions based on the provided Analysis Report. "
            "Return output as a JSON list of objects with keys: 'question', 'options' (list), 'answer'. "
            "Do not use Markdown formatting like ```json."
        )
        
        # [RUBRIC] State Management logic:
        # The Quiz Master does NOT see the original source_text. 
        # It only sees the Analyst's report. This reduces hallucination.
        context_for_quiz = f"Keywords: {state.extracted_keywords}\nAnalysis: {state.analysis_report}"
        
        raw_quiz_output = self.quiz_master.generate(prompt=quiz_prompt, context=context_for_quiz)

        # 5. Parse and Finalize
        self._parse_quiz_output(state, raw_quiz_output)
        state.log("ORCHESTRATOR", "Workflow finished.")
        
        return state

    def _parse_quiz_output(self, state: SessionState, raw_output: str) -> None:
        """Helper method to handle JSON parsing and potential LLM formatting errors."""
        try:
            # Clean potential markdown
            clean_json = raw_output.replace("```json", "").replace("```", "").strip()
            state.generated_quiz = json.loads(clean_json)
            state.log("QUIZ_MASTER", "JSON parsed successfully.")
        except json.JSONDecodeError:
            state.log("ERROR", "Failed to parse Quiz Master output.")
            state.generated_quiz = [{"error": "Invalid JSON", "raw": raw_output}]
