from problems.robot_grid.src.point import Point


DIRECTIONS = ["N", "E", "S", "W"]


class Robot:
    def __init__(self, position: Point, direction: str = "N") -> None:
        if direction not in DIRECTIONS:
            raise ValueError("invalid direction")
        self.position = position
        self.direction = direction

    def turn_left(self) -> None:
        index = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(index - 1) % len(DIRECTIONS)]

    def turn_right(self) -> None:
        index = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(index + 1) % len(DIRECTIONS)]

    def next_position(self) -> Point:
        if self.direction == "N":
            return Point(self.position.x, self.position.y + 1)
        if self.direction == "E":
            return Point(self.position.x + 1, self.position.y)
        if self.direction == "S":
            return Point(self.position.x, self.position.y - 1)
        return Point(self.position.x - 1, self.position.y)
