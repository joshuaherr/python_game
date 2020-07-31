from enum import Enum


class Directions(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class MovementStates(Enum):
    MOVE_DOWN_STAND = 1
    MOVE_DOWN_RIGHT_FOOT = 2
    MOVE_DOWN_LEFT_FOOT = 3
    MOVE_RIGHT_STAND = 4
    MOVE_RIGHT_RIGHT_FOOT = 5
    MOVE_RIGHT_LEFT_FOOT = 6
    MOVE_UP_STAND = 7
    MOVE_UP_RIGHT_FOOT = 8
    MOVE_UP_LEFT_FOOT = 9
    MOVE_LEFT_STAND = 10
    MOVE_LEFT_RIGHT_FOOT = 11
    MOVE_LEFT_LEFT_FOOT = 12

