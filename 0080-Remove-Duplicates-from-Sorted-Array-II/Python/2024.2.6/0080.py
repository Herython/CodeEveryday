from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0
        for p2 in range(len(nums)):
            if p1 < 2 or nums[p2] != nums[p1-2] :
                nums[p1] = nums[p2]
                p1 +=1
        return p1