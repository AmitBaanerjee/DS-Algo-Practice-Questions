# Alice is playing an arcade game and wants to climb to the top of the leaderboard and wants to track her ranking. The game uses Dense Ranking, so its leaderboard works like this:
#
# The player with the highest score is ranked number 1 on the leaderboard.
# Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.
# For example, the four players on the leaderboard have high scores of 100, 90, 90, and 80. Those players will have ranks 1, 2, 2, and 3, respectively. If Alice's scores are 70,80  and 105, her rankings after each game are 4th,3rd  and 1st.
#
# Function Description
#
# Complete the climbingLeaderboard function in the editor below. It should return an integer array where each element represents Alice's rank after the jth game.
#
# climbingLeaderboard has the following parameter(s):
#
# scores: an array of integers that represent leaderboard scores
# alice: an array of integers that represent Alice's scores

#!/bin/python3

import math
import os
import random
import re
import sys
from queue import PriorityQueue
# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    q,ranking,alice_rank=PriorityQueue(),[],[]
    for s in set(scores):
        q.put((-s,s))
    while not q.empty():
        ranking.append(q.get()[1])
    length=len(ranking)
    for i in alice:
        if i<ranking[-1]:
            alice_rank.append(len(ranking)+1)
        elif i>ranking[0]:
            alice_rank.append(1)
        elif i in ranking:
            alice_rank.append(ranking.index(i)+1)
        else:
        # while (length>0) and (i>=ranking[length-1]):
        #     length=length-1
        # alice_rank.append(length+1)
            for j in range(len(ranking)-1):
                if ranking[j]>i and ranking[j+1]<i:
                    alice_rank.append(j+2)
    return alice_rank

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
