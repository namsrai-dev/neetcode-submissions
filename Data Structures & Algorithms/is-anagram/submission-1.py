class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ret = True
        for i in s:
            if i in t:
                t.replace(i, "")

            else:
                ret = False

        return ret