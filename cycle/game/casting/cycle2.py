import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle2(Actor):
    """
    A futuristic cycle that rides on a beam of light and creates a trail behind it that can not be crossed.
    
    The responsibility of Cycle is to move itself.
    """
    def __init__(self):
        """
        Attributes:
        _segments []: Holds the segment details
        _prepare_body(): prepares a new cycle with segments
        """
        super().__init__()
        self._segments = []
        self._prepare_body()

    def get_segments(self):
        """
        Returns segment details
        """
        return self._segments

    def move_next(self):
        # move all segments
        """
        Sets the movement for each segment
        """
        for segment in self._segments:
            segment.move_next()
    
    def get_lightCycle(self):
        """
        Returns the cycle segment details of the Cycle object
        """
        return self._segments[0]

    def grow_trail(self):
        """
        Creates a new segment and appends the segment details to the previous location of the cycle.
        
        Attributes:
        lightCycle: lead segment of the cycle object
        velocity: direction the lightCycle is heading
        offset: used to set location of new segment at the previous location of the cycle
        position: location for new segment
        """
        lightCycle = self._segments[0]
        velocity = lightCycle.get_velocity()
        offset = velocity.reverse()
        position = lightCycle.get_position().add(offset)
        
        segment = Actor()
        segment.set_position(position)
        segment.set_velocity(Point(0,0))
        segment.set_text("#")
        segment.set_color(constants.RED)
        self._segments.append(segment)

    def turn_lightCycle(self, velocity):
        """
        Sets the new velocity for the cycle based on key presses
        """
        self._segments[0].set_velocity(velocity)
        
    def _prepare_body(self):
        """
        Creates the body and cycle trail for the Cycle object

        Attributes:
        x(int): Starting x position for the cycle
        y(int): Starting y position for the cycle
        """
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
