from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorcnt = len(nums)/2
        for i in range(len(nums)):
            cnt = 0
            for j in range(i, len(nums)):
                if nums[j] == nums[i]:
                    cnt +=1
            if cnt > majorcnt:
                return nums[i]
            
#暴力解法 耗时太长