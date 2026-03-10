from problems.lru_cache.src.node import Node


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_front(self, node: Node) -> None:
        first = self.head.next
        node.prev = self.head
        node.next = first
        self.head.next = node
        if first:
            first.prev = node

    def remove(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next
        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node

    def remove_lru(self) -> Node | None:
        if self.tail.prev is self.head:
            return None
        lru = self.tail.prev
        assert lru is not None
        self.remove(lru)
        return lru
