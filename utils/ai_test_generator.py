import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_test_cases(page_description):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system", "content": "You are a QA engineer."},
            {
                "role": "user", "content": f"Generate test cases for: {page_description}"
            }
        ]
    )

    return response.choices[0].message.content
