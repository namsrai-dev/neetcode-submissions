class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_num = 0
        for idx, p in enumerate(prices):
            for idx2, i in enumerate(prices[idx+1:]):
                if i > p:
                    max_num = max(max_num, i - p)
        return max_num