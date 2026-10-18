class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        change = [amount + 1] * (amount + 1)
        change[0] = 0

        for i in range(1, amount + 1):
            for j in coins:
                if i - j >= 0:
                    change[i] = min(change[i], 1 + change[i - j])

        if change[amount] != amount + 1:
            return change[amount]
        else:
            return -1