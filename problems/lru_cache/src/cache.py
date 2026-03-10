from problems.lru_cache.src.linked_list import DoublyLinkedList
from problems.lru_cache.src.node import Node


class LRUCache:
    def __init__(self, capacity: int) -> None:
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.capacity = capacity
        self.nodes: dict[int, Node] = {}
        self.order = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        node = self.nodes[key]
        self.order.remove(node)
        self.order.add_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            node.value = value
            self.order.remove(node)
            self.order.add_to_front(node)
            return

        if len(self.nodes) >= self.capacity:
            lru = self.order.remove_lru()
            if lru is not None:
                del self.nodes[lru.key]

        new_node = Node(key, value)
        self.nodes[key] = new_node
        self.order.add_to_front(new_node)
