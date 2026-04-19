from sentence_transformers import SentenceTransformer
import faiss, numpy as np
from pypdf import PdfReader

model = SentenceTransformer('all-MiniLM-L6-v2')

chunks = []
index = None

def load_pdf(path):
    global chunks, index

    reader = PdfReader(path)
    text = ""

    for p in reader.pages:
        text += p.extract_text()

    chunks = [text[i:i+500] for i in range(0,len(text),500)]
    emb = model.encode(chunks)

    index = faiss.IndexFlatL2(emb.shape[1])
    index.add(np.array(emb))


def search_pdf(q):
    vec = model.encode([q])
    D,I = index.search(vec,3)
    return [chunks[i] for i in I[0]]
