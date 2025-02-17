Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
class Solution:
    def isValid(self, s: str) -> bool:
        op=["(","{","["]
        cs=[")","}","]"]
        stk=[]
        for i in s:
            if i in op:
                stk.append(i)
            elif i in cs:
                pos=cs.index(i)
                if len(stk)>0 and op[pos]==stk[len(stk)-1]:
                    stk.pop()
                else:
                    return False
        return len(stk)==0

        
