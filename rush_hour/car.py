class Car:
    """
    representing the cars in the game, each has it own attributes
    """
    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """

        self.name = name
        self.length = length
        self.location = location
        self.orientation = orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """

        car_cor_lst = []
        row = self.location[0]
        col = self.location[1]
        if self.orientation == 0 :
            for i in range(self.length) :
                car_cor_lst.append((row+i, col))
        if self.orientation == 1 :
            for i in range(self.length) :
                car_cor_lst.append((row, col+i))
        return car_cor_lst


    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """

        moves_dict = {}
        if self.orientation == 1 :
            moves_dict['r'] = 'move right'
            moves_dict['l'] = 'move left'
        if self.orientation == 0 :
            moves_dict['u'] = 'move up'
            moves_dict['d'] = 'move down'
        return moves_dict


    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """

        if movekey not in self.possible_moves().keys() :
            return None
        else :
            if movekey == 'u' :
                cur_cor = self.car_coordinates()[0]
                req_cor = (cur_cor[0]-1, cur_cor[1])
            if movekey == 'd' :
                cur_cor = self.car_coordinates()[len(self.car_coordinates())-1]
                req_cor = (cur_cor[0]+1, cur_cor[1])
            if movekey == 'r':
                cur_cor = self.car_coordinates()[len(self.car_coordinates())-1]
                req_cor = (cur_cor[0], cur_cor[1]+1)
            if movekey == 'l':
                cur_cor = self.car_coordinates()[0]
                req_cor = (cur_cor[0], cur_cor[1]-1)
            return [req_cor]


    def move(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """

        move_to_cor  = self.movement_requirements(movekey)
        if move_to_cor is None :
            return False
        else:
            row_index = self.location[0]
            col_index = self.location[1]
            if movekey == 'd' :
                row_index += 1

            if movekey == 'u' :
                row_index -= 1

            if movekey == 'r' :
                col_index += 1

            if movekey == 'l' :
                col_index -= 1

            self.location = (row_index, col_index)
            return True


    def get_name(self):
        """
        :return: The name of this car.
        """

        return str(self.name)
