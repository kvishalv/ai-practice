Suggested design:

- `Node`: stores key/value and prev/next pointers
- `DoublyLinkedList`: tracks recency order
- `LRUCache`: public API and hashmap lookup

Likely implementation order:
1. Node
2. DoublyLinkedList
3. LRUCache skeleton
4. get()
5. put()
6. eviction
7. tests
