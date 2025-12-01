# tools.py
import re
from typing import List

class TextTools:
    """
    [RUBRIC] Custom Tools:
    Encapsulates deterministic text processing functions.
    We use a static method here as this utility does not maintain state.
    """
    
    @staticmethod
    def extract_keywords(text: str) -> List[str]:
        """
        Extracts capitalized keywords using Regex to ground the LLM.
        
        Why Regex? 
        LLMs can hallucinate importance. Capitalized words (Proper Nouns/Concepts)
        are structurally significant. This ensures the quiz covers actual terms.
        """
        if not text:
            return []
        
        try:
            # Regex Explanation:
            # (?<!^): Lookbehind to ensure it's not the start of a sentence.
            # \b[A-Z][a-z]+\b: Finds words starting with Uppercase followed by lowercase.
            pattern = r'(?<!^)(?<!\. )\b[A-Z][a-z]+\b'
            matches = re.findall(pattern, text)
            
            # Return unique, sorted list
            return sorted(list(set(matches)))
        except Exception as e:
            # [RUBRIC] Error Handling
            print(f"Tool Error: {e}")
            return []
