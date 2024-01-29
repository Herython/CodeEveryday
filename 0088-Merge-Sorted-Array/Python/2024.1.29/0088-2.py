from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sorted = []
        p1, p2 =0, 0
        while p1 < m or p2 < n:
            # if nums1[p1] < nums2[p2]:
            #     sorted.append(nums1[p1])
            #     p1 += 1
            # elif nums1[p1] > nums2[p2]:
            #     sorted.append(nums2[p2])
            #     p2 += 1
            # elif p1 == m:
            #     sorted.append(nums2[p2])
            #     p2 +=1
            # # elif p2 == n
            # else:
            #     sorted.append(nums1[p1])
            #     p1 += 1
            if p1 == m:
                sorted.append(nums2[p2])
                p2 += 1
            elif p2 == n:
                sorted.append(nums1[p1])
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                sorted.append(nums1[p1])
                p1 += 1
            else:
                sorted.append(nums2[p2])
                p2 += 1
        nums1[:] = sorted

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
solution_instance = Solution()
solution_instance.merge(nums1=nums1,m=m,nums2=nums2,n=n)