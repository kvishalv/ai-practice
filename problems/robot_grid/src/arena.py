from problems.robot_grid.src.point import Point
from problems.robot_grid.src.robot import Robot


class Arena:
    def __init__(self, width: int, height: int, obstacles: set[Point] | None = None) -> None:
        self.width = width
        self.height = height
        self.obstacles = obstacles or set()

    def is_in_bounds(self, point: Point) -> bool:
        return 0 <= point.x < self.width and 0 <= point.y < self.height

    def is_blocked(self, point: Point) -> bool:
        return point in self.obstacles

    def can_move_to(self, point: Point) -> bool:
        return self.is_in_bounds(point) and not self.is_blocked(point)

    def move_robot(self, robot: Robot) -> bool:
        candidate = robot.next_position()
        if not self.can_move_to(candidate):
            return False
        robot.position = candidate
        return True
