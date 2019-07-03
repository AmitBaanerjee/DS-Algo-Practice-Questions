It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! There are a number of people queued up, and each person wears a sticker indicating their initial position in the queue. Initial positions increment by 1 from 1 at the front of the line to n at the back.
Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap positions, they still wear the same sticker denoting their original places in line. One person can bribe at most two others. For example, if n=8 and Person 5 bribes Person 4, the queue will look like this: 1,2,3,5,4,6,7,8.
Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get the queue into its current state!
Function Description
Complete the function minimumBribes in the editor below. It must print an integer representing the minimum number of bribes necessary, or Too chaotic if the line configuration is not possible.
minimumBribes has the following parameter(s):
q: an array of integers
Input Format
The first line contains an integer t, the number of test cases.
Each of the next t pairs of lines are as follows: 
- The first line contains an integer t, the number of people in the queue
- The second line has n space-separated integers describing the final state of the queue.


def minimumBribes(q):
    def checkswaps(q):
        swaps=0
        swapped="false"
        for x in range(0,len(q)):
            if q[x]-(x+1) > 2:
                return "Too chaotic"
        for i in range(0,len(q)-1):
            for j in range(len(q)-i-1):
                if q[j]>q[j+1]:
                    q[j],q[j+1]=q[j+1],q[j]
                    swaps=swaps+1
                    swapped="true"
            if swapped=="true":
                swapped="false"
            else:
                break
        return swaps
    print(checkswaps(q))
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
