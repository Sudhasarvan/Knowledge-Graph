import matplotlib.pyplot as plt

def plot_metrics(scores):

    labels = ["Cosine","BLEU","ROUGE"]

    kg = list(scores["KG"].values())
    tr = list(scores["Traditional"].values())

    x = range(len(labels))

    plt.figure()
    plt.bar(x, kg, width=0.4, label="KG")
    plt.bar([i+0.4 for i in x], tr, width=0.4, label="Traditional")

    plt.xticks([i+0.2 for i in x], labels)
    plt.legend()

    return plt
