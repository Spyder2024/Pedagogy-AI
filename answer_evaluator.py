from sentence_transformers import SentenceTransformer, util

class AnswerEvaluator:
    def __init__(self):
        print("Loading Answer Evaluator Model (all-MiniLM-L6-v2)...")
        # This model is small and fast, perfect for CPU usage
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        print("Evaluator Model loaded.")

    def evaluate(self, student_answer, reference_answer):
        if not student_answer or not reference_answer:
            return 0.0, "Missing answer content."

        # Compute embeddings
        embeddings = self.model.encode([student_answer, reference_answer], convert_to_tensor=True)

        # Compute cosine similarity
        cosine_scores = util.cos_sim(embeddings[0], embeddings[1])
        score = cosine_scores.item() # Convert tensor to float

        # Generate qualitative feedback based on score
        feedback = self._generate_feedback(score)

        return round(score * 100, 2), feedback

    def _generate_feedback(self, score):
        if score > 0.85:
            return "Excellent! Your answer is semantically identical to the reference."
        elif score > 0.70:
            return "Good job. You captured the main concept, but missed some nuance."
        elif score > 0.50:
            return "You're on the right track, but the answer is incomplete or slightly off-topic."
        elif score > 0.30:
            return "Some relevance found, but significant details are missing."
        else:
            return "Incorrect. Your answer does not match the context."