class Solution:
    def contains_unordered_substring(self, s1, s2):
        main_counts = Counter(s1)
        sub_counts = Counter(s2)
        return not (sub_counts - main_counts)

    def minWindow(self, s: str, t: str) -> str:
        r = 0
        l = 0
        res = ""

        while r < len(s) and l < len(s):
            if s[r] in t:
                l += 1
            else:
                r += 1

            if self.contains_unordered_substring(s[r:l], t):
                if res == "":
                    res = s[r:l]
                elif len(res) > len(s[r:l]):
                    res = s[r:l]
                r += 1
        return res
            
