import gradio as gr
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

openai.api_type = os.getenv("OPENAI_API_TYPE")
openai.api_version = os.getenv("OPENAI_API_VERSION")
openai.api_base = os.getenv("OPENAI_API_BASE")
openai.api_key = os.getenv("OPENAI_API_KEY")


def predict(input,context, history=[]):
    prompt_keyword = 'Answer users question base on provide Context only. If Question that users ask is not in Context , Response not in context \n\Context:\n'+" ".join([context])+ '\n\Question:\n' + " ".join([input]) + '\n\Answer:\n'
    model_engine = "aouy-txt-davinci-003" # or any other model you prefer
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt_keyword,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5
    )
    response = response.choices[0].text.strip()
    history.append((input, response))
    return history, history
# Define the Gradio interface
with gr.Blocks() as demo:
    
    with gr.Row(visible=True) as submit_row0:
        contxt = gr.Textbox(label="Context",show_label=True, placeholder="Enter context", multiline=True).style(container=True)
    chatbot = gr.Chatbot()
    state = gr.State([])
    with gr.Box():
        with gr.Row(visible=True) as submit_row:
            txt = gr.Textbox(label="Messages",show_label=True, placeholder="Enter text and press enter").style(container=True)
        with gr.Row(visible=True) as submit_row2:
            submit_btn = gr.Button("Submit")
    
    chatstate = gr.State([])
    submit_btn.click(predict, [txt, contxt,state], [chatbot, state])
            
demo.launch()
