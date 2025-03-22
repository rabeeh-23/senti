import streamlit as st

# Set up the Streamlit app
st.title("Simple Chatbot")

# Initialize session state for storing chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Ask me something...")

if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Simple chatbot logic
    if "hello" in user_input.lower():
        response = "Hi there! How can I help you today?"
    elif "how are you" in user_input.lower():
        response = "I'm just a bot, but I'm doing fine! How about you?"
    elif "bye" in user_input.lower():
        response = "Goodbye! Have a great day!"
    elif "what color is sky" in user_input.lower():
        response = "it's blue"
    elif "how old are you" in user_input.lower():
        response = "I'm an AI assistant i dont have age?"
    elif "who is the father of nation" in user_input.lower():
        response = "mahathma gandi"
    else:
        response = "I'm not sure how to respond to that."

    # Add chatbot message to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Display chatbot response
    with st.chat_message("assistant"):
        st.markdown(response)