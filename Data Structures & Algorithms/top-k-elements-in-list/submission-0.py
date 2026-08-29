class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = defaultdict(list)
        for i in nums:
            if my_dict[i]:
                my_dict[i] += 1
            else:
                my_dict[i] = 1
        my_arr = []
        for i in my_dict:
            my_arr.append([my_dict[i], i])

        my_arr.sort(reverse=True)
        ret = []
        for i in range(k):
            ret.append(my_arr[i][1])


        return ret