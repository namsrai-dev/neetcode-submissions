class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ret = True

        for i in board:
            if self.hasDuplicate(i):
                ret = False
        arr2 = [
            [[],[],[]],
            [[],[],[]],
            [[],[],[]]
        ]
        for i in range(len(board)):
            my_arr = []
            for j in range(len(board[0])):
                arr2[i//3][j//3].append(board[i][j])
                my_arr.append(board[j][i])
            if self.hasDuplicate(my_arr):
                ret = False


        for row in arr2:
            for col in row:
                if self.hasDuplicate(col):
                    ret = False
        return ret

    def hasDuplicate(self, i: List[str]) -> bool:
        char_list = [char for char in i if char != '.']
        return len(char_list) != len(set(char_list))
