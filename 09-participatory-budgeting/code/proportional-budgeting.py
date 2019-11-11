#!python3

"""
Using networkx - the graph algorithms package of Python -
to find a room assignment maximizing the sum of values.

AUTHOR: Erel Segal-Halevi
SINCE:  2019-11
"""


from itertools import chain, combinations

def powerset(iterable):
    """
    By Martijn Pieters, from
    From https://stackoverflow.com/a/18035641/827927
    """
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))



print("\n\nThere are three tennants and three rooms.")

# Construct an empty graph:
G=nx.Graph()

# Add edges with weights:
G.add_edge('aya','martef' ,weight=25)
G.add_edge('aya','heder',weight=40)
G.add_edge('aya','salon' ,weight=35)

G.add_edge('batya','martef' ,weight=40)
G.add_edge('batya','heder',weight=60)
G.add_edge('batya','salon' ,weight=35)

G.add_edge('gila','martef' ,weight=20)
G.add_edge('gila','heder',weight=40)
G.add_edge('gila','salon' ,weight=25)

print("Maximum-value matching: ", nx.max_weight_matching(G))
