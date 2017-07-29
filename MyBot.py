import hlt
from hlt import NORTH, EAST, SOUTH, WEST, STILL, Move, Square
import random

myID, game_map = hlt.get_init()
hlt.send_init("PythonBot")


def findNearestEnemyDirection(loc):
    CARDINALS = NORTH, EAST, SOUTH, WEST, STILL
    direction = NORTH;

    maxDistance = min(game_map.width, game_map.height) / 2;

    for direction, in CARDINALS:
        distance = 0
        current = loc
        site = game_map.getSite(current, direction)
        while (site.owner == id and distance < maxDistance):
            distance += 1
            current = game_map.getLocation(current, direction)
            site = game_map.getSite(current)

        if (distance < maxDistance):
            newDirection = direction
            maxDistance = distance

    return newDirection

def assign_move(square):
    for direction, neighbor in enumerate(game_map.neighbors(square)):
        if neighbor.owner != myID and neighbor.strength < square.strength:
            return Move(square, direction)

    if square.strength < 5 * square.production:
        return Move(square, STILL)
    else:
        return Move(square, findNearestEnemyDirection(square))




while True:
    game_map.get_frame()
    moves = [assign_move(square) for square in game_map if square.owner == myID]
    hlt.send_frame(moves)