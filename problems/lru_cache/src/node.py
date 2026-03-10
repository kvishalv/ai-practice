class Node:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.prev: "Node | None" = None
        self.next: "Node | None" = None
