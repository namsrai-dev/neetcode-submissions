class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        total_sum = 0
        for idx, i in enumerate(s):
            sum_k = 0
            for idx2, j in enumerate(s[idx+1:]):
                # print(i,j, idx, idx2)
                if i != j:
                    sum_k += 1
                if sum_k <= k:
                    total_sum = max(total_sum, idx2 - idx + 2)

        return total_sum