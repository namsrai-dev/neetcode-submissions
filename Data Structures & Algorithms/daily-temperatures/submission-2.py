class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = []
        for i in range(len(temperatures)):
            my_num = 0
            for j in range(i+1, len(temperatures)):
                if my_num == 0 and temperatures[j] > temperatures[i]:
                    my_num = j - i
            ret.append(my_num)

        return ret