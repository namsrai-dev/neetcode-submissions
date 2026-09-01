class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        if len(nums) == 0:
            return 0    

        prev = nums[0]
        max_count = 1
        count = 1
        for i in range(1, len(nums)):
            if prev == nums[i] - 1:
                count += 1
            else:
                count = 1
            prev = nums[i]
            max_count = max(max_count, count)
        return max_count
