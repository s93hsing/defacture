import streamlit as st
import json
from fact_checker import rule_based_fact_check

st.title("🔎 External Tool: Rule-Based Fact Checker")

st.markdown("""
This module uses a simple rule-based system to detect suspicious or reliable patterns in article text.
""")

# Load sample data
try:
    with open("data/sample_articles.json", "r", encoding="utf-8") as f:
        articles = json.load(f)
except FileNotFoundError:
    st.error("sample_articles.json not found. Please add some articles to the file.")
    st.stop()

# Display each article and result
for idx, article in enumerate(articles[:10]):
    st.markdown(f"### 📰 Article {idx+1}")
    st.write(article.get("title", "Untitled"))
    content = article.get("content", "")
    st.write(content)

    result = rule_based_fact_check(content)
    st.markdown(f"**Prediction:** `{result}`")
    st.markdown("---")
