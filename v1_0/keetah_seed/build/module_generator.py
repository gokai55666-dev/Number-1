def suggest_modules(report):

    suggestions = []

    total_functions = sum(r["functions"] for r in report)

    if total_functions < 5:
        suggestions.append("Expand functionality with more modules")

    suggestions.append("Add GPU manager module")
    suggestions.append("Add reward system")
    suggestions.append("Add environment monitoring")

    return suggestions