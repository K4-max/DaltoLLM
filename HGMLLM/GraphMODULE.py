import networkx as nx 
import matplotlib.pyplot as plt

class GRAPH:
    def __init__(self, nodes: list):
        pass

g = nx.complete_graph(10)

nx.draw(g, node_color='#E37D5D', node_size=10000,  with_labels=True)
plt.show()