import requests

def chat_once(uner_input):
    url = "http://localhost:8080/v1/chat/completions"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": "llama3.2-1B",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user",   "content": f"""{uner_input}"""}
        ],
        "temperature": 0.7,
        "max_tokens": 128
    }

    resp = requests.post(url, headers=headers, json=payload)
    resp.raise_for_status()
    data = resp.json()
    print(data)

    assistant_reply = data["choices"][0]["message"]["content"]
    return assistant_reply


if __name__ == "__main__":
    print(chat_once("what is capital of Nepal?"))
