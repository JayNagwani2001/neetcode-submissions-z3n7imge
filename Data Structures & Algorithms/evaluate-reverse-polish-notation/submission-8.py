class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        i = 0
        if len(tokens) == 1:
            return int(tokens[0])
        while i < len(tokens):

            ele = tokens[i]
            print(st)
            if ele in ['+', '-', '*', '/']:
                x1 = st.pop()
                x2 = st.pop()
                
                if ele == '+':
                    st.append(int(x1) + int(x2))
                if ele == '-':
                    st.append(int(x2) - int(x1))
                if ele == '*':
                    st.append(int(x1) * int(x2))
                if ele == '/':
                    st.append(int(int(x2)/int(x1)))
            else:
                st.append(ele)
            i += 1
        print(st)
        
        return st[0]
