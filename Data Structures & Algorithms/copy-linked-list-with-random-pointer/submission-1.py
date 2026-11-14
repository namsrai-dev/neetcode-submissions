"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = temp2 = temp3 = head
        my_dict = {}
        idx = 0
        while temp:
            my_dict[temp] = [idx]
            idx += 1
            temp = temp.next

        while temp2:
            if temp2.random:
                my_dict[temp2].append(my_dict[temp2.random][0])
            else:
                my_dict[temp2].append(None)
            temp2 = temp2.next

        dummy = n = n2 = Node(0)
        my_arr = []
        while temp3:
            n.next = Node(temp3.val)
            my_arr.append(n.next)
            n = n.next
            temp3 = temp3.next
        if n2:
            n2 = n2.next
        for idx, i in enumerate(my_dict):
            # print(my_dict[i])
            if my_dict[i][1] is not None:
                n2.random = my_arr[my_dict[i][1]]
            else:
                n2.random = None
            n2 = n2.next

        return dummy.next
