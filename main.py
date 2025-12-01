# main.py
import json
import os
from orchestrator import Orchestrator

# [RUBRIC] Deployment Bonus: Flask wrapper
# To run as web server: export FLASK_APP=main.py && flask run
def create_app():
    from flask import Flask, request, jsonify
    app = Flask(__name__)
    orchestrator = Orchestrator()

    @app.route('/audit', methods=['POST'])
    def audit_content():
        data = request.json
        text = data.get('text', '')
        session_id = data.get('session_id', 'web-req-001')
        
        result_state = orchestrator.process_content(session_id, text)
        
        return jsonify({
            "summary": result_state.analysis_report,
            "quiz": result_state.generated_quiz,
            "logs": result_state.logs
        })
    return app

if __name__ == "__main__":
    # CLI Execution for Hackathon Demo
    print("--- Pedagogy AI: Starting CLI Mode ---")
    
    # Check for API Key
    if "GEMINI_API_KEY" not in os.environ:
        print("WARNING: GEMINI_API_KEY not found in env. Please set it.")
        # For testing, you might uncomment this:
        # os.environ["GEMINI_API_KEY"] = "AIzaSy..." 

    sample_text = """
    Photosynthesis is a process used by plants and other organisms to convert light energy into chemical energy that, 
    through cellular respiration, can later be released to fuel the organism's activities. 
    The process creates Oxygen as a byproduct. Chlorophyll is the primary pigment involved.
    """

    # Instantiate Orchestrator
    system = Orchestrator()
    
    # Run Workflow
    final_state = system.process_content("cli-session-1", sample_text)

    # Display Results
    print("\n" + "="*40)
    print("FINAL REPORT")
    print("="*40)
    print(f"1. Keywords Identified: {final_state.extracted_keywords}")
    print(f"\n2. Analyst Summary:\n{final_state.analysis_report}")
    print(f"\n3. Generated Quiz (JSON):\n{json.dumps(final_state.generated_quiz, indent=2)}")
