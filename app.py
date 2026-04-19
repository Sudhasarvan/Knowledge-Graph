import streamlit as st
from kg_builder import build_graph
from pdf_rag import load_pdf
from compare import compare
from metrics import evaluate
from confidence import confidence_score
from dashboard import plot_metrics
from graph_viz import visualize

st.title("🔬 Research KG-RAG System")

pdf = st.file_uploader("Upload NCERT PDF")

if pdf:
    with open("temp.pdf", "wb") as f:
        f.write(pdf.read())

    if st.button("Build KG"):
        build_graph("temp.pdf")
        load_pdf("temp.pdf")
        st.success("Ready!")

q = st.text_input("Ask question")

if st.button("Run"):

    kg_ans, trad_ans, concept, reasoning = compare(q)

    scores = evaluate(q, kg_ans, trad_ans)
    conf = confidence_score(scores)

    # KG Answer
    st.subheader("KG Answer")
    st.write(kg_ans)

    # Reasoning
    st.subheader("🔗 Reasoning Paths")
    if reasoning:
        for r in reasoning:
            st.write("➡️", r)
    else:
        st.write("No reasoning paths found")

    # Traditional Answer
    st.subheader("Traditional Answer")
    st.write(trad_ans)

    # Metrics
    st.subheader("Metrics")
    st.json(scores)

    # Confidence
    st.subheader("Confidence")
    st.json(conf)

    # Chart
    st.pyplot(plot_metrics(scores))

    # Graph visualization
    graph_data = reasoning  # or use get_reasoning_paths(concept) if needed
    html = visualize(graph_data)

    with open(html) as f:
        st.components.v1.html(f.read(), height=500)