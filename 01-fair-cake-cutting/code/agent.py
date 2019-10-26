#!python3

"""
Defines an Agent class, that represents an agent in a cake-cutting algorithm.

AUTHOR: Erel Segal-Halevi
SINCE:  2019-10
"""

from typing import List

class Agent:
    def mark(self, x:float)->float:
        """
        :param    x: a positive number representing a location on the cake.
        :return:  v: the value of the piece [0,x] for the agent.
        """
        pass

    def eval(self, v:float)->float:
        """
        :param    v: a positive number representing a value of a piece.
        :return:  x: a number such that the value of [0,x] equals v.
        """
        pass

def cutAndChoose(a:Agent, b:Agent):
    """
    :param a, b: two agents.
    :return:  prints a fair division of the cake [0,1].

    """
    pass

def lastDiminisher(agents:List[Agent]):
    """
    :param a, b: two agents.
    :return:  prints a fair division of the cake [0,1].

    """
    pass

