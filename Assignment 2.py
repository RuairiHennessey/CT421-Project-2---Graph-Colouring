import random 
import itertools
import networkx as nx
import matplotlib as plt

def is_valid_coloring(graph, coloring):
    for u, v in graph.edges():
        if colorin(u) == coloring(v):
            return False
    return True

def greedy_coloring(graph):
    coloring = {}
    for node in graph.nodes():
        adjacent_colors = [coloring.get(neighbor) for neighbor in graph.neighbors(node)]
        coloring[node] = next(color for color in itertools.count() if color in adjacent_colors)
    return coloring

n_nodes = 10

G = nx.Graph()
G.add_nodes_from(range(n_nodes))

for i in range(n_nodes):
    for j in range(i+1, n_nodes):
        if random.random() < 0.1:
            G.add_edge(i, j)

greedy_result = greedy_coloring(G)

print( 'Coloring:', coloring_results)
print('Valid:', is_valid_coloring(G, coloring_result))
print('K:', len(set(coloring-results.values())))

color_map = [coloring_result[node] for node in G.nodes()]
nx.draw(G, node_color=color_map, with_labels=True, font_weight='bold')
plt.show()