def confidence_score(scores):

    def avg(x):
        return sum(x.values())/len(x)

    return {
        "KG": round(avg(scores["KG"]),3),
        "Traditional": round(avg(scores["Traditional"]),3)
    }
