#!python3

"""
A demo of finding a cycle using networkx -
the graph-algorithms package of python.
"""

import networkx as nx

# Construct an empty directed graph:
G=nx.DiGraph()

# Add edges:
G.add_edge('avi','beni')
G.add_edge('beni','rami')
G.add_edge('rami','avi')


# Find cycles:
for cycle in nx.simple_cycles(G):
    print(cycle)
