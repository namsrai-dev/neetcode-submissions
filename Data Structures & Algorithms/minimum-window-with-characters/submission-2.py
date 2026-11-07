class Solution:
    def contains_unordered_substring(self, s1, s2):
        main_counts = Counter(s1)
        sub_counts = Counter(s2)
        return not (sub_counts - main_counts)

    def minWindow(self, s: str, t: str) -> str:
        r = 0
        l = 0
        res = ""

        print(len(s))

        while r < len(s) and l < len(s):
            
            if s[l] in t and not self.contains_unordered_substring(s[l:r+1], t):
                r += 1
            elif not self.contains_unordered_substring(s[l:r+1], t):
                l += 1

            if self.contains_unordered_substring(s[l:r+1], t):
                if res == "":
                    res = s[l:r+1]
                elif len(res) > len(s[l:r+1]):
                    res = s[l:r+1]
                l += 1
                # print("true with res", res, r, l)

        return res
            
