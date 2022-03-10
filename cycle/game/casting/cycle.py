import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle(Actor):
    """
    A futuristic cycle that rides on a beam of light and creates a trail behind it that can not be crossed.
    
    The responsibility of Cycle is to move itself.

    Attributes:
        _points (int): The number of points.
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
    
    def get_lightCycle(self):
        return self._segments[0]

    def grow_trail(self):
        lightCycle = self._segments[0]
        velocity = lightCycle.get_velocity()
        offset = velocity.reverse()
        position = lightCycle.get_position().add(offset)
        
        segment = Actor()
        segment.set_position(position)
        segment.set_velocity(Point(0,0))
        segment.set_text("#")
        segment.set_color(constants.GREEN)
        self._segments.append(segment)

    def turn_lightCycle(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        x = int(constants.MAX_X / 4)
        y = int(constants.MAX_Y - constants.MAX_Y / 8)

        for i in range(constants.CYCLE_LENGTH):
            position = Point(x + i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0) if i == 0 else Point(0,0)
            text = "8" if i == 0 else "#"
            color = constants.YELLOW if i == 0 else constants.GREEN
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)
