from typing import Tuple
class Apple :
    """
    represents the apples in the game, each apple has a location and a score
    """
    def __init__(self, location: Tuple, score: int) :

        self.location = location
        self.score = score
        self.color = "green"


    def get_location(self):
        return self.location

    def get_score(self):
        return self.score