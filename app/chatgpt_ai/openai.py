from dotenv import load_dotenv
import openai
import os
from app.util.util import cleanup_response_turbo, calculate_score_turbo


load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

def chatgpt_response_3_5_turbo(prompt):
    cleanup_response = cleanup_response_turbo(prompt)
    master_response = calculate_score_turbo(cleanup_response)
    return cleanup_response
