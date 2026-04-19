from llm import generate_answer, generate_kg_answer, extract_entities_intent
from kg_retriever import get_reasoning_paths
from pdf_rag import search_pdf
from reasoning import format_paths

def compare(question):

    info = extract_entities_intent(question)
    concept = info["concept"].capitalize()

    # KG reasoning
    paths = get_reasoning_paths(concept)
    formatted_paths = format_paths(paths)

    kg_ans = generate_kg_answer(question, formatted_paths)

    # Traditional RAG
    pdf_data = search_pdf(question)
    trad_ans = generate_answer(question, pdf_data)

    return kg_ans, trad_ans, concept, formatted_paths
