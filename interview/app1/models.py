from django.db import models

"""
position X = n (given)
step X+1 it should be continuous i.e. 1, 2, 3,...., n

Scenario 1:
if: 
X = 5 
A = [3, 2, 1, 5, 3, 4, 2, 1]
then to make a continuous chain of positions from 1 to X i.e. 1, 2, 3, 4, 5.
we have to find the least occurance of element which completes this path chain.
Here in our case its position 4 so the least time req is 5 secs


Scenario 2:
if X = 5
A = [2, 1, 3, 5, 1, 2]
here we can't create a continuous chain from 1 to X beacuse position 4 is missing, so frog can't cross river
"""


def solution(X, A):
    if X not in A:
        return -1, "cannot jump, X: {} is not in given sequence A!".format(X)

    s_given_steps = set(A)
    s_con_steps = set([i for i in range(1, X + 1)])
    sd = s_con_steps - s_given_steps
    if len(sd) > 0:
        return -1, "cannot jump, leaves missing at position(s): {}".format(sd)

    if X in A:
        # i = A.index(X)
        d = {}
        for time_sec, leaf_position in enumerate(A):
            if leaf_position not in d and leaf_position <= X:
                d[leaf_position] = time_sec

        return max(d.values()), "jumped successfully"



