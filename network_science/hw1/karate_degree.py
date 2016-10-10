import networkx as nx
import csv
import matplotlib.pyplot as plt
from  eigen_centrality import *
import scipy as sp

G = nx.Graph()

with open('zachary.txt', 'rb') as csvfile:
    karate_data = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in karate_data:
        G.add_edge(int(row[0]), int(row[1]), weight=float(row[2]))


degrees = nx.degree(G)
print("Degrees: ")
for node in degrees:
    print('%s %0.2f' % (node, degrees[node]))

centrality = eig_centrality(G)
print("Eigen Vector Centrality: ")
for node in centrality:
    print('%s %0.2f ' % (node, centrality[node]))



nx.draw_networkx(G,node_size=[v*1000 for v in centrality.values()],node_color='b')
plt.show()
plt.savefig("centrality.jpg")

nx.draw_networkx(G,node_size=[v*100 for v in degrees.values()],node_color='r')
plt.show()
plt.savefig("degrees.jpg")