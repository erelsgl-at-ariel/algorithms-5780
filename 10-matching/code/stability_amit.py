# Programmer: Amit Eliyahu
# Since:      2020-01

from typing import List, Tuple


def is_stable_match(match: List[Tuple[int, int]], pref_a: List[List[int]], pref_b: List[List[int]]) -> bool:
    """

    @param match: A match which each match is represented by: (index, match[index]), where index is a player from
    group A, and match[index] is a player from group B
    @param pref_a: preferences for each players in the group A, the value that player i (from group A) give to player j
    (in group B) is pref_a[i][j], where 1 <= value <= m
    @param pref_b: preferences for each players in the group A, the value that player i (from group B) give to player j
    (in group A) is pref_b[i][j], where 1 <= value <= m
    for each players in the group B
    @return: True if the match is stable, False otherwise

    @note: In the future we can make this function a bit nicer
    (e.g implement an agent class that would make reading this function and using it a bit easier
    and/or implement a match class that can find the match for an agent [in any group] faster then O(n) time as we did
    here (O(1) time is pretty easy using a dictionary, but O(n) space],
    thus improving time Complexity [over space of course].
    Currently the algorithm's Complexity is: O(n^3) time, O(1) space
            and easily can be changed to: O(n^2) time, O(n) space

    >>> # Example in class where: Tomer = 0, Shlomo = 1, Raphi = 2
    >>> #                        Aviva = 0, Batya = 1, Galia = 2
    >>> is_stable_match([(0, 2), (1, 1), (2, 0)], [[1, 3, 2], [3, 2, 1], [3, 1, 2]], [[1, 2, 3], [1, 3, 2],[2, 3, 1]])
    True
    >>> # Example in class where: s1 = 0, s2 = 1
    >>> #                        c1 = 0, c2 = 1
    >>> # Both students prefer class 1 over class 2
    >>> # Both classes prefer student 1 over student 2
    >>> # [(s1 - c2), (s2 - c1)] is not stable (as we saw in class)
    >>> is_stable_match([(0, 1), (1, 0)], [[2, 1], [2, 1]], [[2, 1], [2, 1]])
    False
    >>> # [(s1 - c2), (s2 - c1)] is stable (as we saw in class)
    >>> is_stable_match([(1, 1), (0, 0)], [[2, 1], [2, 1]], [[2, 1], [2, 1]])
    True

    """

    for i in range(len(pref_b)):  # for each player in group A
        for j in range(len(pref_b)):  # for each player in group A
            if (i, j) not in match:  # if they are not matched, then we need to check if they are unstable couple
                match_i = [match for match in match if match[0] == i][0][1]  # the match for i
                match_j = [match for match in match if match[1] == j][0][0]  # the match for j
                # if i prefers j over what he matched with and j prefers i over what he match with,they are an unstable
                # couple, thus the match is not stable
                if pref_a[i][j] > pref_a[i][match_i] and pref_b[j][i] > pref_b[j][match_j]:
                    return False
    # If all pairs are not unstable couple, then the match is stable
    return True


print(is_stable_match(
    [(0, 0), (1, 1), (2, 2)],
    [[33, 22, 11], [33, 11, 22], [11, 33, 22]],
    [[22, 33, 11], [33, 22, 11], [11, 22, 33]]))
