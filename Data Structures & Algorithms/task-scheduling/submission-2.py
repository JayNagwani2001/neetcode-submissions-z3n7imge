class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0]*26
        for t in tasks:
            freq[ord(t)-ord('A')] += 1
        
        arr = []
        for f in freq:
            if f>0:
                arr.append(-1*f) #for max heap 

        heapq.heapify(arr)
        time = 0
        while arr:
            print(arr)
            temp_arr = []
            for i in range(n+1):
                if arr:
                    top_freq = heapq.heappop(arr)*-1
                    top_freq -= 1
                    temp_arr.append(top_freq)
            
            for f in temp_arr:
                if f>0:
                    heapq.heappush(arr, f*-1)
            
            if arr:
                time += n+1
            else:
                time += len(temp_arr)

        return time
            





