from pyvis.network import Network

def visualize(graph_data):

    net = Network(height="500px", width="100%")

    for item in graph_data:
        path = item["path"]

        for node in path.nodes:
            net.add_node(node.id, label=node["name"])

        for rel in path.relationships:
            net.add_edge(rel.start_node.id, rel.end_node.id, label=rel.type)

    net.save_graph("graph.html")
    return "graph.html"
