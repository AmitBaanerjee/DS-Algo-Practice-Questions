3. Longest Substring Without Repeating Characters
Medium

6798

400

Favorite

Share
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

             class Solution {
                 public int lengthOfLongestSubstring(String s) {
                     // HashSet<Character> hs=new HashSet<Character>();
                     // int counter=0;
                     // int maxLength=Integer.MIN_VALUE;
                     // if(s.length()==0)return 0;
                     // if(s.length()==1)return 1;
                     // for (char c:s.toCharArray()){
                     //     if(!hs.contains(c)){
                     //         hs.add(c);
                     //     }
                     //     else{
                     //         hs=new HashSet<Character>();
                     //         hs.add(c);
                     //         maxLength=Math.max(counter,maxLength);
                     //         counter=0;
                     //     }
                     //     counter++;
                     // }
                     // return Math.max(counter,maxLength);
                     if(s.length()==0)return 0;
                     if(s.length()==1)return 1;
                     int left=0,right=0;
                     int answer=0;
                     int n=s.length();
                     Set<Character> hs=new HashSet<Character>();
                     while(left < n && right< n){
                         if (!hs.contains(s.charAt(right))){
                             hs.add(s.charAt(right));
                             right++;
                             answer=Math.max(answer,right-left);
                         }
                         else{
                             hs.remove(s.charAt(left));
                             left++;
                         }
                     }
                     return answer;
                 }
             }
