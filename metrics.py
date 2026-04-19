from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.translate.bleu_score import sentence_bleu
from rouge_score import rouge_scorer

def evaluate(q, kg, trad):

    vect = TfidfVectorizer()
    vecs = vect.fit_transform([q,kg,trad])

    sim_kg = cosine_similarity(vecs[0:1],vecs[1:2])[0][0]
    sim_trad = cosine_similarity(vecs[0:1],vecs[2:3])[0][0]

    bleu_kg = sentence_bleu([q.split()], kg.split())
    bleu_trad = sentence_bleu([q.split()], trad.split())

    scorer = rouge_scorer.RougeScorer(['rouge1'], use_stemmer=True)

    rouge_kg = scorer.score(q,kg)['rouge1'].fmeasure
    rouge_trad = scorer.score(q,trad)['rouge1'].fmeasure

    return {
        "KG":{"cosine":sim_kg,"bleu":bleu_kg,"rouge":rouge_kg},
        "Traditional":{"cosine":sim_trad,"bleu":bleu_trad,"rouge":rouge_trad}
    }
