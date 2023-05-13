import sys
from typing import Callable
from game_model import GameModel
from game_gui import GameGui
from boggle_board_randomizer import randomize_board
import ex12_utils


class GameController:
    def __init__(self) -> None:
        self._model = GameModel()
        self.board = randomize_board()
        self._gui = GameGui(self.board)

        self.good_words = []
        self.set_first_displays()
        self.set_buttons()
        self.words_lst = self.set_words_list()
        self.finish = False

    def set_first_displays(self):
        self._gui.set_time_display('03:00')
        self._gui.set_word_display('')
        self._gui.set_score_display('Score: ' + str(self._model.score))
        self._gui.set_good_words_display('Good Words:')

    def set_buttons(self):
        # set chars buttons
        for btn in self._gui.get_button_chars():
            action = self.create_button_action(btn)
            self._gui.set_button_command(btn, action)
        # set lets go button
        self.set_lets_go()
        # set reset word button
        self.set_reset_word()
        # set quit game button
        self.set_quit_game()
        # set reset game button
        self.set_reset_game()

    def set_words_list(self):
        with open('boggle_dict.txt', 'r') as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
        return lines

    def reset_game(self):
        self._gui.main_window.destroy()
        GameController().run()

    def set_lets_go(self):
        # lets go button
        self._gui.set_button_command((4, 0), self.lets_go_action())

    def check_game_state(self):
        if self._gui.keep_playing:
            self.reset_game()
        self._gui.main_window.after(300, lambda: self.check_game_state())

    def lets_go_action(self):
        def action():
            if not self._model.game_is_running() and not self._gui.clock_finish:
                self._model.set_game_is_running(True)
                self._gui.set_button_chars()
                self._gui.update_clock(180)
                # self._model.set_game_is_running()

        return action

    def set_reset_word(self):
        self._gui.set_button_command((4, 3), lambda: (self._model.reset_word(),
                                                      self._gui.set_word_display(self._model.current_word()),
                                                      self._gui.reset_buttons_color()))

    def set_quit_game(self):
        self._gui.set_button_command((4, 1), lambda: self._gui.exit_game())

    def set_reset_game(self):
        self._gui.set_button_command((4, 2), lambda: self.reset_game())

    def check_valid_char(self, path, coor):
        if len(path) == 0:
            return True
        prev_coor = path[-1]
        neighbors_coors = ex12_utils.get_neighbors_coors(prev_coor[0], prev_coor[1], path)
        if coor in neighbors_coors:
            return True
        return False

    def check_word_in_dict(self):
        word = self._model.current_word()
        if word in self.words_lst:
            self.words_lst.remove(word)
            self.good_words.append(word)
            self._gui.set_good_words_display('Good Words:\n' + '\n'.join(self.good_words))
            return True
        return False

    def create_button_action(self, btn) -> Callable[[], None]:
        def fun() -> None:
            if self._model.game_is_running() and self.check_valid_char(self._model.path,
                                                                       btn) and not self._gui.clock_finish:
                #go down in line
                if len(self._model.current_word()) % 10 == 0 and len(self._model.current_word()) > 0:
                    self._model.add_char_to_word(self.board[btn[0]][btn[1]] + '\n')
                else:
                    self._model.add_char_to_word(self.board[btn[0]][btn[1]])
                self._gui.color_pressed_button(btn)
                # btn is tuple coor
                self._model.add_coor_to_path(btn)
                self._gui.set_word_display(self._model.current_word())
                # check if good word
                if self.check_word_in_dict():
                    self._model.update_score()
                    self._gui.set_word_display('')
                    self._gui.set_score_display('Score: ' + str(self._model.score))
                    self._gui.reset_buttons_color()

        return fun

    def run(self) -> None:
        self.check_game_state()
        self._gui.run()


if __name__ == "__main__":
    GameController().run()
