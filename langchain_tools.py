from langchain.agents import Tool

# Simulated tool: finds alternative article
def dummy_alt_article_search(query: str) -> str:
    return f"Simulated: Found Article14 on {query}"

# Simulated tool: compares two articles
def dummy_article_comparator(articles: str) -> str:
    return "Simulated: Alt-source highlights tribal grievances, BBC focuses on violence."

# Register tools for the LangChain agent
langchain_tools = [
    Tool(
        name="AltArticleSearch",
        func=dummy_alt_article_search,
        description="Search for alternative articles to compare against mainstream news."
    ),
    Tool(
        name="ArticleComparator",
        func=dummy_article_comparator,
        description="Compare two news articles and summarize the difference."
    )
]
