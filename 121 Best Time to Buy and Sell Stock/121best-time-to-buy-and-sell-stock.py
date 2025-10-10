class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0
        
        while right < len(prices):
        # profitable?
            if prices[right]>prices[left]:
                profit = prices[right]-prices[left]
                max_profit = max(max_profit,profit)
            else:
        # if price at right is smaller, move left (buy) pointer
                left=right
        # move right pointer (next day)
            right+=1
        return max_profit