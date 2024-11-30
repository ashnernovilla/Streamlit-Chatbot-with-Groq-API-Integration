# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 22:00:00 2024

@author: ASHNER_NOVILLA
"""

import streamlit as st
from time import sleep
from groq import Groq

# Streamlit header
st.header("**Groq Fast AI Inference Deployment** 🤖")
st.caption("This is an LLM PoC using Groq Fast AI Inference.")
st.caption("Author: Ashner Novilla :sunglasses:")


# Function to access Groq API
def groq_access(content):
    try:
        # Retrieve the API key from Streamlit Secrets
        api_key = st.secrets["GROQ_API_KEY"]

        # Initialize the Groq client with the API key
        client = Groq(api_key=api_key)

        # Make a request to the Groq API
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": content,
                }
            ],
            model="llama3-8b-8192",
        )
        # Return the bot's response
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"


# Function to stream response dynamically
def stream_data(response_chat):
    """
    Stream response one word at a time.
    """
    for word in response_chat.split(" "):
        yield word + " "
        sleep(0.0002)


# Initialize conversation history
if "history" not in st.session_state:
    st.session_state["history"] = []

# Chat input and processing
prompt = st.chat_input("Ask the bot something (type 'quit' to stop)")
if prompt:
    if prompt.lower() == "quit":
        st.write("**Chatbot session ended. Refresh the page to start a new conversation.**")
    else:
        # Add user message to history
        st.session_state["history"].append({"role": "user", "message": prompt})

        # Get bot response
        bot_response = groq_access(prompt)
        st.session_state["history"].append({"role": "bot", "message": bot_response})

# Display conversation history with streaming
for entry in st.session_state["history"]:
    if entry["role"] == "user":
        st.chat_message("user").write(entry["message"])
    elif entry["role"] == "bot":
        # Stream the bot's response dynamically
        placeholder = st.chat_message("assistant").empty()
        streamed_text = ""
        for chunk in stream_data(entry["message"]):
            streamed_text += chunk
            placeholder.write(f"**Bot:** {streamed_text}")
