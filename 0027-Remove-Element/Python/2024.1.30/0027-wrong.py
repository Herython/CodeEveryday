from typing import List
##这个版本没有满足原地的要求，使用了交换
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1 = 0
        p2 = len(nums)-1

        while p1 <= p2:
            if nums[p1] == val:
                if nums[p2] == val:
                    p2 -=1
                else:
                    nums[p1], nums[p2] = nums[p2], nums[p1]
                    p2 -=1
            else:
                p1 += 1
        
        # for p1 in range(len(nums)):
        #     if nums[p1] == val and nums[p2] != val:
        #         nums[p1] = nums[p2]
        #         p2 -= 1
        #     else:
        #         p2 -= 1
        #         continue

        while len(nums) > 0 and nums[-1] == val:
            nums.pop()
        return len(nums)