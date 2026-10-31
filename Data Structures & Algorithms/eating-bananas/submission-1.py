class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        sorted_piles = sorted(piles)
        my_arr = list(range(1, sorted_piles[-1] + 1))
        l = 0
        r = len(my_arr) - 1
        # print(my_arr)
        ret = 0
        while r >= l:
            m = (l + r) // 2
            t = 0
            for i in piles:
                t += math.ceil(i / my_arr[m])
            # print("what is t", t, m)
            if t > h:
                # print("t > h")
                l = m + 1
            else:
                # print("else", m)
                ret = my_arr[m]
                r = m - 1

        return ret