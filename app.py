from flask import Flask, render_template, request, jsonify
from question_generator import QuestionGenerator
from answer_evaluator import AnswerEvaluator
import traceback

app = Flask(__name__)

# Instantiate global models (Singleton pattern for the app lifespan)
# This prevents reloading models on every request.
try:
    qg_model = QuestionGenerator()
    eval_model = AnswerEvaluator()
except Exception as e:
    print(f"Critical Error loading models: {e}")
    exit(1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_question():
    try:
        data = request.get_json()
        context_text = data.get('context', '')

        if not context_text:
            return jsonify({'error': 'No text provided'}), 400

        result = qg_model.generate(context_text)
        
        return jsonify({
            'status': 'success',
            'question': result['question'],
            'reference_answer': result['reference_answer']
        })

    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': 'Internal Server Error during generation'}), 500

@app.route('/evaluate', methods=['POST'])
def evaluate_answer():
    try:
        data = request.get_json()
        student_answer = data.get('student_answer', '')
        reference_answer = data.get('reference_answer', '')

        if not student_answer or not reference_answer:
            return jsonify({'error': 'Missing student answer or reference context'}), 400

        score, feedback = eval_model.evaluate(student_answer, reference_answer)

        return jsonify({
            'status': 'success',
            'score': score,
            'feedback': feedback
        })

    except Exception as e:
        print(traceback.format_exc())
        return jsonify({'error': 'Internal Server Error during evaluation'}), 500

if __name__ == '__main__':
    # Threaded=True allows handling multiple requests (useful since models are global)
    app.run(debug=True, port=5000, threaded=True)