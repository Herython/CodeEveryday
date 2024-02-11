# 0189-Rotate-Array 轮转数组

**LINK:**[189. 轮转数组](https://leetcode.cn/problems/rotate-array/description/)

## 题目

### 中文

给定一个整数数组 `nums`，将数组中的元素向右轮转 `k` 个位置，其中 `k` 是非负数。

 

**示例 1:**

```
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]
```

**示例 2:**

```
输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释: 
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]
```

 

**提示：**

- `1 <= nums.length <= 105`
- `-231 <= nums[i] <= 231 - 1`
- `0 <= k <= 105`

 

**进阶：**

- 尽可能想出更多的解决方案，至少有 **三种** 不同的方法可以解决这个问题。
- 你可以使用空间复杂度为 `O(1)` 的 **原地** 算法解决这个问题吗？

### 英文

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

 

**Example 1:**

```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

**Example 2:**

```
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```

 

**Constraints:**

- `1 <= nums.length <= 105`
- `-231 <= nums[i] <= 231 - 1`
- `0 <= k <= 105`

 

**Follow up:**

- Try to come up with as many solutions as you can. There are at least **three** different ways to solve this problem.
- Could you do it in-place with `O(1)` extra space?

## 反思

### 2024.2.9

这一题做的时候思路比较清晰，用了Python的切片来旋转数组，自己的代码如下，可惜只想到这一种解法，题解中的其他方法还有待学习

```python
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]
```

#### 官方题解

**LINK:**https://leetcode.cn/problems/rotate-array/solutions/551039/xuan-zhuan-shu-zu-by-leetcode-solution-nipk

##### 方法一：使用额外数组

使用额外的数组来将每个元素放至正确的位置。

###### C++

```c++
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> newArr(n);
        for (int i = 0; i < n; ++i) {
            newArr[(i + k) % n] = nums[i];
        }
        nums.assign(newArr.begin(), newArr.end());
    }
};
```

###### Javascript

```javascript
var rotate = function(nums, k) {
    const n = nums.length;
    const newArr = new Array(n);
    for (let i = 0; i < n; ++i) {
        newArr[(i + k) % n] = nums[i];
    }
    for (let i = 0; i < n; ++i) {
        nums[i] = newArr[i];
    }
};
```

###### Python

根据题解仿写如下Python代码

```python
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        newArr = [0] * n  # 创建一个与 nums 相同大小的新列表，并初始化为 0
        for i in range(n):
            newArr[(i + k) % n] = nums[i]  # 将每个元素移动到正确的位置
        nums[:] = newArr  # 将新列表的内容复制回原列表，实现原地修改
```

##### 方法二：环状替换

```xml
nums = [1, 2, 3, 4, 5, 6]
k = 2
```

![image.png](https://pic.leetcode-cn.com/f0493a97cdb7bc46b37306ca14e555451496f9f9c21effcad8517a81a26f30d6-image.png)

###### C++

```c++
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k = k % n;
        int count = gcd(k, n);
        for (int start = 0; start < count; ++start) {
            int current = start;
            int prev = nums[start];
            do {
                int next = (current + k) % n;
                swap(nums[next], prev);
                current = next;
            } while (start != current);
        }
    }
};
```

###### Javascript

```javascript
const gcd = (x, y) => y ? gcd(y, x % y) : x;

var rotate = function(nums, k) {
    const n = nums.length;
    k = k % n;
    let count = gcd(k, n);
    for (let start = 0; start < count; ++start) {
        let current = start;
        let prev = nums[start];
        do {
            const next = (current + k) % n;
            const temp = nums[next];
            nums[next] = prev;
            prev = temp;
            current = next;
        } while (start !== current);
    }
};
```

###### Python

仿照写的Python如下

```python
from typing import List
from math import gcd  # 引入gcd函数计算最大公约数

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # 确保k不大于n
        count = gcd(k, n)  # 计算k和n的最大公约数，以确定需要遍历的环数
        
        for start in range(count):
            current = start
            prev = nums[start]
            while True:
                next_idx = (current + k) % n  # 计算下一个要替换的位置
                nums[next_idx], prev = prev, nums[next_idx]  # 交换元素
                current = next_idx  # 更新当前位置
                if start == current:  # 如果环回到起点，则结束当前环的替换
                    break
```

##### 方法三：数组翻转

**LINK:**https://leetcode.com/problems/rotate-array/discuss/54250/Easy-to-read-Java-solution

这个方法太巧妙了，下面这个解释写的很清晰

```xml
nums = "----->-->"; k =3
result = "-->----->";

reverse "----->-->" we can get "<--<-----"
reverse "<--" we can get "--><-----"
reverse "<-----" we can get "-->----->"
this visualization help me figure it out :)
```

###### C++

```c++
class Solution {
public:
    void reverse(vector<int>& nums, int start, int end) {
        while (start < end) {
            swap(nums[start], nums[end]);
            start += 1;
            end -= 1;
        }
    }

    void rotate(vector<int>& nums, int k) {
        k %= nums.size();
        reverse(nums, 0, nums.size() - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, nums.size() - 1);
    }
};
```

###### Javascript

```js
const reverse = (nums, start, end) => {
    while (start < end) {
        const temp = nums[start];
        nums[start] = nums[end];
        nums[end] = temp;
        start += 1;
        end -= 1;
    }
}

var rotate = function(nums, k) {
    k %= nums.length;
    reverse(nums, 0, nums.length - 1);
    reverse(nums, 0, k - 1);
    reverse(nums, k, nums.length - 1);
};
```

###### Python

仿照写的Python如下

```Python
from typing import List

class Solution:
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]  # 交换元素
            start, end = start + 1, end - 1  # 更新索引

    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n  # 确保k不大于数组长度

        # 翻转整个数组
        self.reverse(nums, 0, n - 1)
        # 翻转前k个元素
        self.reverse(nums, 0, k - 1)
        # 翻转剩余的元素
        self.reverse(nums, k, n - 1)
```
