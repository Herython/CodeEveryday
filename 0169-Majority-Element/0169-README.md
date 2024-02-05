# 0169-Majority-Element 多数元素

**LINK:**[169. 多数元素](https://leetcode.cn/problems/majority-element/description/)

>  这一题的有几种解法还没有完全弄懂，一定要再学习学习

## 题目

### 中文

给定一个大小为 `n` 的数组 `nums` ，返回其中的多数元素。多数元素是指在数组中出现次数 **大于** `⌊ n/2 ⌋` 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

**示例 1：**

```
输入：nums = [3,2,3]
输出：3
```

**示例 2：**

```
输入：nums = [2,2,1,1,1,2,2]
输出：2
```

 

**提示：**

- `n == nums.length`
- `1 <= n <= 5 * 104`
- `-109 <= nums[i] <= 109`

 

**进阶：**尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。

### 英文

Given an array `nums` of size `n`, return *the majority element*.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

 

**Example 1:**

```
Input: nums = [3,2,3]
Output: 3
```

**Example 2:**

```
Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

 

**Constraints:**

- `n == nums.length`
- `1 <= n <= 5 * 104`
- `-109 <= nums[i] <= 109`

 

**Follow-up:** Could you solve the problem in linear time and in `O(1)` space?

## 反思

### 2024.2.6

自己用的是暴力解法，问题就在于不够高效，官方题解给出的方案很多，让我受益匪浅

**题解链接：**[169. 多数元素官方题解](https://leetcode.cn/problems/majority-element/solutions/146074/duo-shu-yuan-su-by-leetcode-solution/)

#### 哈希表 HashMap

用哈希表来快速统计每个元素出现的次数。在这之后，遍历哈希映射中的所有键值对，返回值最大的键。

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
```

#### 排序 Sort

按照单增或者单减顺序排列，多数元素就是中位数

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
```

#### 随机化 Randomize

由于一个给定的下标对应的数字很有可能是众数，随机挑选一个下标，检查它是否是众数，如果是就返回，否则继续随机挑选。

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_count = len(nums) // 2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate
```

**最后一行的讲解**

这一行代码使用了一个非常紧凑的Python语法来计算`candidate`在`nums`中出现的次数，并将其与`majority_count`进行比较。让我们一步步分解这个表达式：

```python
sum(1 for elem in nums if elem == candidate)
```

1. **列表推导式**：`for elem in nums` 部分是一个列表推导式的一部分，它遍历列表`nums`中的每个元素`elem`。

2. **条件表达式**：`if elem == candidate` 是一个条件表达式，它检查当前元素`elem`是否等于`candidate`。只有当这个条件为真时，才会考虑这个元素对总和的贡献。

3. **生成器表达式**：整个`(1 for elem in nums if elem == candidate)`实际上是一个生成器表达式，而不是列表推导式。生成器表达式与列表推导式类似，但它产生的是一个迭代器而不是列表，这意味着它在内存使用上更高效。每当`elem == candidate`为真时，这个表达式就会生成一个`1`。

4. **`sum`函数**：`sum`函数计算所有生成的`1`的总和，这实际上就是`candidate`在`nums`中出现的次数。因为每次`elem == candidate`为真，就会产生一个`1`，所有这些`1`加起来就是`candidate`的总出现次数。

所以，这一行的意思是：“计算`nums`中等于`candidate`的元素数量，如果这个数量大于`majority_count`，则返回`candidate`”。这是一个非常高效的方式来计数，因为它在单个遍历中完成了计数，而且没有创建额外的列表，只是简单地累加满足条件的次数。

#### 分治 Divide and Conquer

如果数 `a` 是数组 `nums` 的众数，如果我们将 `nums` 分成两部分，那么 `a` 必定是至少一部分的众数。

**还需要再理解一下**

> 递归思想

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def majority_element_rec(lo, hi) -> int:
            # base case; the only element in an array of size 1 is the majority
            # element.
            if lo == hi:
                return nums[lo]

            # recurse on left and right halves of this slice.
            mid = (hi - lo) // 2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid + 1, hi)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count each element and return the "winner".
            left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums) - 1)
```

#### Boyer-Moore 投票算法

如果我们把众数记为 `+1`，把其他数记为 `−1`，将它们全部加起来，显然和大于 `0`，从结果本身我们可以看出众数比其他数多。

**值得再次学习推敲**

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
```

**一个看起来更加容易理解的实现**

> 我的灵感来源很简单，就是一个简单事实：如果一个数组有大于一半的数相同，那么任意删去两个不同的数字，新数组还是会有相同的性质。 基于这个事实，就引发了类似 [参考](https://leetcode.cn/problems/majority-element/solution/javashi-pin-jiang-jie-xi-lie-majority-element-by-s/)这个回答一样的相消思想，然后就出来算法了。
>
> ```python
> class Solution {
> public:
>  int majorityElement(vector<int>& nums) {
>      int consistant=nums[0];
>      int times=1;
>      for(int i=1;i<nums.size();i++){
>          if(consistant==nums[i]) times++;
>          else{
>              if(times==0) consistant=nums[i];
>              else times--;
>          }
>      }
>      return consistant;
>  }
> };
> ```
> https://leetcode.cn/problems/majority-element/solutions/146074/duo-shu-yuan-su-by-leetcode-solution/comments/1934773



