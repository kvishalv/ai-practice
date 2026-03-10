from problems.robot_grid.src.arena import Arena
from problems.robot_grid.src.point import Point
from problems.robot_grid.src.robot import Robot


def test_robot_turns_left() -> None:
    robot = Robot(Point(1, 1), "N")
    robot.turn_left()
    assert robot.direction == "W"


def test_robot_turns_right() -> None:
    robot = Robot(Point(1, 1), "N")
    robot.turn_right()
    assert robot.direction == "E"


def test_robot_moves_forward_when_space_is_valid() -> None:
    arena = Arena(5, 5)
    robot = Robot(Point(1, 1), "N")

    moved = arena.move_robot(robot)

    assert moved is True
    assert robot.position == Point(1, 2)


def test_robot_does_not_move_into_obstacle() -> None:
    arena = Arena(5, 5, obstacles={Point(1, 2)})
    robot = Robot(Point(1, 1), "N")

    moved = arena.move_robot(robot)

    assert moved is False
    assert robot.position == Point(1, 1)
