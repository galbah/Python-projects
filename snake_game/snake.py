from typing import List, Any, Tuple
import game_parameters


class Link:
    """
    represents the object that the snake is made of
    """

    def __init__(self, location: Tuple) -> None:
        """
        :param color: color of link
        :param location: location of link
        """
        self.location = location


class Snake:
    """
    the snake in Snake game, build as a list of Links
    """

    def __init__(self, head_location: Tuple, length=3, color="black") -> None:
        """
        :param location: a list of tuples contains the location of every link that the snake is made of
        :param length: the length of the snake - number of links that it is made of
        :param color: color of the snake
        """
        self.head_location = head_location
        self.length = length
        self.color = color
        self.ate_apple = False
        self.direction = "Up"
        self.links = []
        for i in range(length):
            link_location = (head_location[0], head_location[1] - i)
            link = Link(link_location)
            self.links.append(link)

    def get_head_location(self):
        # returns the location of the first link in the snakes links list
        return self.head_location

    def change_ate_apple(self, did_it_eat: bool):
        # changes th boolean expression that indicates if the snake ate an apple or not, if it should grow or not
        self.ate_apple = did_it_eat

    def check_collide(self):
        """
        :return: True if the snake collide into itself, False otherwise
        """
        if self.get_head_location() in self._get_links_coordinates(self.links[1:]):
            return True
        return False

    def cut_head(self):
        self.links.remove(self.links[0])

    def get_coordinates(self):
        """
        :return: the coordinates of all links in snake
        """
        coor_list = self._get_links_coordinates(self.links)
        return coor_list

    def _get_links_coordinates(self, links: List):
        """
        :param links: list pf links
        :return:list of coordinates of the links
        """
        coor_list = []
        for link in links:
            coor_list.append(link.location)
        return coor_list

    def move_snake(self, move_direction: str) -> None:
        """
        :param direction: the direction the snake should move
        changes snake coordinates according to the move
        if ate_apple is True it doesnt remove the snakes last link after a move
        """
        new_link_location = []
        cur_row = self.head_location[1]
        cur_col = self.head_location[0]
        # ---if move_direction is None continue in same direction---
        if not move_direction:
            move_direction = self.direction
        # ---snake cannot go in opposite direction check---
        not_legal_moves = [["Down", "Up"], ["Right", "Left"]]
        for moves in not_legal_moves:
            if self.direction in moves and move_direction in moves:
                move_direction = self.direction

        if move_direction == "Up":
            new_link_location = (cur_col, cur_row + 1)
        if move_direction == "Down":
            new_link_location = (cur_col, cur_row - 1)
        if move_direction == "Right":
            new_link_location = (cur_col + 1, cur_row)
        if move_direction == "Left":
            new_link_location = (cur_col - 1, cur_row)

        # ---check if new link in border---
        if 0 <= new_link_location[0] < game_parameters.WIDTH and 0 <= new_link_location[1] < game_parameters.HEIGHT:
            self.head_location = new_link_location
            self.direction = move_direction
            new_link = Link(new_link_location)
            self.links.insert(0, new_link)
            if not self.ate_apple:
                self.links.remove(self.links[len(self.links) - 1])
            return True
        else:
            self.links.remove(self.links[len(self.links) - 1])
            return False
