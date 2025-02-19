# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import streamlit as st
import requests

# GitHub repository link
GITHUB_REPO_URL = "https://github.com/your-username/your-repo"

# Function to fetch the latest marketing news
def get_latest_marketing_news():
    search_url = "https://newsapi.org/v2/everything"
    params = {
        "q": "marketing",
        "sortBy": "publishedAt",
        "apiKey": "ff5a3ec0da7d4280950ed3964ec02a99",  # Replace with your NewsAPI key
        "language": "en",
        "pageSize": 3  # Fetch only the latest 3 articles
    }
    response = requests.get(search_url, params=params)
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        return articles
    else:
        return []

# Streamlit UI
st.title("📢 Latest Marketing News")

# Button to fetch news
if st.button("Get the Latest Marketing News 🚀"):
    news_list = get_latest_marketing_news()
    if news_list:
        for index, news in enumerate(news_list, start=1):
            st.subheader(f"📌 {news['title']}")
            st.write(news['description'])
            st.write(f"[Read more]({news['url']})")
    else:
        st.warning("Failed to fetch the latest news. Please try again later!")

# GitHub repository link
GITHUB_REPO_URL = "https://github.com/lucylu20020801/daily-marketing-news"
st.markdown(f"[📂 Visit GitHub Repository]({GITHUB_REPO_URL})")
