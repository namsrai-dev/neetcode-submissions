class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pop_idx = len(nums) - 1
        while nums[-1] < nums[0]:
            popped = nums.pop()
            if popped == target:
                return pop_idx
            else:
                pop_idx -= 1
        
        l = 0
        r = len(nums) - 1
        while r >= l:
            m = (r + l) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        
        return -1