class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = []
        res = []
        for i in range(k-1):
            window.append(nums[i])
        
        for i in nums[k-1:]:
            window.append(i)
            res.append(max(window))
            window = window[1:]
        return res

