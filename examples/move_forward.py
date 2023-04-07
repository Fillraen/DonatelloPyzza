from donatellopyzza import Game
from donatellopyzza import Action
from donatellopyzza import Feedback
from donatellopyzza import Maze
import donatellopyzza
import random
import time


if __name__ == '__main__':
    # the name of the environment
    __ENVIRONMENT__ = "maze"
    # display the interface (or not)
    __GUI__ = True

    game = Game(__ENVIRONMENT__, __GUI__)
    # returns a turtle that execute actions on its environment
    turtle = game.start()
    
    while not game.isWon():
        # execute the path step by step
        for a in actions:
            time.sleep(0.3)
            r = random.randint(0, 3)
            actions = [Action.MOVE_FORWARD, Action.TOUCH, Action.TURN_LEFT, Action.TURN_RIGHT]
            result = turtle.execute(actions[r])