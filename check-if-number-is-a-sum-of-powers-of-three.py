Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

An integer y is a power of three if there exists an integer x such that y == 3x.

 

Example 1:

Input: n = 12
Output: true
Explanation: 12 = 31 + 32
Example 2:

Input: n = 91
Output: true
Explanation: 91 = 30 + 32 + 34
Example 3:

Input: n = 21
Output: false
 

Constraints:

1 <= n <= 107



Program
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        cap=16
        arr=[0]*cap
        for i in range(cap):
            arr[i]=pow(3,i)
        for i in range(cap-1,-1,-1):
            if n>=arr[i]:
                n-=arr[i]
            if n==0:
                return True
        return False
        
