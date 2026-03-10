# Practical 13
# Source: IR_Question_15_April_2025_900_1100 (2).pdf, Page 14
import numpy as np

class PageRank:
    def __init__(self, graph, damping_factor=0.85, max_iterations=100, tolerance=1e-6):
        self.graph = graph
        self.damping_factor = damping_factor
        self.max_iterations = max_iterations
        self.tolerance = tolerance
        self.num_pages = len(graph)
        self.initialize_scores()

    def initialize_scores(self):
        self.scores = np.ones(self.num_pages) / self.num_pages

    def calculate_pagerank(self):
        for _ in range(self.max_iterations):
            prev_scores = np.copy(self.scores)
            for i in range(self.num_pages):
                incoming_links = [j for j in range(self.num_pages) if self.graph[j][i] == 1]
                out_counts = [len([k for k in range(self.num_pages) if self.graph[j][k] == 1]) for j in incoming_links]
                self.scores[i] = (1 - self.damping_factor) / self.num_pages + \
                                 self.damping_factor * sum(prev_scores[j] / out_counts[idx] for idx, j in enumerate(incoming_links) if out_counts[idx] > 0)
            
            if np.linalg.norm(self.scores - prev_scores) < self.tolerance:
                break
        self.normalize_scores()

    def normalize_scores(self):
        self.scores /= sum(self.scores)

# Example usage
graph = np.array([[0, 1, 1], [1, 0, 0], [1, 1, 0]])
pagerank = PageRank(graph)
pagerank.calculate_pagerank()
print("PageRank scores:", pagerank.scores)