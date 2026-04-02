from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.table = OrderedDict() 
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.table:
            return -1
        # move to most recent (end) since we are accessing now 
        self.table.move_to_end(key)
        return self.table[key]

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            self.table.move_to_end(key)
        self.table[key] = value

        if len(self.table) > self.capacity:
            self.table.popitem(last=False)

    """
    OrderdDict is a dict but it remembers WHEN keys were inserted 
    Instead of doing a random order. So its perfect here

    we keep track of capacity, size of ordered dict, pop when needed if we exceed

    """
        
