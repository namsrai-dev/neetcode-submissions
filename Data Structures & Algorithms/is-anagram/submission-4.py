class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ret = True
        text = t
        for i in s:
            if i in text:
                text = text.replace(i, "", 1)
                # print("text", text)

            else:
                ret = False

        if text != "":
            ret = False

        return ret