from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j
    
# nums = [3,2,2,3]
nums = [0,1,2,2,3,3,0,4,2]
val = 3
solution_instance = Solution()
ret = solution_instance.removeElement(nums,val)
print(f"nums = {nums}, ret = {ret}")