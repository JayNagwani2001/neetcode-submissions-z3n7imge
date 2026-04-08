class Solution:
    def isValid(self, s: str) -> bool:

        if len(s)%2:
            return False
    
            
            
        st = []

        for c in s:
            if c in ('(', '[', '{'):
                st.append(c)
            else:
                if not st:
                    return False
                if c == '}' and st[-1] != '{':
                    return False
                if c == ']' and st[-1] != '[':
                    return False
                if c == ')' and st[-1] != '(':
                    return False
                
                st.pop(-1)

            print(st)
            # break
        if st:
            return False
        return True

        
        # st = []
        # for c in s:
        #     st.append(c)

        # while st:
        #     c1 = st.pop()

        #     if not st:
        #         return False

        #     c2 = st.pop()
        #     if c1 == ''
