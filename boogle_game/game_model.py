from typing import Callable
import time



class GameModel:
    _time: str
    _current_word: list
    _path: list
    _game_is_running: bool
    _score: str
    good_words: list

    def __init__(self):
        self.reset_game()

    def del_last_char(self):
        self._current_word.pop()

    def add_char_to_word(self, c):
        self._current_word.append(c)

    @property
    def score(self):
        return self._score

    def update_score(self):
        self._score += len(self.path) ** 2
        self.taken_words.append(self.current_word())
        self.reset_word()

    def set_time(self, t):
        self._time = t

    def set_game_is_running(self, run):
        self._game_is_running = run

    def current_word(self):
        x = ''.join(self._current_word)
        return x

    def reset_word(self):
        self._current_word = []
        self._path = []

    def game_is_running(self):
        return self._game_is_running

    @property
    def path(self):
        return self._path

    def add_coor_to_path(self, coor: tuple):
        self._path.append(coor)

    def reset_game(self):
        self._time = '180'
        self._current_word = []
        self._path = []
        self._game_is_running = False
        self._score = 0
        self.taken_words = []
        self.good_words = []
