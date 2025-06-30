# main.py - Flashcard Generator using a PDF or text input
from flashcard_generator import generate_flashcards

print("📘 AI Flashcard Study App")
text = input("Enter your notes or paste text:
")
flashcards = generate_flashcards(text)

print("\nGenerated Flashcards:")
for i, card in enumerate(flashcards, 1):
    print(f"Q{i}: {card['question']}")
    print(f"A{i}: {card['answer']}\n")