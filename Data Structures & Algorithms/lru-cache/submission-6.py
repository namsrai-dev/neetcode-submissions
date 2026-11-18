class ListNode:
    def __init__(self, k, v):
        self.prev = self.next = None
        self.key = k
        self.val = v

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.my_dict = {}
        self.left = ListNode(0,0)
        self.right = ListNode(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        del self.my_dict[node.key]
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        

    def insert(self, node):
        l_n = self.left.next
        node.next = l_n
        l_n.prev = node
        self.left.next = node
        node.prev = self.left

    def get(self, key: int) -> int:
        if key in self.my_dict:
            node = self.my_dict[key]
            self.remove(node)
            self.my_dict[key] = node
            self.insert(node)
            return node.val  


        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.my_dict:
            self.remove(self.my_dict[key])

        if len(self.my_dict) == self.capacity:
            self.remove(self.right.prev)

        new_node = ListNode(key, value)
        self.my_dict[key] = new_node
        self.insert(new_node)
