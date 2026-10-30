class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        # arr = nums
        ret = -1
        # print(nums[l:r])
        while l < r and ret == -1:
            # print("haa", nums[len(nums[l:r]) // 2])
            if nums[len(nums[l:r]) // 2] == target:
                ret = len(nums[l:r]) // 2
            elif nums[len(nums[l:r]) // 2] > target:
                l = len(nums[l:r]) // 2
            else:
                r = len(nums[l:r]) // 2
        return ret
            
