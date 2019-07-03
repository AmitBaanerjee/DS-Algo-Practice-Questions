There are a number of people who will be attending ACM-ICPC World Finals. Each of them may be well versed in a number of topics. Given a list of topics known by each attendee, you must determine the maximum number of topics a 2-person team can know. Also find out how many ways a team can be formed to know that many topics. Lists will be in the form of bit strings, where each string represents an attendee and each position in that string represents a field of knowledge, 1 if its a known field or 0 if not.
For example, given three attendees' data as follows:
10101
11110
00010
These are all possible teams that can be formed:
Members Subjects
(1,2)   [1,2,3,4,5]
(1,3)   [1,3,4,5]
(2,3)   [1,2,3,4]
In this case, the first team will know all 5 subjects. They are the only team that can be created knowing that many subjects.
Function Description
Complete the acmTeam function in the editor below. It should return an integer array with two elements: the maximum number of topics any team can know and the number of teams that can be formed that know that maximum number of topics.
acmTeam has the following parameter(s):
topic: a string of binary digits

import math
import os
import random
import re
import sys

def acmTeam(topic):
    count=[]
    for i in range(len(topic)):
        for j in range(i+1,len(topic)):
            topic1=int(topic[i],2)
            topic2=int(topic[j],2)
            binary_result="{0:b}".format(topic1|topic2)
            one_count=binary_result.count("1")
            count.append(one_count)
    return max(count),count.count(max(count))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
