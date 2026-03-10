# Problem: LRU Cache

Design and implement an LRU cache from scratch.

## Core requirements

- Support `get(key)` and `put(key, value)`
- Both operations should be O(1)
- Cache has fixed capacity
- When full, evict the least recently used item
- `get` returns -1 when the key is missing

## Suggested follow-ups

- configurable capacity names (small, medium, large)
- pluggable storage backend
- metrics for hit/miss counts
- configurable eviction strategies

## Practice workflow

1. Ask clarifying questions
2. Write requirements
3. Define class design
4. Create files
5. Implement one component at a time
6. Add tests early
7. Extend for follow-ups
