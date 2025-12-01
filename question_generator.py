import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import nltk

# Download nltk punkt for sentence splitting if not present
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

class QuestionGenerator:
    def __init__(self):
        print("Loading Question Generation Model (valhalla/t5-base-qg-hl)...")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model_name = "valhalla/t5-base-qg-hl"
        
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name).to(self.device)
        self.model.eval()
        print(f"QG Model loaded on {self.device}.")

    def _prepare_inputs(self, context, answer):
        # The model expects: "generate question: <answer> </s> context: <context>"
        input_text = f"generate question: {answer} </s> context: {context}"
        return input_text

    def _extract_likely_answer(self, text):
        """
        Simple heuristic: Pick the first sentence as the 'answer' to generate a question about.
        In a production V2, you would use NER or Keyphrase extraction here.
        """
        sentences = nltk.sent_tokenize(text)
        if not sentences:
            return text[:50] # Fallback
        
        # We select the first sentence that is between 20 and 100 chars for best results
        selected_answer = sentences[0]
        for sent in sentences:
            if 20 < len(sent) < 150:
                selected_answer = sent
                break
        
        return selected_answer

    def generate(self, context_text):
        if not context_text or len(context_text.strip()) < 10:
            raise ValueError("Context text is too short.")

        # 1. Select a span from text to be the 'answer' key
        target_answer = self._extract_likely_answer(context_text)

        # 2. Format input for T5
        input_text = self._prepare_inputs(context_text, target_answer)
        
        # 3. Tokenize
        inputs = self.tokenizer(
            input_text, 
            return_tensors="pt", 
            max_length=512, 
            truncation=True,
            padding="max_length"
        ).to(self.device)

        # 4. Generate Question
        with torch.no_grad():
            outputs = self.model.generate(
                input_ids=inputs["input_ids"],
                attention_mask=inputs["attention_mask"],
                max_length=64,
                num_beams=4,
                early_stopping=True
            )

        question = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        return {
            "question": question,
            "reference_answer": target_answer
        }