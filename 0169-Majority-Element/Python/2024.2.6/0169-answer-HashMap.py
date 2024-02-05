from typing import List
import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_map = {}  # 初始化哈希表来存储每个元素的计数
        majority_count = len(nums) // 2  # 多数元素的最小计数

        for num in nums:
            # 对每个元素进行计数
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1

            # 如果当前元素的计数超过了 majority_count，直接返回该元素
            if count_map[num] > majority_count:
                return num
        
        # 根据题目描述，假设总是存在多数元素，所以这里不需要处理找不到多数元素的情况

# 示例使用
solution = Solution()
print(solution.majorityElement([3,2,3]))  # 输出: 3
print(solution.majorityElement([2,2,1,1,1,2,2]))  # 输出: 2




#官方题解
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/majority-element/solutions/146074/duo-shu-yuan-su-by-leetcode-solution/