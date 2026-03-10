def pagerank(graph, damping=0.85, iters=100):
    n = len(graph)
    scores = {node: 1.0 / n for node in graph}
    for _ in range(iters):
        new_scores = {}
        for node in graph:
            rank = (1 - damping) / n
            for referrer, links in graph.items():
                if node in links: rank += damping * (scores[referrer] / len(links))
            new_scores[node] = rank
        scores = new_scores
    return scores
if __name__ == "__main__":
    print("PageRank Scores:", pagerank({'A': ['B', 'C'], 'B': ['C'], 'C': ['A']}))
