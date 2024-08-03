import os
import google.generativeai as genai

genai.configure(api_key="your gemini api key")

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}


model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[]
)
def compress_to_single_line(text):
    single_line = text.replace('\n', ' ').strip()
    return single_line

def answer_anything(txt):
  response =chat_session.send_message(f"you are an indian and from west bengal,your name is srijan.you know bengali,english.Response for last three lines excluding time in {txt} in a single line and avoid any special character and answer should be bengali or english based on the language of text, but type in english letter.")
  return response.text