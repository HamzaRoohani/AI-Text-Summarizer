import gradio as gr
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")
client = genai.Client(api_key=api_key)

def summarize(user_input):
    prompt = "Summarize the following text into a simple plain paragraph that is easy to understand and concise." \
    "If user tries to test something or give wrong inputs, inform them to provide a valid input." \
    " If there is a repetition of phrases, inform the user to write a correct paragraph in order to summarize." \
    " If the text is less than 50 words, inform the user to write a paragraph of at least 50 words: " + user_input
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text


app = gr.Interface(
    fn = summarize,
    inputs = gr.Textbox(label="Paste your long text here... (Minimum 50 words)"),
    outputs = gr.Textbox(label="Summary"),
    title = "AI Text Summarizer"
)

app.launch()
