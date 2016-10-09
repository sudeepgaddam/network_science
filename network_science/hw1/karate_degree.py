import networkx as nx
import csv
import matplotlib.pyplot as plt
import scipy as sp

G = nx.Graph()

with open('zachary.txt', 'rb') as csvfile:
    karate_data = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in karate_data:
        G.add_edge(float(row[0]), float(row[1]), weight=float(row[2]))


mat = nx.adjacency_matrix(G)
print type(mat[1])

print nx.degree(G)
nx.draw_networkx(G)
plt.show()
