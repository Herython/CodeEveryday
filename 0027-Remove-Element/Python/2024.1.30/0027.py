from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1 = 0
        p2 = len(nums)-1

        while p1 <= p2:
            if nums[p1] == val:
                if nums[p2] == val:
                    p2 -=1
                else:
                    nums[p1] = nums[p2]
                    p2 -=1
            else:
                p1 += 1
        return p1