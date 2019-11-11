#!python3

"""
Using cvxpy to find "rental harmony" - an envy-free rent division.

AUTHOR: Erel Segal-Halevi
SINCE:  2019-11
"""

import cvxpy


print("\nFinding rents for maximum-value matching {('salon', 'aya'), ('heder', 'batya'), ('martef', 'gila')}:")

m, h, s = cvxpy.Variable(),cvxpy.Variable(), cvxpy.Variable()
prob = cvxpy.Problem(
    # cvxpy.Minimize(0),
    cvxpy.Maximize(m+h+s),
    constraints = [#m+h+s==100,
            m >= 0, h >= 0, s >= 0,
            35-s >= 40-h, 35-s >= 25-m,  # aya
            60-h >= 35-s, 60-h >= 40-m,  # batya
            20-m >= 40-h, 20-m >= 25-s,  # gila
            ]
)
prob.solve()
print("status: ", prob.status)
print("optimal value: ", prob.value)
print("rents: heder={}, martef={}, salon={}".format(h.value,m.value,s.value))

print("\nFinding rents for another matching {('salon', 'batya'), ('heder', 'aya'), ('martef', 'gila')}")
m, h, s = cvxpy.Variable(),cvxpy.Variable(), cvxpy.Variable()
prob = cvxpy.Problem(
    cvxpy.Minimize(0),
    constraints = [m+h+s==100,
            40-h >= 35-s, 40-h >= 25-m,  # aya
            35-s >= 60-h, 35-s >= 40-m,  # batya
            20-m >= 40-h, 20-m >= 25-s,  # gila
            ]
)
prob.solve()
print("status: ", prob.status)
print("optimal value: ", prob.value)
print("rents: heder={}, martef={}, salon={}".format(h.value,m.value,s.value))
