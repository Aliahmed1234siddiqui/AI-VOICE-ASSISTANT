
import openai



openai.api_key = "your_openai_api_key"  # Replace with your OpenAI API key

def chat_with_ai(prompt):
    """Get AI response from ChatGPT API."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

    