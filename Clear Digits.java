
Program:

class Solution {
    public String clearDigits(String s) {
        Stack<Character> st=new Stack<>();
        for(char ch: s.toCharArray())
        {
            if(Character.isDigit(ch)&&!st.isEmpty())
            {
                st.pop();
            }
            else
            {
                st.push(ch);
            }
        }
        StringBuilder res=new StringBuilder();
        while(!st.isEmpty())
        {
            res.append(st.pop());
        }
        return res.reverse().toString();
        
    }
}
