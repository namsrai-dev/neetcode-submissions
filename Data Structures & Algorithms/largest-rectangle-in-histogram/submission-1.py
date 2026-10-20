class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_num = 0
        for i in range(len(heights)):
            arr = [heights[i]]
            min_num = heights[i]
            max_num = max(max_num, min_num)
            for j in range(i+1, len(heights)):
                min_num = min(heights[j], min_num)
                arr.append(heights[j])
                max_num = max(max_num, min_num * len(arr))

        return max_num

