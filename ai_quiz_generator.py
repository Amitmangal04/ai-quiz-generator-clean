import requests

prompt = input("Geography: ")

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "tinyllama",
        "prompt": f"Generate exactly 5 MCQs on {prompt} with 4 options each. Do not write explanations. Do not write 'multiple choice'. Include answer key at the end.",
        "stream": False
    }
)

data = response.json()

print(data["response"])