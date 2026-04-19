from neo4j_db import run_query

from neo4j_db import run_query

def get_subgraph(concept):

    query = """
    MATCH path = (c:Concept {name:$concept})-[*1..3]->(n)
    RETURN path
    ORDER BY length(path) DESC
    LIMIT 5
    """

    return run_query(query, {"concept": concept})


def get_reasoning_paths(concept):

    query = """
    MATCH path = (c:Concept {name:$concept})-[*1..3]->(n)
    RETURN path
    ORDER BY length(path) DESC
    LIMIT 5
    """

    return run_query(query, {"concept": concept})
