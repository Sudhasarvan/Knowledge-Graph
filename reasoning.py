def format_paths(paths):

    results = []

    for item in paths:
        path = item["path"]
        chain = []

        for i, rel in enumerate(path.relationships):
            start = path.nodes[i]["name"]
            end = path.nodes[i+1]["name"]
            relation = rel.type

            chain.append(f"{start} → {relation} → {end}")

        if chain:
            results.append(" → ".join(chain))

    return results
