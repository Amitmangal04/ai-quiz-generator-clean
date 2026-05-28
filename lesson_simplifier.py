import requests

grade = input("Enter class level: ")
text = input("Your paragraph: ")

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "phi3:mini",
        "prompt": f"""
Reply ONLY in English.

You are a helpful teacher for Class {grade} students.

Read the paragraph and give output EXACTLY in this format.

Simple Summary:
(write 3 simple sentences)

Key Points:
- point 1
- point 2
- point 3

Difficult Words:
1. Gravity = force that pulls objects together
2. Celestial = related to space
3. Asteroids = small rocky objects in space

Paragraph:
{text}
""",
        "stream": False
    }
)

data = response.json()

print("\n========== RESULT ==========\n")
print(data["response"])

print("\n============================")
print("\n============================")