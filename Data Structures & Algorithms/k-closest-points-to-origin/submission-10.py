import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = {}
        i = 0
        for x, y in points:
            d = (x**2 + y**2)**0.5
            if d in distances:
                distances[d].append(i)
            else:
                distances[d] = [i]
            i += 1
        
        dist = list(distances.keys())
        heapq.heapify(dist)

        ans = []
        print(dist)
        print(distances)
        for _ in range(k):
            #get min distance
            # print(ans)
            min_dist = heapq.heappop(dist)
            # if len(distances[min_dist]) > 1:
            for ind in distances[min_dist]:
                ans.append(points[ind])
                if len(ans) == k:
                    return ans
            # else:
            #     ans.append(points[distances[min_dist][0]])

        return ans[:k]


        # {index: distance}
