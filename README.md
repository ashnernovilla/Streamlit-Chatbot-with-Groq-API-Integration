# Streamlit-Chatbot-with-Groq-API-Integration
This repository contains a Streamlit-based chatbot that integrates with the Groq API for natural language processing. The chatbot supports dynamic user interaction with streaming responses to create a seamless conversational experience.



🚀 Features
- Streamlit Frontend: A simple and intuitive UI for user interaction.
- Groq API Integration: Leverages the Groq API to generate responses using the llama3-8b-8192 model.
- Streaming Responses: Dynamically displays responses one word at a time for real-time feedback.
- Session Management: Maintains conversation history within a single session.
- Error Handling: Gracefully manages API and runtime errors.



🛠️ Installation
1. Clone the repository:

    - git clone https://github.com/your-username/your-repo-name.git
    - cd your-repo-name

2. Set up the environment: Ensure you have Python 3.9 or later installed.

    - python -m venv venv
    - source venv/bin/activate  # On Windows: venv\Scripts\activate
    - pip install -r requirements.txt

3. Configure API Key:

    - Create a .env file in the project root.
    - Add your Groq API key:
      - GROQ_API_KEY=your_api_key_here

4. Run the app:

    - streamlit run app.py

5. Open your browser and go to: http://localhost:8501
