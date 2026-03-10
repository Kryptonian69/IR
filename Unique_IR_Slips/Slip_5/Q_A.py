# Practical 5
# Source: IR_Question_15_April_2025_900_1100 (2).pdf, Page 5
def pagerank(graph, damping=0.85, iters=100):
    n = len(graph)
    scores = {node: 1.0 / n for node in graph}
    for _ in range(iters):
        new_scores = {}
        for node in graph:
            rank = (1 - damping) / n
            for r, links in graph.items():
                if node in links: rank += damping * (scores[r] / len(links))
            new_scores[node] = rank
        scores = new_scores
    return scores
if __name__ == "__main__":
    res = pagerank({'A': ['B', 'C', 'and', 'D'], 'B': ['C', 'and', 'E'], 'C': ['A', 'and', 'D']})
    for site, score in sorted(res.items(), key=lambda x: x[1], reverse=True):
        print(f"{site}: {score:.4f}")
