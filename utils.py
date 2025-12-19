from groq import Groq
import os
from dotenv import load_dotenv
import json

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_gpt_data(state: str, district: str):
    prompt = f"""
    Provide the following information for {district}, {state}, India:
    - Dominant soil type
    - Average annual temperature (°C)
    - Average annual humidity (%)
    - Average annual rainfall (mm)

    Return the answer in pure JSON with keys: soil, temperature, humidity, rainfall.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are an Indian agriculture data expert who returns only clean JSON."},
            {"role": "user", "content": prompt}
        ]
    )

    content = response.choices[0].message.content.strip()

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        content = content[content.find("{"):content.rfind("}")+1]
        try:
            return json.loads(content)
        except:
            return {"soil": None, "temperature": None, "humidity": None, "rainfall": None}
