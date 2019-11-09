#!python3

"""
Using scipy.linprog to find "rental harmony" - an envy-free rent division.

AUTHOR: Erel Segal-Halevi
SINCE:  2019-11
"""

from scipy.optimize import linprog

print("\nFinding rents for maximum-value matching {('salon', 'aya'), ('heder', 'batya'), ('martef', 'gila')}:")


result = linprog(  # variables: h, m, s
    [0, 0, 0], # we do not minimize anything

    # envy-freeness conditions on h, m, s:
    A_ub=[
        [-1, 0, 1],        [0, -1, 1],
        [1, 0, -1],        [1, -1, 0],
        [-1, 1, 0],        [0, 1, -1],
        ],
    b_ub=[
        -5,     10,
        25,     20,
        -20,    -5,
    ],

    # h+m+s=100
    A_eq=[
        [1,1,1]
    ],
    b_eq=[
        100
    ],
    bounds=[(0,None), (0,None), (0,None)]  # h>=0, m>=0, s>=0
    )
print(result.message)
print("Optimal value: ",result.fun)
print("Rent values: [h, m, s] = ",result.x)
print()

#
# print("\nFinding rents for another matching {('salon', 'batya'), ('heder', 'aya'), ('martef', 'gila')}")
# m, h, s = cvxpy.Variable(),cvxpy.Variable(), cvxpy.Variable()
# prob = cvxpy.Problem(
#     cvxpy.Maximize(1),
#         constraints = [m+h+s==100,
#             35-s >= 60-h, 35-s >= 40-m,  # aya
#             40-h >= 35-s, 40-h >= 25-m,  # batya
#             20-m >= 40-h, 20-m >= 25-s,  # gila
#             ]
# )
# prob.solve()
# print("status: ", prob.status)
# print("rents: martef={}, heder={}, salon={}".format(m.value,h.value,s.value))
#


import itertools


