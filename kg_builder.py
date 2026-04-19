from pypdf import PdfReader
from llm import extract_triplets
from neo4j_db import run_query
from utils import clean_text

ALLOWED = ["CAUSES","RESULTS_IN","DEFINES","HAS_FORMULA","DEPENDS_ON","MEASURED_IN"]

def load_chunks(path):
    reader = PdfReader(path)
    text = ""
    for p in reader.pages:
        text += p.extract_text()
    return [text[i:i+1000] for i in range(0,len(text),1000)]


def parse_store(triplets):

    for line in triplets.split("\n"):
        if "->" not in line:
            continue

        try:
            line = line.replace("(","").replace(")","")
            left,right = line.split("->")

            c1,rel = left.split("]-[")
            rel = rel.strip().upper()
            c2 = right.strip()

            if rel not in ALLOWED:
                continue

            c1, c2 = clean_text(c1), clean_text(c2)

            query = f"""
            MERGE (a:Concept {{name:$c1}})
            MERGE (b:Concept {{name:$c2}})
            MERGE (a)-[:{rel}]->(b)
            """

            run_query(query, {"c1":c1,"c2":c2})

        except:
            continue


def build_graph(pdf):
    chunks = load_chunks(pdf)

    for ch in chunks:
        trip = extract_triplets(ch)
        parse_store(trip)

    print("Graph Built!")
