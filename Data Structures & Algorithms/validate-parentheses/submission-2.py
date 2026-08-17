class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        ret = True
        arr = []

        for i in s:
            if i in ["(", "{", "["]:
                arr.append(i)
            else:
                l = len(arr)
                # print(arr[l-1], my_dict[i])
                if l > 0 and arr[l-1] == my_dict[i]:
                    arr.pop()
                else:
                    ret = False

        if len(arr) != 0:
            ret = False

        return ret