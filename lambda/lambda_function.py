import json
import requests

def lambda_handler(event, context):
    intent = event['request']['intent']
    user_query = intent['slots']['searchQuery']['value']

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer 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",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-5.1-chat",
            "messages": [
                {"role": "user", "content": user_query}
            ]
        }
    ).json()

    ai_response = response["choices"][0]["message"]["content"]

    return {
        "version": "1.0",
        "response": {
            "shouldEndSession": False,
            "outputSpeech": {
                "type": "PlainText",
                "text": ai_response
            }
        }
    }
