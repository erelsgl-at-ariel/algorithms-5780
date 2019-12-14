#!python3

"""
Demo of Shapley value calculation.

Programmer: Erel Segal-Halevi
Since: 2019-12
"""

import itertools, collections, networkx
from dicttools import stringify  # Install dicttools from here: https://github.com/trzemecki/dicttools

import logging
logger = logging.getLogger(__name__)

import shapley_value
import logging, sys
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.INFO)


print("\n## Ride-sharing example")
map_subset_to_cost = {
	"":	   0,
	"a":   5,
	"b":   9,
	"ab":  11,
}
sv = shapley_value.shapley_values("ab", map_subset_to_cost)
for player,value in sv.items():
	print("Shapley value of {} is {}".format(player, value))


print("\n## Airport problem example")
map_subset_to_cost = {
	"":	   0,
	"a":   3,
	"b":   23,
	"c":   123,
	"ab":  23,
	"ac":  123,
	"bc":  123,
	"abc": 123,
}
sv = shapley_value.shapley_values("abc", map_subset_to_cost)
for player in sorted(sv.keys()):
	print("Shapley value of {} is {}".format(player, sv[player]))


print("\n## Ride-sharing example using a graph")

roads = networkx.DiGraph()
roads.add_edge("0","a", weight=5)
roads.add_edge("0","b", weight=9)
roads.add_edge("a","b", weight=6)
print(roads.edges(data=True))
print(networkx.dijkstra_path_length(roads, "0","a"))
