#from contextlib import nullcontext
import random
import constants
from game.casting.cycle import Cycle
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle2(Actor):
    """
    A tasty item that snakes like to eat.
    
    The responsibility of Food is to select a random position and points that it's worth.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        super().__init__()
        self._segments = []
        self._prepare_body()

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
    
    def get_head(self):
        return self._segments[0]

    def grow_tail(self):
        head = self._segments[0]
        velocity = head.get_velocity()
        offset = velocity.reverse()
        position = head.get_position().add(offset)
        
        segment = Actor()
        segment.set_position(position)
        segment.set_velocity(Point(0,0))
        segment.set_text("#")
        segment.set_color(constants.RED)
        self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
        
    def _prepare_body(self):
        x = int((constants.MAX_X * 3) / 4)
        y = int(constants.MAX_Y - constants.MAX_Y / 8)

        for i in range(constants.CYCLE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0) if i == 0 else Point(0,0)
            text = "8" if i == 0 else "#"
            color = constants.YELLOW if i == 0 else constants.RED
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)
