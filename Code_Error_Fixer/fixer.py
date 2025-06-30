# fixer.py - Suggests fixes for common Python beginner errors
def suggest_fix(code):
    if "print " in code:
        return "Use parentheses: print(...) instead of print ..."
    elif "=" in code and "==" not in code and "if" in code:
        return "Use '==' for comparisons inside if-statements"
    else:
        return "Code looks good or needs manual review."