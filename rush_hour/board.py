from car import Car

class Board:
    """
    board class represent the board of the game,
    the board doesnt change after constructed
    """
    global ROWS, COLS
    ROWS, COLS = 7, 7
    global _car_list
    _car_list = []

    def __init__(self):

        self.board = []
        for i in range(ROWS) :
            temp_row = []
            for j in range(COLS) :
                temp_row.append('_')
            self.board.append(temp_row)
        self.board[COLS//2].append('_')     # exit point


    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """

        str_board = ''
        for i in range(ROWS):
            str_board += str(self.board[i]) +'\n'
        return str_board


    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """

        cord_list = []
        for i in range(ROWS) :
            for j in range(COLS+1) :
                if j == COLS and i != COLS//2 :
                    continue
                cord_list.append((i,j))
        return cord_list


    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description)
                 representing legal moves
        """

        moves_lst = []
        target = self.target_location()
        if not _car_list :
            return moves_lst
        for car in _car_list :
            if car.orientation == 1 :
                directions = ['r','l']
            elif car.orientation == 0 :
                directions = ['u','d']
            else:
                return
            for direction in directions :
                requiremnts = car.movement_requirements(direction)
                for req in requiremnts :
                    if req == target :
                        moves_lst.append((car.get_name(), direction, "description"))
                    if req[0] < 0 or req[0] > ROWS-1 or req[1] < 0 or req[1] > COLS-1 :
                        continue
                    if self.cell_content((req[0], req[1])) != None :
                        continue
                    elif -1 < req[0] < ROWS+1 and -1 < req[1] < COLS+1 :
                        moves_lst.append((car.get_name(), direction, "description"))
                    else:
                        continue
        return moves_lst


    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """

        return (ROWS//2, COLS)


    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """

        x = coordinate[0]
        y = coordinate[1]
        if self.board[x][y] == '_' :
            return None
        else:
            return self.board[x][y]


    def add_car(self, car: Car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """

        car_name = car.get_name()
        for i in range(ROWS):
            if car_name in self.board[i] :
                return False
        _car_list.append(car)
        car_coor = car.car_coordinates()
        for coor in car_coor :
            if coor not in self.cell_list() :
                return False
            if self.cell_content(coor) is not None :
                return False
        for coor in car_coor :
            self.board[coor[0]][coor[1]] = car_name
        return True


    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """

        for _car in _car_list :
            if _car.get_name() == name :
                car = _car
                break
        move = (name, movekey, "description")
        if move not in self.possible_moves() :
            return False

        car_length = car.length
        car_row = car.location[0]
        car_col = car.location[1]

        if movekey == 'u' :
            self.board[car_row-1][car_col] = name
            self.board[car_row+car_length-1][car_col] = '_'
        if movekey == 'd' :
            self.board[car_row][car_col] = '_'
            self.board[car_row+car_length][car_col] = name
        if movekey == 'r' :
            self.board[car_row][car_col] = '_'
            self.board[car_row][car_col+car_length] = name
        if movekey == 'l' :
            self.board[car_row][car_col-1] = name
            self.board[car_row][car_col+car_length-1] = '_'
        car.move(movekey)
        return True


