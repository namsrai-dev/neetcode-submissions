class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        if len(strs) > 0:
            ret = strs[0]
        for i in range(1, len(strs)):
            ret += "#$5" + strs[i]

        # if ret == "":
        #     ret = "#$5"
        print(ret)
        return ret


    def decode(self, s: str) -> List[str]:
        # if s == "#$5":
        #     return [""]
        return s.split("#$5")
