import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the cycle collides
    with another cycle, or the cycle collides with its trails, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        if not self._is_game_over:
            self._handle_segment_addition(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
    
    def _handle_segment_addition(self, cast):
        """Updates the score and if a player collides with a light trail.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycle = cast.get_first_actor("cycle")
        cycle.grow_trail()
        cycle2 = cast.get_first_actor("cycle2")
        cycle2.grow_trail()

                  
        
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the cycle collides with one of its or another players trail.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycleCollision = False
        cycleCollision2 = False
        score = cast.get_first_actor("score")
        score2 = cast.get_first_actor("score2")

        cycle = cast.get_first_actor("cycle")
        lightCycle = cycle.get_segments()[0]
        segments = cycle.get_segments()[1:]

        cycle2 = cast.get_first_actor("cycle2")
        lightCycle2 = cycle2.get_segments()[0]
        segments2 = cycle2.get_segments()[1:]

        if lightCycle.get_position().equals(lightCycle2.get_position()):
            self._is_game_over = True
            cycleCollision = True
            cycleCollision2 = True
        
        for segment in segments:
            if lightCycle.get_position().equals(segment.get_position()):
                self._is_game_over = True
                cycleCollision = True
            elif lightCycle2.get_position().equals(segment.get_position()):
                self._is_game_over = True
                cycleCollision2 = True
        
        for segment2 in segments2:
            if lightCycle.get_position().equals(segment2.get_position()):
                self._is_game_over = True
                cycleCollision = True
            elif lightCycle2.get_position().equals(segment2.get_position()):
                self._is_game_over = True
                cycleCollision2 = True
        
        if cycleCollision == True and cycleCollision2 == False:
            score2.add_points(1)
        elif cycleCollision2 == True and cycleCollision == False:
            score.add_points(1)


        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the cycles to white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            cycle = cast.get_first_actor("cycle")
            segments = cycle.get_segments()
            score = cast.get_first_actor("score")
            cycle2 = cast.get_first_actor("cycle2")
            segments2 = cycle2.get_segments()
            score2 = cast.get_first_actor("score2")

            if score._points == score2._points:
                score.set_color(constants.ORANGE)
                score2.set_color(constants.ORANGE)
                score.set_text(f"Player One: Loser")
                score2.set_text(f"Player Two: Loser")
            elif score._points != 0:
                score.set_color(constants.ORANGE)
                score2.set_color(constants.ORANGE)
                score.set_text(f"Player One: Winner")
                score2.set_text(f"Player Two: Loser")
            elif score2._points != 0:
                score.set_color(constants.ORANGE)
                score2.set_color(constants.ORANGE)
                score.set_text(f"Player One: Loser")
                score2.set_text(f"Player Two: Winner")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text(f"Game Over!")
            message.set_position(position)
            message.set_color(constants.ORANGE)
            cast.add_actor("messages", message)

            # segments[0].set_color(constants.WHITE)
            # for segment in segments:
            #     segment.set_color(constants.WHITE)
            # segments2[0].set_color(constants.WHITE)
            # for segment2 in segments2:
            #     segment2.set_color(constants.WHITE)
