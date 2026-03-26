import gradio as gr
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
client = genai.Client(api_key=api_key)

def summarize(user_input):
    prompt = "Summarize the following text into a simple plain paragraph that is easy to understand" + user_input
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

app = gr.Interface(
    fn = summarize,
    inputs = gr.Textbox(label="Paste your long text here..."),
    outputs = gr.Textbox(label="Summary"),
    title = "AI Text Summarizer"
)

app.launch()
