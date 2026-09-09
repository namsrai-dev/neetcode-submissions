class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        new_position = []
        fleet = 1
        for i in range(len(position)):
            new_position.append([position[i], speed[i]])
        new_position.sort(key=lambda x: x[0], reverse=True)
        prev_time = 0
        for idx, i in enumerate(new_position):
            if idx == 0:
                prev_time = (target - i[0]) / i[1]
            else:
                curr_time = (target - i[0]) / i[1]
                if curr_time > prev_time:
                    fleet+= 1
                    prev_time = curr_time

        return fleet