# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 16:51:06 2024

@author: ASHNER_NOVILLA
"""

import os

import streamlit as st
from time import sleep
import os
#from dotenv import load_dotenv
from groq import Groq

# Load environment variables
#load_dotenv()


st.header("**Groq is Fast AI Inference Deployment** 🤖")
st.caption("This is a LLM PoC using Groq Fast AI Inference.")
st.caption("Author: Ashner Novilla :sunglasses:")


# Function to access Groq API
def groq_access(content):
    try:
        # client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        client = Groq(api_key = os.getenv('GROQ_API_KEY'))
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": content,
                }
            ],
            model="llama3-8b-8192",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Function to stream response
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
