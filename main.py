import streamlit as st
import json
import os
from collections import defaultdict

# Load JSON
data_path = os.path.join("data", "sample_articles.json")
with open(data_path, "r", encoding="utf-8") as f:
    raw_articles = json.load(f)

# Step 1: Grouping manually or by a keyword (e.g., "Manipur")
articles = defaultdict(dict)

# We'll consider "Manipur Unrest" as a common topic
for item in raw_articles:
    if "Manipur" in item["title"] or "Manipur" in item["content"]:
        articles["Manipur Unrest"][item["source"]] = {
            "title": item["title"],
            "content": item["content"]
        }

# Streamlit UI
st.title("📰 de-Facture: Expand Your News Perspective")

if not articles:
    st.error("No topics found.")
else:
    topic = st.selectbox("🎯 Choose a Topic", list(articles.keys()))
    sources = list(articles[topic].keys())

    if len(sources) < 2:
        st.warning("⚠️ Only one source available for this topic. Please add more sources to compare.")
    else:
        main_source = st.selectbox("🗞️ Select Your News Source", sources)

        if st.button("🔍 Compare with Alternative Sources"):
            original = articles[topic][main_source]
            alt_sources = [s for s in sources if s != main_source]
            alt = articles[topic][alt_sources[0]]  # pick first alternative

            st.markdown("## 🧾 Original Article")
            st.write(f"**🗂️ Title:** {original['title']}")
            st.write(f"**📄 Content:** {original['content']}")

            st.markdown("## 🔁 Alternative Source")
            st.write(f"**🗂️ Title:** {alt['title']}")
            st.write(f"**📄 Content:** {alt['content']}")

            st.markdown("## 🧠 Summary Comparison")
            st.success("✅ Original article focuses on high-level reporting and official responses.")
            st.warning("❗ Alternative source reveals deeper context such as structural issues and local voices.")
            st.markdown("🔗 [Read More: BBC](https://www.bbc.com)")
            st.markdown("🔗 [Read More: Article14](https://article-14.com)")
