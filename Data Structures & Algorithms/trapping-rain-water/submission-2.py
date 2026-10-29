class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        minV = 0
        ret = 0
        for i, num in enumerate(height):
            while stack and stack[-1][1] <= num:
                # print((min(num, stack[-1][1]) - minV) * (i - stack[-1][0] -1))
                ret += (min(num, stack[-1][1]) - minV) * (i - stack[-1][0] -1)
                # print("ret",ret)
                # print("minV, stack", minV, stack)
                popped = stack.pop()
                minV = popped[1]
            minV = 0
            stack.append([i, num])

        return ret
