class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1 #left and right pointers for sliding window
        max = 0

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
                r += 1
                continue

            profit = prices[r] - prices[l]
            if profit > max:
                max = profit

            r += 1 # extend window by 1

        return max