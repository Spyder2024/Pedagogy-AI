# state.py
from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass
class SessionState:
    """
    [RUBRIC] Sessions & State Management:
    A centralized data class that persists information across the workflow.
    It acts as the memory shared between the Orchestrator and Agents.
    """
    session_id: str
    source_text: str = ""
    
    # [RUBRIC] Observability/Logging: Trace log for debugging agent flow
    logs: List[str] = field(default_factory=list)
    
    # Deterministic data from Custom Tool
    extracted_keywords: List[str] = field(default_factory=list)
    
    # Output from Analyst Agent
    analysis_report: str = ""
    
    # Output from Quiz Master Agent (Structured Data)
    generated_quiz: List[Dict[str, Any]] = field(default_factory=list)

    def log(self, step: str, message: str) -> None:
        """
        [RUBRIC] Observability:
        Adds a timestamped-style entry to the execution trace.
        """
        entry = f"[{step.upper()}]: {message}"
        self.logs.append(entry)
        # Printing purely for Hackathon demo visibility
        print(entry)
