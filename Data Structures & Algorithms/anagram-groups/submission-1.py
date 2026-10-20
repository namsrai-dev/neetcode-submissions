class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        for i in strs:
            is_contained = False
            for idx, j in enumerate(ret):
                if self.isAnagram(i,j[0]):
                    is_contained = True
                    ret[idx].append(i)

            if is_contained == False:
                ret.append([i])

            

        return ret


    def isAnagram(self, str1: str, str2: str) -> bool:
        # print(str1, str2)
        ret = True

        if len(str1) != len(str2):
            return False

        text = str2
        for i in str1:
            if i in text:
                text = text.replace(i, "", 1)
            else:
                ret = False

        return ret

