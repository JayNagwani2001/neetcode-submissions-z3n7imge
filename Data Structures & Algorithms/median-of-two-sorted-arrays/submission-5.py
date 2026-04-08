class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        p1, p2 = 0, 0

        ct = 1
        n = len(nums1)
        m = len(nums2)
        l = m+n
        isEven = 1 if (m+n)%2 == 0 else 0

        if not nums2:
            if n%2 == 0:
                mid = n//2-1
                return (nums1[mid] + nums1[mid+1])/2
            else:
                mid = n//2
                return nums1[mid]

        if not nums1:
            if m%2 == 0:
                mid = m//2-1
                return (nums2[mid] + nums2[mid+1])/2
            else:
                mid = m//2
                return nums2[mid]

        while p1<len(nums1) or p2<len(nums2):
            if isEven:
                if ct == l//2:
                    print(p1, p2, ct)

                    if nums1[p1] < nums2[p2]:
                        m1 = nums1[p1]
                        if p1+1 < len(nums1):
                            m2 = min(nums1[p1+1], nums2[p2])
                        else:
                            m2 = nums2[p2]
                        return (m1+m2)/2
                    else:
                        m1 = nums2[p2]
                        if p2+1 < len(nums2):
                            m2 = min(nums1[p1], nums2[p2+1])
                        else:
                            m2 = nums1[p1]

                        # print('yes', m1, m2)
                        return (m1+m2)/2.0
            else:
                if ct == l//2 +1:
                    return min(nums1[p1], nums2[p2])

            if nums1[p1] < nums2[p2]:
                if p1 >= len(nums1)-1:
                    p2 += 1
                else:
                    p1 += 1
            else:
                if p2 >= len(nums2)-1:
                    p1 += 1
                else:
                    p2 += 1
            
            ct += 1
        
        print(p1, p2, ct)
        return -1
