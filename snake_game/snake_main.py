import game_parameters
from snake import Snake
from game_display import GameDisplay
from apple import Apple
from bomb import Bomb


def main_loop(gd: GameDisplay) -> None:
    # the main loop is in charge on the continuity of the game and stops it if the user lost or won

    # ---setting the parameters required for first round of game---
    taken_coors, score, apple_list, num_round, stop_growing_round, snake, bomb, finish_game = set_first_round(gd)
    if finish_game :
        return

    # ---draws board elements---
    draw_board(apple_list, bomb, snake, gd)

    # ---updates the score value---
    gd.show_score(0)

    gd.end_round()

    while True:
        key_clicked = gd.get_key_clicked()

        # ---setting the bomb state---
        bomb_set_up(bomb, num_round, taken_coors)

        # ---setting the taken coordinates for this round---
        taken_coors = snake.get_coordinates() + bomb.get_location() + get_apples_location(apple_list)

        # ---checks if snake collide with himself or with the bomb or in game border end finish---
        if check_lost(snake, bomb, key_clicked):
            draw_board(apple_list, bomb, snake, gd)
            gd.end_round()
            break

        # ---apples---
        add_to_score, snake_ate_apple = check_apple(snake, bomb, apple_list, taken_coors)
        if not update_apples(apple_list, taken_coors) :
            draw_board(apple_list, bomb, snake, gd)
            gd.end_round()
            break
        stop_growing_round = check_stop_growing(snake_ate_apple, stop_growing_round, snake, num_round)

        # ---update and show score---
        score += add_to_score
        gd.show_score(score)

        # ---draws board elements---
        draw_board(apple_list, bomb, snake, gd)

        # ---add 1 to round number---
        num_round += 1

        gd.end_round()
    return


def set_first_round(gd):
    # creates all necessary parameters and returns them
    taken_coors = []
    score = 0
    apple_list = []
    num_round = 0
    stop_growing_round = -1
    finish_game = False

    # ---setting up the snake object, in start point (10,10) and length 3---
    snake = Snake((10, 10), 3)

    taken_coors += snake.get_coordinates()

    # ---setting up the bomb object---
    bomb = Bomb(num_round, taken_coors)
    taken_coors += bomb.get_location()

    # ---stting up apples---
    for t in range(3):
        if check_free_space(taken_coors) :
            apple = create_apple(taken_coors)
            taken_coors += apple.get_location()
            apple_list.append(apple)
        else :
            finish_game = True

    return taken_coors, score, apple_list, num_round, stop_growing_round, snake, bomb, finish_game


def check_free_space(taken_coors) :
    # returns False if all coordinates in game are taken, and False otherwise
    if len(taken_coors) >= game_parameters.WIDTH * game_parameters.HEIGHT :
        return False
    return True


def update_apples(apple_list, taken_coors) -> bool:
    # makes sure there are always 3 apples
    if len(taken_coors) == game_parameters.WIDTH * game_parameters.HEIGHT :
        return False
    while len(apple_list) < 3:
        apple = create_apple(taken_coors)
        apple_list.append(apple)
    return True


def check_stop_growing(snake_ate_apple, stop_growing_round, snake, num_round):
    """
    :param snake_ate_apple: True if snake ate an apple in this round, False otherwise
    :param stop_growing_round: the current round that the snake should stop growing
    :param num_round: number of current round
    if the stop_growing_round did not pass yet adds 3 to it, else makes stop_growing round to be current + 3
    also changes snake_ate_apple to True if snake should grow, and to False otherwise
    :return: the new round number that the snake should stop growing in
    """
    if snake_ate_apple:
        if stop_growing_round > num_round:
            stop_growing_round += 3
        else:
            stop_growing_round = num_round + 3
        snake.change_ate_apple(True)
    if num_round == stop_growing_round:
        snake.change_ate_apple(False)
    return stop_growing_round


def get_apples_location(apple_list):
    apple_coors = []
    for apple in apple_list:
        apple_coors.append(apple.get_location())
    return apple_coors


def draw_board(apple_list, bomb, snake, gd):
    # draws all items on board
    draw_snake(snake, gd)
    draw_bomb(bomb, gd)
    draw_apples(apple_list, gd)


def create_apple(taken_coors):
    """ :param apple_list: a list contains all apples that are in game
    :param taken_coors: list of coordinates that are taken by other object
    creates an apple in a place that is not taken and adds it to the list """
    x, y, apple_score = game_parameters.get_random_apple_data()
    while (x, y) in taken_coors:
        x, y, apple_score = game_parameters.get_random_apple_data()
    apple = Apple((x, y), apple_score)
    taken_coors.append(apple.get_location())
    return apple


def check_empty(coor, taken_coors):
    # True if the coordinate given is empty, False if it is taken
    if coor in taken_coors:
        return False
    return True


def check_apple(snake, bomb, apple_lst, taken_coors):
    """
    :param apple_lst: list of apples that are created and not destroyed yet
    makes all checks concerning the apples:
    if the snake ate the apple, if the bomb destroyed the apple
    :return: if the snake ate the apple : the score of the apple, True
             else: 0, False
    """
    score = 0
    snake_ate_apple = False
    bomb_coor = bomb.get_location()
    snake_head_location = snake.get_coordinates()[0]
    for apple in apple_lst:
        # ---bomb touches an apple---
        if apple.get_location() in bomb_coor:
            taken_coors.remove(apple.get_location())
            apple_lst.remove(apple)
        # ---snakes eats apple---
        if apple.get_location() == snake_head_location:
            taken_coors.remove(apple.get_location())
            apple_lst.remove(apple)
            score += apple.get_score()
            snake_ate_apple = True
    return score, snake_ate_apple


def check_lost(snake, bomb, key_clicked):
    # ---return TRUE if lost game (snake touch bomb/himself/boarder), False otherwise---

    # ---moving snake and checking if snake touch borders---
    if not snake.move_snake(key_clicked):
        return True
    # ---checks if snake colide with himself
    elif snake.check_collide():
        snake.cut_head()
        return True
    # ---checks if bomb and snake same location---
    elif set(bomb.get_location()).intersection(snake.get_coordinates()):
        # ---"cutting the head" if snake colide with head in unexploded bomb---
        if snake.get_head_location() in bomb.get_location():
            snake.cut_head()
        return True
    return False


def draw_snake(snake, gd):
    for coor in snake.get_coordinates():
        gd.draw_cell(coor[0], coor[1], snake.color)


def draw_apples(apple_list, gd):
    for apple in apple_list:
        gd.draw_cell(apple.location[0], apple.location[1], apple.color)


def draw_bomb(bomb, gd):
    for one_location in bomb.get_location():
        gd.draw_cell(one_location[0], one_location[1], bomb.get_color())


def bomb_set_up(bomb, num_round, taken_coors):
    # ---updating the bomb time (num_round), and taken coors and if exploded reset the bomb---
    bomb.set_time_state(num_round)
    if bomb.get_bomb_exploded():
        bomb.reset_bomb(num_round, taken_coors)
