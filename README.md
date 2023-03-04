# Sparkevent-Context-Based Chatbot using OpenAI 

This project implements a context-based chatbot using OpenAI's GPT-3 language model. The chatbot can answer users' questions based on the provided context. If the question that users ask is not in context, the chatbot responds with a message indicating that the question is not in context.

## Requirements

To run this project, you will need to install the following Python packages:

- `gradio`
- `openai`
- `python-dotenv`

You will also need an API key for OpenAI's GPT-3 language model.

## Usage

1. Clone this repository.
2. Create a `.env` file in the project directory and add the following environment variables:
- OPENAI_API_KEY
- OPENAI_API_BASE
- OPENAI_API_TYPE
- OPENAI_API_VERSION
3. Run the following command to install the required packages:
pip install -r requirements.txt
4. Run the `app.py` file:
python app.py
5. Open your web browser and go to `http://localhost:7860`. You should see the Gradio interface for the chatbot.
6. Enter the context in the textbox provided and click on "Submit".
7. Type your question in the "Messages" textbox and hit "Enter". The chatbot will respond with an answer based on the provided context.

##notebook Q&A with AOAI
![image](https://user-images.githubusercontent.com/110788250/222911428-20d577c7-86c7-47e4-8985-ef18ae485689.png)

## Contributing
If you want to contribute to this project, please feel free to fork the repository and submit a pull request.

