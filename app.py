import streamlit as st
from dotenv import load_dotenv
import os
import requests

# Load environment variables
load_dotenv()

st.set_page_config(page_title="Financial Analyst AI", page_icon="💹", layout="wide")

st.title("💹 Financial Analyst AI Multi-Agent System")
st.markdown("""
Welcome to the **Financial Analyst AI**. Use the sidebar to select an agent and enter your query. Results will be displayed below in a professional, easy-to-read format.
""")

# Sidebar for agent selection and input
st.sidebar.header("Agent Selection")
agent = st.sidebar.selectbox("Choose an agent:", ["Finance AI Agent", "Web Search Agent"])

st.sidebar.header("Query Input")
user_query = st.sidebar.text_area("Enter your query:")

submit = st.sidebar.button("Submit Query")

# Placeholder for results
def display_results(results):
    if isinstance(results, str):
        st.markdown(results, unsafe_allow_html=True)
    elif isinstance(results, dict):
        for key, value in results.items():
            st.subheader(key)
            st.write(value)
    else:
        st.write(results)

# Simulate agent responses (replace with real backend integration)
def run_agent(agent, query):
    # Prefix the agent name to the query for backend routing
    prompt = f"[{agent}] {query}"
    try:
        response = requests.post(
            "http://localhost:8000/query",
            json={"prompt": prompt},
            timeout=30
        )
        response.raise_for_status()
        data = response.json()
        return data.get("response", "No response from backend.")
    except Exception as e:
        return f"<span style='color:red;'>Error contacting backend: {e}</span>"

# Main logic
if submit and user_query:
    with st.spinner("Processing your query..."):
        results = run_agent(agent, user_query)
        display_results(results)
elif submit:
    st.warning("Please enter a query before submitting.")

# Footer
st.markdown("---")
st.markdown("<div style='text-align:center;'>© 2024 Financial Analyst AI | Powered by Streamlit</div>", unsafe_allow_html=True) 