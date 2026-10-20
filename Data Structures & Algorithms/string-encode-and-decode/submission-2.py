class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        if len(strs) > 0:
            ret = strs[0]
        for i in range(1, len(strs)):
            ret += "#$5" + strs[i]

        return ret


    def decode(self, s: str) -> List[str]:
        return s.split("#$5")
