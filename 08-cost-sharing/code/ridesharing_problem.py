#!python3

"""
Calculate the Shapley value in the ride-sharing problem,
with a single pickup location and a fixed dropoff order.

Reference:

Chaya Levinger, Noam Hazon, Amos Azaria (2019)
[Fair Sharing: The Shapley Value for Ride-Sharing and Routing Games](https://arxiv.org/abs/1909.04713)


Programmer: Erel Segal-Halevi
Since: 2019-12
"""


import itertools, collections, powerset
from dicttools import stringify  # Install dicttools from here: https://github.com/trzemecki/dicttools

import logging
logger = logging.getLogger(__name__)

import networkx
from networkx import DiGraph
import shapley_value

def path_cost(road_graph: DiGraph, path: list)->float:
	"""
	Calculate the total cost of the given path in the given graph.

	:param road_graph:  a weighted directed graph, representing travel costs between destinations.
	:param path: a list of destinations that must be traveled in the given order.
	:return the length of traveling the path in the given order.

	>>> road_graph = DiGraph()
	>>> road_graph.add_edge("0", "a", weight=11)
	>>> road_graph.add_edge("a", "b", weight=22)
	>>> road_graph.add_edge("b", "a", weight=44)
	>>> path_length(road_graph, ["0","a","b"])
	33
	>>> path_length(road_graph, ["0","b","a"])
	77
	"""
	length = 0
	for i in range(len(path)-1):
		length += networkx.dijkstra_path_length(road_graph, path[i], path[i+1])
	return length


def sublist(the_list:list, the_set:set)->list:
	"""
	return a sub-list of the_list, where the elements are from the_set.

	>>> sublist([1,2,3,4,5], set([5,3,1]))
	[1, 3, 5]

	>>> sublist([1,2,3,4,5], set([4,2,3]))
	[2, 3, 4]
	"""
	return list([item for item in the_list if item in the_set])



def shapley_values_inefficient(road_graph:DiGraph, dropoff_order:list):
	"""
	Calculates the Shapley values for all players in an instance of the ride-sharing problem.
	NOTE: values are calculated inefficiently, by creating an instance of the generic Shapley value problem.
	This is done for demonstration purposes only.

	:param road_graph:  a weighted directed graph, representing travel costs between destinations.
	                    "0" denotes the source; all other nodes are destinations.
	:param dropoff_order: the fixed order by which the passangers should be dropped from the source.
	:return: a dict where each key is a single char representing a passanger, and each value is the player's Shapley value.

	>>> road_graph = DiGraph()
	>>> road_graph.add_edge("0", "a", weight=5)
	>>> road_graph.add_edge("0", "b", weight=9)
	>>> road_graph.add_edge("a", "b", weight=6)
	>>> road_graph.add_edge("b", "a", weight=6)
	>>> stringify(shapley_values_inefficient(road_graph, ["a", "b"]))
	'{a:3.5, b:7.5}'

	>>> stringify(shapley_values_inefficient(road_graph, ["b", "a"]))
	'{a:5.5, b:9.5}'
	"""
	all_players = list(dropoff_order)
	SOURCE = ["0"]
	map_subset_to_cost = {
		"".join(sorted(subset)): path_cost(road_graph, SOURCE+sublist(dropoff_order, subset))
		for subset in powerset.powerset(all_players)
		if len(subset)>0
	}
	map_subset_to_cost[""] = 0
	return shapley_value.shapley_values("".join(all_players), map_subset_to_cost)


if __name__ == "__main__":
    import doctest
    (failures,tests) = doctest.testmod(report=True)
    print ("{} failures, {} tests".format(failures,tests))
