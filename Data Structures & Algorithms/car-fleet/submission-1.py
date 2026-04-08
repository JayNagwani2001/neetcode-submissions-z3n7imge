class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tup = [(position[i], speed[i]) for i in range(len(speed))]
        tup = sorted(tup, key=lambda x:x[0])
        d = {position[i]:speed[i] for i in range(len(speed))}
        time = [(target-x[0])/x[1] for x in tup]
        # .reverse()

        ans = len(time)

        for i in range(len(time)-1, 0, -1):
            if time[i-1] <= time[i]:
                time[i-1] = time[i]
                ans -= 1
            else:
                pass
        
        return ans