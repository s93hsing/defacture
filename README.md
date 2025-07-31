# Defacture: A Platform for News Comparison and Fact Verification

Defacture is a modular Streamlit-based application designed to help users compare news narratives across sources, explore language model (LLM) agent reasoning, and evaluate news credibility using a rule-based fact-checking system. This project demonstrates three distinct approaches to understanding and analyzing news content:

1. **News API Comparison**  
   Fetches and compares articles on a topic from different news APIs. This allows users to view multiple perspectives on the same event and observe differences in framing or emphasis.

2. **LangChain Agent Comparison**  
   Utilizes LangChain’s agent framework to simulate how an AI model might retrieve alternative sources and generate a comparative summary. This component mimics decision-making and reasoning capabilities within an agent-based workflow.

3. **Rule-Based Fact Checker**  
   Applies a lightweight, interpretable set of pattern-matching rules to classify a news article as "Likely Real", "Likely Fake", or "Uncertain" based on textual cues. This module helps demonstrate how explainable heuristics can assist in identifying suspicious or misleading content.

---

## Project Structure

defacture/
│
├── main.py
├── news_api_app.py
├── langchain_app.py
├── external_tool_app.py
├── api_fetcher.py
├── langchain_tools.py
├── fact_checker.py
├── sample_articles.json
├── News_Category_Dataset_v3.jsonl
├── styles.css
├── .env
├── requirements.txt
└── README.md




---

## Setup Instructions

Follow these steps to set up and run the Defacture application:

1. **Clone the Repository**

```
git clone https://github.com/your-username/defacture.git
cd defacture
```

2. **Create and Activate a Virtual Environment**

For Windows:

```
python -m venv venv
venv\Scripts\activate
```

For macOS/Linux:

```
python3 -m venv venv
source venv/bin/activate
```

3. **Install Required Python Packages**

```
pip install -r requirements.txt
```

4. **Create the `.env` File and Add Your API Keys**

In the root of the project, create a file named `.env` and include the following:

```
OPENAI_API_KEY=your_openai_key_here
NEWS_API_KEY=your_newsapi_key_here
```

*You can get your OpenAI API key from: [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
*You can get your NewsAPI key from: [https://newsapi.org/](https://newsapi.org/)

5. **Run the Streamlit Application**

```
streamlit run main.py
```

After launching, the application will be available at:

```
http://localhost:8501
```



