class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1]

        for i in nums[:len(nums) - 1]:
            ret.append(ret[len(ret) -1] * i)

        memo = 1
        for index, element in reversed(list(enumerate(nums))):
            if index != len(nums) - 1:
                # print("what is memo", memo)
                # print("ret[index]", ret[index])
                ret[index] = ret[index] * memo
            memo = memo * nums[index]


        # print("ret is",ret)
        return ret

