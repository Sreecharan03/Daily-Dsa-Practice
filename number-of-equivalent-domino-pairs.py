Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 

Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1
Example 2:

Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
Output: 3
 

Constraints:

1 <= dominoes.length <= 4 * 104
dominoes[i].length == 2
1 <= dominoes[i][j] <= 9

My solution:
We have Permutations and Combinations.
Permutation (order matters):
a, b, c: ab, ba, ac, ca, bc, cb
Combinations (order does not matter):
a, b, c: ab, bc, ac
This problem is a Combinations problem
Formula for Combinations:
C(n,r) = n!/( r! (n - r)! )
Simplifying for r = 2:
C(n, 2) = n*(n-1)/2

Code:
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        num_dic=collections.defaultdict(int)
        n=len(dominoes)
        for i in range(n):
            a,b=sorted(dominoes[i])
            num_dic[(a,b)]+=1
        pairs=0
        for k,v in num_dic.items():
            # formula of comtinational number, C(2, n) = n(n-1)/2. For example, item a, b, c could form three combinations of two: (a, b), (a, c), (b, c)
            if v>=2:
                pairs+=(v*(v-1))//2
        return pairs

TC: O(n)

