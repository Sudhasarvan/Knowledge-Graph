import os, json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_entities_intent(question):
    prompt = f"""
Extract:
1. Main concept
2. Intent (definition, formula, relation, explanation)

Return JSON only:
{{"concept": "...", "intent": "..."}}

Question: {question}
"""

    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return json.loads(res.choices[0].message.content)


def extract_triplets(text):
    prompt = f"""
Extract physics knowledge graph triplets.

Rules:
- Allowed relations: CAUSES, RESULTS_IN, DEFINES, HAS_FORMULA, DEPENDS_ON, MEASURED_IN
- Output ONLY:
(Concept1)-[RELATION]->(Concept2)

Text:
{text}
"""

    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return res.choices[0].message.content

def generate_kg_answer(question, reasoning):

    prompt = f"""
You are a Physics teacher.

Answer ONLY using the reasoning paths.

Rules:
- Explain step-by-step
- Use cause and effect
- Keep it simple (grade 9)
- Do NOT ignore reasoning

Question:
{question}

Reasoning Paths:
{reasoning}
"""

    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return res.choices[0].message.content

def generate_answer(question, context):
    prompt = f"""
Answer clearly for grade 9.

Question: {question}
Context: {context}
"""

    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return res.choices[0].message.content
