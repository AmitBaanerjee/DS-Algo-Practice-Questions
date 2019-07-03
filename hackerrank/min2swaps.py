You are given an unordered array consisting of consecutive integers i.e. [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in ascending order.
For example, given the array, arr=[7,1,3,2,4,5,6] we perform the following steps:
i   arr                         swap (indices)
0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
5   [1, 2, 3, 4, 5, 6, 7]
It took 5 swaps to sort the array.
Function Description
Complete the function minimumSwaps in the editor below. It must return an integer representing the minimum number of swaps to sort the array.
minimumSwaps has the following parameter(s):
arr: an unordered array of integers


def minimumSwaps(arr):
    correct_array=[x+1 for x in range(len(arr))]
    given_arr_dic={}
    swapcount=0

    for i,v in enumerate(arr):
        given_arr_dic[v]=i

    for i,v in enumerate(arr):
        correct_value=correct_array[i]
        if v!=correct_value:
        #change the values in arr as you iterate and also in array dictionary so that             they are in sync
            index_correct_value=given_arr_dic[correct_value]
            arr[i],arr[index_correct_value]=arr[index_correct_value],arr[i]
            given_arr_dic[correct_value]=i
            given_arr_dic[v]=index_correct_value
            swapcount=swapcount+1
    return swapcount


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
