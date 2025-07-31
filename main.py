import streamlit as st

st.set_page_config(page_title="Defacture - News Comparison", layout="wide")

st.title("📰 Defacture: News Comparison Platform")
st.markdown("Choose one of the apps from the sidebar to explore different approaches:")

st.sidebar.title("Choose App")
st.sidebar.page_link("apps/news_api_app.py", label="🔍 News API Comparison")
st.sidebar.page_link("apps/langchain_app.py", label="🧠 LangChain Agent Comparison")
st.sidebar.page_link("apps/external_tool_app.py", label="🔎 External Tool: Rule-Based Checker")
