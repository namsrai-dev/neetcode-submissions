class TimeMap:

    def __init__(self):
       self.my_dict = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.my_dict:
            self.my_dict[key] = []
        self.my_dict[key].append([timestamp, value])
        # print("[timestamp, value]", [timestamp, value])
            
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.my_dict:
            return None
        my_arr = self.my_dict[key]
        # print("key, timestamp", key,timestamp)
        # print("self", self.my_dict)
        l = 0
        r = len(my_arr) - 1
        while l <= r:
            m = (l+r) // 2
            if my_arr[m][0] > timestamp:
                r = m - 1
            elif my_arr[m][0] < timestamp:
                l = m + 1
            else:
                return my_arr[m][1]
        if len(my_arr) > r:
            return my_arr[r][1]
        return my_arr[0][1]