

import os

from dotenv import load_dotenv
from mistralai.client import Mistral


SYSTEM_PROMPT = """
You are a friendly, patient, and supportive study assistant. Your role is to help the student understand concepts, complete assignments, and build confidence.

Explain ideas clearly and simply, using step-by-step reasoning and examples when helpful. Adjust your explanations to the student’s level and avoid unnecessary jargon. If the student seems confused, rephrase the explanation in a different way and check their understanding.

Encourage the student without being judgmental. Celebrate progress, acknowledge effort, and treat mistakes as normal parts of learning. Do not simply give answers when guiding the student would help them learn; use hints, guiding questions, and explanations first. However, provide a direct answer when the student clearly asks for one or when it is appropriate.

Ask clarifying questions when the request is unclear. Organize longer explanations with headings, bullet points, or numbered steps. Be concise for simple questions and more detailed for difficult topics.

Always be honest about uncertainty. Never invent facts, sources, or results. Help the student develop independent problem-solving and study skills.
"""

# Assistant settings
MODEL = "ministral-8b-2512"
TEMPERATURE = 0.3
#MAX_TOKENS = 500

load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY", "").strip()

if not api_key:
    raise ValueError("La clé API Mistral est absente du fichier .env.")

client = Mistral(api_key=api_key)
messages = [{"role": "system", "content": SYSTEM_PROMPT}]

question = input("Que voulez-vous demander à l'assistant ? ")
while question.strip().lower() not in ("quit", "exit", "stop"):
    if not question.strip():
        print("Veuillez entrer une question.")
        question = input("\nQue voulez-vous demander à l'assistant ? ")
        continue

    messages.append({"role": "user", "content": question})

    try:
        response = client.chat.complete(
            model=MODEL,
            messages=messages,
            temperature=TEMPERATURE,
            #max_tokens=MAX_TOKENS,
        )
    except Exception as e:
        print(f"Erreur lors de l'appel à l'API Mistral : {e}")
        break

    answer = response.choices[0].message.content
    messages.append({"role": "assistant", "content": answer})
    print(response.choices[0].message.content)
    question = input("\nQue voulez-vous demander à l'assistant ? ")


