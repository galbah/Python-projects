

import game_parameters


class Bomb:
    def __init__(self, time_state, taken_coors):
        self.border = (game_parameters.WIDTH, game_parameters.HEIGHT)
        self.__color = None
        self.__exp_radius = None
        self.__timer_bomb = None
        self.__when_it_will_explode = None
        self.__location = None
        self.__time_state = None
        self.__first_location = None
        self.__exploded = None
        self.reset_bomb(time_state, taken_coors)

    def reset_bomb(self, time_state, taken_coors=[]):
        x, y, radius, time = game_parameters.get_random_bomb_data()
        while (x, y) in taken_coors:
            x, y, radius, time = game_parameters.get_random_bomb_data()
        self.__color = 'red'
        self.__exp_radius = radius
        self.__timer_bomb = time - 1
        self.__when_it_will_explode = self.get_timer_bomb() + time_state
        self.__location = [(x, y)]
        self.__time_state = time_state
        self.__first_location = (x, y)
        self.__exploded = False

    def get_color(self):
        return self.__color

    def get_when_it_will_explode(self):
        return self.__when_it_will_explode

    def get_time_state(self):
        return self.__time_state

    def get_timer_bomb(self):
        return self.__timer_bomb

    def get_bomb_exploded(self):
        return self.__exploded

    def set_time_state(self, time):
        self.__time_state = time
        if time >= self.get_when_it_will_explode():
            self.boom()

    def get_first_location(self):
        return self.__first_location

    def __set_color(self, color):
        self.__color == color

    def __set_location(self, location):
        self.__location = location

    def get_exp_radius(self):
        return self.__exp_radius

    def get_location(self):
        return self.__location

    def boom(self):
        # ---counts the round from explosion to the end of it---
        delta_explode = self.get_time_state() - self.get_when_it_will_explode()
        self.__color = 'orange'
        self.__move_bomb_explode(delta_explode)

    def __move_bomb_explode(self, delta_explode):
        """
        :param delta_explode: the range the explosion in the correct round
        :return: None
        """
        new_location = []
        if self.get_exp_radius() > delta_explode > 0:
            for i in self.get_location():
                x, y = i[0], i[1]
                #---checks if one of new location out of border---
                self.__check_if_one_of_location_out_of_border(x, y, self.border)

                new_location += self.__check_and_append_location(x, y, delta_explode)
            self.__set_location(list(set(new_location)))  # I did this to remove duplicates of coor

        elif self.get_exp_radius() <= delta_explode:
            self.__exploded = True

    def __check_and_append_location(self, x, y, delta):
        """gets x and y coordinates of point and returns a list of next location on range of explosion"""
        new_location = []
        if self.__check_distance_from_start_is_on_edge(x + 1, y, delta):
            new_location.append((x + 1, y))
        if self.__check_distance_from_start_is_on_edge(x, y + 1, delta):
            new_location.append((x, y + 1))
        if self.__check_distance_from_start_is_on_edge(x - 1, y, delta):
            new_location.append((x - 1, y))
        if self.__check_distance_from_start_is_on_edge(x, y - 1, delta):
            new_location.append((x, y - 1))

        return new_location

    def __check_if_one_of_location_out_of_border(self, x, y, border):
        """gets x and y coordinates of point and set bomb as finished to explode"""
        if self.__check_out_of_bounds(x + 1, y, border) or self.__check_out_of_bounds(x, y + 1,
                                                                                      border) or self.__check_out_of_bounds(
            x - 1, y, border) or self.__check_out_of_bounds(x, y - 1, border):
            self.__exploded = True

    def __check_distance_from_start_is_on_edge(self, x, y, delta):
        """gets x and y coordinates of point and return True its equals to range of explosion"""
        return abs(x - self.get_first_location()[0]) + abs(y - self.get_first_location()[1]) == delta

    def __check_out_of_bounds(self, x, y, border):
        """gets x and y coordinates of point and return True if out of game border"""
        if x < 0 or x > border[0] - 1 or y < 0 or y > border[1] - 1:
            return True
        return False
