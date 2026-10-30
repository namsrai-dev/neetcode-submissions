class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        # arr = nums
        ret = -1
        # print(nums[l:r])
        count = 0
        while ret == -1 and r > l:
            count += 1
            idx = (r + l) // 2
            # print("idx", idx)
            if nums[idx] == target:
                ret = idx
            elif nums[idx] > target:
                # print("r changed",r, idx)
                if r == idx:
                    r = idx - 1
                else:
                    r = idx
            else:
                # print("l changed",l, idx)
                if l == idx:
                    l = idx + 1
                else:
                    l = idx

        return ret
            
