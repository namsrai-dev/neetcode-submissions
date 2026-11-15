class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = []
        for i in nums:
            if i in s:
                return i
            else:
                s.append(i)
        return 0
        