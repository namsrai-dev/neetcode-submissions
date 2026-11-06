class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        res = False
        l = 0
        r = len(s1) - 1
        for idx, val in enumerate(s2[:len(s2) + 1 - len(s1)]):
            print(s2[idx: idx + len(s1)])
            str1 = Counter(s2[idx: idx + len(s1)])
            str2 = Counter(s1)
            if str1 == str2:
                res = True
        return res