class Solution:
    def evalRPN(self, tokens: List[str]) ->  int:
        st = []
        i = 0

        while i < len(tokens):

            ele = tokens[i]
            if ele in ['+', '-', '*', '/']:
                x1 = st.pop()
                x2 = st.pop()
                
                if ele == '+':
                    st.append( (x1) +  (x2))
                if ele == '-':
                    st.append( (x2) -  (x1))
                if ele == '*':
                    st.append( (x1) *  (x2))
                if ele == '/':
                    st.append(int(x2/x1))
            else:
                st.append(int(ele))
            i += 1
        
        return st[0]
