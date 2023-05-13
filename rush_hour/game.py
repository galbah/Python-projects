from sys import argv
from helper import  load_json
from car import Car
from board import Board

class Game:
    """
    game class makes combines al classes to a game,
    it makes sure all input are valid and notifies if the game is finished
    """
    global _car_list
    _car_list = []

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.board = board

    def __single_turn(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. 

        The function runs one round of the game :
            1. Get user's input of: what color car to move, and what 
                direction to move it.
            2. Check if the input is valid.
            3. Try moving car according to user's input.

        Before and after every stage of a turn, you may print additional 
        information for the user, e.g., printing the board. In particular,
        you may support additional features, (e.g., hints) as long as they
        don't interfere with the API.
        """

        choise = input("enter which car to move and what direction?")
        if choise == '!' :
            return True
        if len(choise) != 3 :
            print("input is not valid")
            return False
        if choise[1] != ',' :
            print("input is not valid")
            return False
        name_car_to_move, direction = choise.split(',')
        if not self.board.move_car(name_car_to_move, direction) :
            print("move is not legal")
        return False




    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """

        wants_to_stop = False
        target = self.board.target_location()
        while not wants_to_stop :
            print(self.board)
            wants_to_stop = self.__single_turn()
            if self.board.cell_content(target) is not None :
                print(self.board)
                print("you win!")
                break



if __name__== "__main__":

    board = Board()
    car_file = load_json(argv[1])
    for key, value in car_file.items() :
        row_index, col_index = value[1][0], value[1][1]
        new_car = Car(key, value[0], (row_index, col_index), value[2])
        if new_car.length < 2 or new_car.length > 4 :
            continue
        _car_list.append(new_car)
        if not board.add_car(new_car) :
            print("there is a car that cant be added")
            continue

    game = Game(board)
    game.play()

