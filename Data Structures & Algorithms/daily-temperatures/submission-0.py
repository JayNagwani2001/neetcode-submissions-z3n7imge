class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        st = [(temperatures[-1], l-1)]

        res = [0]*l

        for i in range(len(temperatures)-2, -1, -1):
            while st and st[-1][0] <= temperatures[i]:
                st.pop()
            
            if st:
                res[i] = st[-1][1]-i
            
            st.append((temperatures[i], i))

        return res