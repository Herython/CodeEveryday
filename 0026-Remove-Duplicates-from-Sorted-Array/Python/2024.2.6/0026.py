from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0
        p2 = 1
        
        while p2 <len(nums):
            if nums[p2] != nums[p1]:
                p1 +=1
                nums[p1] = nums[p2]
            p2 +=1
        return p1+1

        # while p1 < len(nums):
        #     p2 = p1 + 1
        #     tmp = p1
        #     while nums[p2] == nums[p1]:
        #         p2 +=1
        #     while p2 >= tmp :
        #         tmp +=1
        #         nums[tmp] = nums[p2]
        #     p1 +=1
        # return p1