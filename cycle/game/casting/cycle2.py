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
        self._segments2 = []
        self._prepare_body()

    def get_segments(self):
        return self._segments2

    def move_next(self):
        # move all segments
        for segment in self._segments2:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments2) - 1, 0, -1):
            trailing = self._segments2[i]
            previous = self._segments2[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)
    
    def get_head(self):
        return self._segments2[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments2[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment2 = Actor()
            segment2.set_position(position)
            segment2.set_velocity(velocity)
            segment2.set_text("O")
            segment2.set_color(constants.RED)
            self._segments2.append(segment2)

    def turn_head(self, velocity):
        self._segments2[0].set_velocity(velocity)
        
    def _prepare_body(self):
        #x = 15 
        x = random.randint(451, 900)
        #y = 15 
        y = random.randint(301, 600)

        for i in range(constants.CYCLE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(0, 0)
            text = "+" if i == 0 else "O"
            color = constants.YELLOW if i == 0 else constants.RED
            
            segment2 = Actor()
            segment2.set_position(position)
            segment2.set_velocity(velocity)
            segment2.set_text(text)
            segment2.set_color(color)
            self._segments2.append(segment2)