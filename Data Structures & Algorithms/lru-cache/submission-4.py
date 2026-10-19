class Node:
    def __init__(self, key=0, value=0):
        self.val = value 
        self.key = key
        self.prev = None
        self.next = None
        


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_front(self, _node: Node):
        node = _node
        node.next = self.head.next 
        self.head.next = node
        node.prev = self.head
        node.next.prev = node
    
    def _remove(self, _node: Node):
        if _node:
            _node.prev.next = _node.next
            _node.next.prev = _node.prev



    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._add_front(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self._remove(self.cache[key])
            self._add_front(self.cache[key])
        else:
            if self.capacity == len(self.cache):
                self.cache.pop(self.tail.prev.key)
                self._remove(self.tail.prev)
            self.cache[key] = Node(key, value)
            self._add_front(self.cache[key])    


            
    
                
        
