// Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
//
// You may return any answer array that satisfies this condition.
//
// Example 1:
//
// Input: [3,1,2,4]
// Output: [2,4,3,1]
// The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

class Solution {
    public int[] sortArrayByParity(int[] input) {
        List<Integer> odd= new ArrayList<Integer>();
        List<Integer> even=new ArrayList<Integer>();
        for(int i=0; i <input.length; i++){
            if(input[i]%2==0){
                even.add(input[i]);
            }
            else{
                odd.add(input[i]);
            }
        }
        even.addAll(odd);
        int[] result=even.stream().mapToInt(i -> i).toArray();
        return result;
    }
}

/*
Alternative approach:-
class Solution {
    public int[] sortArrayByParity(int[] A) {
        int i = 0, j = A.length - 1;
        while (i < j) {
            if (A[i] % 2 > A[j] % 2) {
                int tmp = A[i];
                A[i] = A[j];
                A[j] = tmp;
            }

            if (A[i] % 2 == 0) i++;
            if (A[j] % 2 == 1) j--;
        }

        return A;
    }
}
*/
