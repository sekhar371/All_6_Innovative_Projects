# main.py - Error Detector for Beginner Code
from fixer import suggest_fix

print("🛠️ Paste your Python code:")
user_code = input(">>> ")
fix = suggest_fix(user_code)
print(f"Suggested fix: {fix}")