import streamlit as st
import requests
import json

# GitHub repository link
GITHUB_REPO_URL = "https://github.com/lucylu20020801/daily-marketing-news"


# Function to fetch the latest marketing news
def get_latest_marketing_news():
    search_url = "https://newsapi.org/v2/everything"
    params = {
        "q": "marketing",
        "sortBy": "publishedAt",
        "apiKey": "ff5a3ec0da7d4280950ed3964ec02a99",  # Replace with your actual NewsAPI key
        "language": "en",
        "pageSize": 3  # Fetch only 3 articles
    }
    response = requests.get(search_url, params=params)
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        return articles
    else:
        return []


# Function to process .lnntl files
def process_lnntl_file(uploaded_file):
    try:
        file_content = uploaded_file.read()
        decoded_content = file_content.decode("utf-8")

        # Try to parse as JSON (if structured)
        try:
            json_data = json.loads(decoded_content)
            return json.dumps(json_data, indent=4)  # Pretty print JSON
        except json.JSONDecodeError:
            pass  # If not JSON, treat it as plain text

        return decoded_content  # Return as text if not JSON
    except Exception as e:
        return f"Error reading file: {e}"


# Streamlit UI
st.title("📢 AI Marketing News & File Processor")

# Section 1: Fetch latest marketing news
st.header("🔍 Get the Latest Marketing News")

if st.button("Fetch News 🚀"):
    news_list = get_latest_marketing_news()
    if news_list:
        for index, news in enumerate(news_list, start=1):
            st.subheader(f"📌 {news['title']}")
            st.write(news['description'])
            st.write(f"[Read more]({news['url']})")
    else:
        st.warning("Failed to fetch the latest news. Please try again later!")

# Section 2: Upload & Process .lnntl File
st.header("📂 Upload an .lnntl File")

uploaded_file = st.file_uploader("Choose an .lnntl file", type=["lnntl"])

if uploaded_file is not None:
    st.success("File uploaded successfully!")

    # Process file and display content
    file_content = process_lnntl_file(uploaded_file)

    # Display content in a text area
    st.text_area("File Content:", file_content, height=300)

# GitHub repository link
st.markdown(f"[📂 Visit GitHub Repository]({GITHUB_REPO_URL})")