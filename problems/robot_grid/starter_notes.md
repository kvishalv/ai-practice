Suggested design:

- `Point`: x/y coordinate
- `Robot`: position and facing direction
- `Arena`: grid bounds, obstacles, occupancy validation
- `commands.py`: command constants or parsing helpers

Likely implementation order:
1. Point
2. Robot state transitions
3. Arena validation
4. Command execution
5. Tests
6. Multi-robot extension
