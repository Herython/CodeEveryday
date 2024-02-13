# 0121-Best-Time-to-Buy-and-Sell-Stock 买卖股票的最佳时机

**LINK:**[121. 买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/description)

## 题目

### 中文

给定一个数组 `prices` ，它的第 `i` 个元素 `prices[i]` 表示一支给定股票第 `i` 天的价格。

你只能选择 **某一天** 买入这只股票，并选择在 **未来的某一个不同的日子** 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 `0` 。

 

**示例 1：**

```
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
```

**示例 2：**

```
输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
```

 

**提示：**

- `1 <= prices.length <= 105`
- `0 <= prices[i] <= 104`

### 英文

You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return *the maximum profit you can achieve from this transaction*. If you cannot achieve any profit, return `0`.

 

**Example 1:**

```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

**Example 2:**

```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

 

**Constraints:**

- `1 <= prices.length <= 105`
- `0 <= prices[i] <= 104`

## 反思

### 2024.2.13

自己的解法

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for p1 in range(len(prices)):
            for p2 in range(p1+1, len(prices)):
                profit = prices[p2] - prices[p1]
                if profit > max_profit:
                    max_profit = profit
        return max_profit
```

时间复杂度为`O(n^2)`，对于较大的数据集没有办法高效的处理，需要优化

以下是GPT优化后的算法

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  # 初始化最低价格为无穷大
        max_profit = 0  # 初始化最大利润为0

        for price in prices:
            if price < min_price:
                min_price = price  # 更新最低价格
            elif price - min_price > max_profit:
                max_profit = price - min_price  # 更新最大利润

        return max_profit
```

优化后的方法旨在减少原来我的方法中对于每一个买入价格都检查所有后续的卖出价格的重复检查。

具体思路如下：

1. **跟踪最低价格**：在遍历过程中，始终保持迄今为止遇到的最低买入价格。这意味着，随着遍历的进行，可以知道在任何给定点，如果在之前的某个时间点买入，那么买入的价格是多少。
2. **计算当前利润**：对于每个价格，计算如果在迄今为止的最低价格买入，并在当前价格卖出，能获得的利润。这就是`price - min_price`，其中`price`是当前价格，`min_price`是迄今为止的最低价格。
3. **更新最大利润**：如果当前的利润（即当前价格减去迄今为止的最低价格）大于之前记录的最大利润，就更新最大利润。这样，就始终保持了迄今为止可能的最大利润。
4. **只遍历一次**：通过上述方法，我们只需要遍历一遍价格数组，就可以找到最大利润，无需嵌套循环。