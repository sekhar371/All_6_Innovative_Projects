# flashcard_generator.py - Simple keyword-based flashcard generator
import re

def generate_flashcards(text):
    sentences = re.split(r'[.!?]', text)
    flashcards = []
    for sentence in sentences:
        words = sentence.split()
        if len(words) > 5:
            question = "What is " + " ".join(words[:2]) + "?"
            answer = sentence.strip()
            flashcards.append({"question": question, "answer": answer})
    return flashcards