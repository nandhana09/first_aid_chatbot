import streamlit as st
import json
import random

# Load the dataset
with open(r"E:\NikkiBot\venv\dataset\intents.json", "r") as f:
    data = json.load(f)

# Initialize session state for search history
if "search_history" not in st.session_state:
    st.session_state.search_history = []

# Function to get the bot's response
def get_bot_response(user_input):
    intent = None
    for item in data["intents"]:
        for pattern in item["patterns"]:
            if pattern.lower() in user_input.lower():
                intent = item
                break

    if intent:
        responses = intent["responses"]
        return random.choice(responses)
    else:
        return "I'm sorry, I don't understand that."

# Streamlit app
def main():
    st.set_page_config(
        page_title="NikkiBot",
        layout="wide",
    )

    st.title("NikkiBot")

    # Sidebar with details
    st.sidebar.markdown("## NikkiBot")
    st.sidebar.text("Version: 1.0")
    st.sidebar.text("Developer: Nandhana PK")
    st.sidebar.text("Contact: nandhana2001@gmail.com")

    # Sidebar for search history
    with st.sidebar:
        st.markdown("## Search History")
        # Display search history from session state
        for search in st.session_state.search_history:
            st.text(search)

    user_input = st.text_input("You:", "")
    if st.button("Submit"):
        bot_response = get_bot_response(user_input)
        st.text_area("NikkiBot:", bot_response, height=100)

        # Add the current search to the session state history
        st.session_state.search_history.append(user_input)

if __name__ == "__main__":
    main()
