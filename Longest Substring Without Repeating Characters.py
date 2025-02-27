Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

Program:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = 0
        s1 = set()
        l = 0
        for r in range(len(s)):
            while s[r] in s1:
                s1.remove(s[l])
                l+=1
            s1.add(s[r])
            c=max(c,r-l+1)
        return c
