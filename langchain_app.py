import streamlit as st
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from tools.langchain_tools import search_alt_articles, compare_articles

st.set_page_config(page_title="LangChain Agent Comparison", layout="wide")
st.title("🧠 LangChain Agent: News Comparison")

# Load your LLM
llm = OpenAI(temperature=0.5)

# Define custom tools
tools = [
    Tool(
        name="AltArticleSearch",
        func=search_alt_articles,
        description="Finds an alternative source for a given news topic."
    ),
    Tool(
        name="ArticleComparator",
        func=compare_articles,
        description="Compares two news articles and summarizes the differences."
    )
]

# Initialize LangChain Agent
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

# Input prompt
query = st.text_input("Enter a news topic to compare:", value="Manipur unrest")

if st.button("Run Agent"):
    if query.strip():
        with st.spinner("Running LangChain Agent..."):
            try:
                response = agent.run(f"Compare BBC article on {query} with alt-sources")
                st.success("Comparison Complete:")
                st.markdown(f"**{response}**")
            except Exception as e:
                st.error(f"Agent Error: {str(e)}")
    else:
        st.warning("Please enter a topic to compare.")
