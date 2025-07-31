import streamlit as st
from tools.news_fetcher import fetch_news_from_api

st.title("🔍 News API Comparison")

st.markdown("Enter a topic to fetch news articles from multiple sources and compare their headlines or summaries.")

query = st.text_input("Search Topic", value="Manipur violence")

if query:
    with st.spinner("Fetching articles..."):
        articles = fetch_news_from_api(query)

    if not articles:
        st.error("No articles found or failed to fetch.")
    else:
        st.success(f"Found {len(articles)} articles.")
        for article in articles:
            st.markdown(f"### {article['source']}")
            st.write(article['title'])
            st.write(article['summary'])
            st.markdown("---")
