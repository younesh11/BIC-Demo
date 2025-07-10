curl -X POST http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama-3.2",
    "messages": [
      { "role": "system", "content": "You are a helpful assistant." },
      { "role": "user",   "content": "Hello, how are you today?" }
    ],
    "temperature": 0.7,
    "max_tokens": 128,
    "stream": true
  }'
