class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pop_idx = len(nums) - 1
        new_nums = nums
        while new_nums[-1] < new_nums[0]:
            popped = new_nums.pop()
            if popped == target:
                return pop_idx
            else:
                pop_idx -= 1
        
        r = 0
        l = len(new_nums) - 1
        while r >= l:
            m = (r + l) // 2
            if new_nums[m] > target:
                r = m - 1
            elif new_nums[m] < target:
                l = m + 1
            else:
                return m
        
        return -1