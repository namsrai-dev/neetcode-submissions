class Solution:
        def maxProfit(self, prices: List[int]) -> int:
            l = 0
            r = 1
            max_num = 0
            while r < len(prices):
                if prices[r] < prices[l]:
                    l = r
                else:
                    prof = prices[r] - prices[l]
                    max_num = max(max_num, prof)
                r += 1

            return max_num
