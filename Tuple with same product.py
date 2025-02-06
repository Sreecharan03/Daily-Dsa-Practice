Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.
Example 1:

Input: nums = [2,3,4,6]
Output: 8
Explanation: There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
Example 2:

Input: nums = [1,2,4,5,10]
Output: 16
Explanation: There are 16 valid tuples:
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 104
All elements in nums are distinct.

Intuition:
The goal is to find sets of four numbers ((a, b, c, d)) where the product of two numbers equals the product of another two numbers. Since the order matters in forming tuples, we need an efficient way to track these product occurrences.

Approach
Use a hash map (Counter) to store how many times a product appears as we iterate through pairs of numbers.
Loop through all possible pairs in nums, calculating their product.
If the product has been seen before, it means we can form valid tuples. We add count[prod] * 8 to the result because each previous pair contributes 8 possible permutations.
Update the count of the current product in the hash map.
Finally, return the accumulated count.
Complexity
Time complexity: ( O(n^2) ) due to the nested loop iterating over all pairs.

Space complexity: ( O(n^2) ) for storing product frequencies in the hash map.

Code
class Solution:
  def tupleSameProduct(self, nums: list[int]) -> int:
    
    ans = 0
    count = collections.Counter()

    for i in range(len(nums)):
      for j in range(i):
        prod = nums[i] * nums[j]
        ans += count[prod] * 8
        count[prod] += 1

    return ans
