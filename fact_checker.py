import re

def rule_based_fact_check(article_text):
    """
    Simulated rule-based fact-checker.
    Returns 'Likely Real', 'Likely Fake', or 'Uncertain' based on keyword heuristics.
    """
    if not article_text or not isinstance(article_text, str):
        return "Uncertain"

    lower_text = article_text.lower()

    suspicious_patterns = [
        r"shocking discovery", r"you won't believe", r"miracle cure",
        r"hidden truth", r"banned information", r"unreported by mainstream media"
    ]

    trusted_indicators = [
        "reuters", "associated press", "bbc", "nyt", "official", "according to government"
    ]

    if any(re.search(pattern, lower_text) for pattern in suspicious_patterns):
        return "Likely Fake"

    if any(keyword in lower_text for keyword in trusted_indicators):
        return "Likely Real"

    return "Uncertain"
