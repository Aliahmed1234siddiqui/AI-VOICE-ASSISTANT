import requests

def chat_with_gemini(prompt):
    """Send a message to Gemini 2.0 Flash via Google's REST API and return the response."""
    API_KEY = "AIzaSyDrhABJahsrzNg7rmlHmVwpfYf9KvbsgZs"
    endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

    headers = {
        "Content-Type": "application/json",
    }

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    response = requests.post(endpoint, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        return result["candidates"][0]["content"]["parts"][0]["text"]
    else:
        raise Exception(f"Gemini API call failed: {response.status_code} {response.text}")
