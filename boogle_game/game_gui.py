import tkinter as tki
from typing import Callable, Dict, List, Any
import time
from tkinter import messagebox as mb

BUTTON_HOVER_COLOR = 'gray'
REGULAR_COLOR = 'lightgray'
BUTTON_ACTIVE_COLOR = 'slateblue'

BUTTON_STYLE = {"font": ("Courier", 20),
                "borderwidth": 10,
                "relief": tki.RAISED,
                "bg": REGULAR_COLOR,
                "activebackground": BUTTON_ACTIVE_COLOR}


class GameGui:
    # create buttons and labels dict
    _buttons: Dict[str, tki.Button] = {}
    _labels: Dict[str, tki.Label] = {}

    def __init__(self, board: list):
        # set game defult vars
        root = tki.Tk()
        root.title("Boogle Game")
        root.resizable(False, False)
        root.maxsize(1100, 700)
        # var that check if clock finish
        self.clock_finish = False
        # var that check if user wants to keep playing
        self.keep_playing = False
        self.board = board
        self.board_rows = len(board)
        self.board_cols = len(board[0])
        self.main_window = root

        self._set_frames(root)

        self._set_buttons_and_labels()

        self.main_window.bind("<Key>", self._key_pressed)

    def _set_frames(self,root):
        self._outer_frame = tki.Frame(root, bg=REGULAR_COLOR,
                                      highlightbackground=REGULAR_COLOR,
                                      highlightthickness=5)
        self._outer_frame.pack(side=tki.TOP, fill=tki.BOTH, expand=True)

        self._upper_frame = tki.Frame(self._outer_frame)
        self._upper_frame.pack(side=tki.TOP, fill=tki.BOTH, expand=True)

        self._lower_frame = tki.Frame(self._outer_frame)
        self._lower_frame.pack(side=tki.TOP, fill=tki.BOTH, expand=True)

    def _set_buttons_and_labels(self):
        self._create_labels_in_upper_frame()
        self._create_buttons_in_lower_frame()

    def run(self) -> None:
        self.main_window.mainloop()

    def _create_buttons_in_lower_frame(self) -> None:
        #set grid
        for i in range(self.board_cols + 1):
            tki.Grid.columnconfigure(self._lower_frame, i, weight=1)  # type: ignore
        for i in range(self.board_rows + 1):
            tki.Grid.rowconfigure(self._lower_frame, i, weight=1)  # type: ignore
        #set buttons
        for i in range(self.board_rows):
            for j in range(self.board_cols):
                self._make_button('*', i, j)

        self._make_button('Lets Go!', 4, 0, columnspan=1)
        self._make_button('Quit Game', 4, 1, columnspan=1)
        self._make_button('Reset Word', 4, 3, columnspan=1)
        self._make_button('Reset Game', 4, 2, columnspan=1)
        self._make_labels_lower('Created Words', 0, 4, rowspan=5)

    def _make_labels_lower(self, label_text, row, col, columnspan=1, rowspan=1):
        label = tki.Label(self._lower_frame, font=("Courier", 10),
                          bg=REGULAR_COLOR, width=15, relief="ridge", anchor='n')
        label.grid(row=row, column=col, rowspan=rowspan, columnspan=columnspan, sticky=tki.NSEW)
        self._labels[label_text] = label

    def _create_labels_in_upper_frame(self):
        tki.Grid.columnconfigure(self._upper_frame, 0, weight=1)  # type: ignore
        tki.Grid.columnconfigure(self._upper_frame, 1, weight=1)  # type: ignore
        tki.Grid.columnconfigure(self._upper_frame, 2, weight=1)  # type: ignore
        # tki.Grid.rowconfigure(self._upper_frame, 0, weight=1)  # type: ignore

        self._make_labels_upper('time', 0, 0)
        self._make_labels_upper('score', 0, 1)
        self._make_labels_upper('word', 0, 2)

    def _make_labels_upper(self, label_text, row, col, columnspan=1, rowspan=1):
        label = tki.Label(self._upper_frame, font=("Courier", 30),
                          bg=REGULAR_COLOR, width=10, relief="ridge")
        label.grid(row=row, column=col, rowspan=rowspan, columnspan=columnspan, sticky=tki.NSEW)
        self._labels[label_text] = label

    def set_good_words_display(self, display_text: str) -> None:
        self._labels['Created Words'].configure(text=display_text)

    def set_time_display(self, display_text: str) -> None:
        self._labels['time'].configure(text=display_text)

    def set_word_display(self, display_text: str):
        self._labels['word'].configure(text=display_text)

    def set_score_display(self, display_text: str):
        self._labels['score'].configure(text=display_text)

    def set_button_command(self, button_name: str, cmd: Callable[[], None]) -> None:
        self._buttons[button_name].configure(command=cmd)

    def get_button_chars(self) -> List[str]:
        return list(self._buttons.keys())

    def _make_button(self, button_char: str, row: int, col: int,
                     rowspan: int = 1, columnspan: int = 1) -> tki.Button:
        button = tki.Button(self._lower_frame, text=button_char, **BUTTON_STYLE)
        button.grid(row=row, column=col, rowspan=rowspan, columnspan=columnspan, sticky=tki.NSEW)
        self._buttons[(row, col)] = button

    def _key_pressed(self, event: Any) -> None:
        """the callback method for when a key is pressed.
        It'll simulate a button press on the right button."""
        if event.char in self._buttons:
            self._simulate_button_press(event.char)
            self.color_pressed_button(event.char)
        # elif event.keysym == "Return":
        #     self._simulate_button_press("=")

    def set_button_chars(self):
        for i in range(self.board_rows):
            for j in range(self.board_cols):
                self._buttons[(i, j)].configure(text=self.board[i][j])

    def exit_game(self):
        self.main_window.after_cancel(self.main_window)
        self.main_window.destroy()

    def _simulate_button_press(self, button_char: str) -> None:
        """make a button light up as if it is pressed,
        and then return to normal"""
        button = self._buttons[button_char]
        button["bg"] = BUTTON_ACTIVE_COLOR

        def return_button_to_normal() -> None:
            # find which widget the mouse is pointing at:
            x, y = self.main_window.winfo_pointerxy()
            widget_under_mouse = self.main_window.winfo_containing(x, y)
            # change color accordingly:
            if widget_under_mouse is button:
                button["bg"] = BUTTON_HOVER_COLOR
            else:
                button["bg"] = REGULAR_COLOR

        button.invoke()  # type: ignore
        button.after(100, func=return_button_to_normal)

    def update_clock(self, t):

        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        self._labels['time'].configure(text=timer)
        if t == 0:
            self._labels['time'].configure(text='00:00')
            self.clock_finish = True
            self.check_if_play_again()
            return
        self.main_window.after(1000, lambda: self.update_clock(t - 1))

    def check_if_play_again(self):
        self.keep_playing = mb.askyesno('shit', "do you want to continue?")
        if not self.keep_playing:
            self.exit_game()

    def color_pressed_button(self, button_char):
        button = self._buttons[button_char]
        button["bg"] = BUTTON_HOVER_COLOR

    def reset_buttons_color(self):
        for button in self._buttons.values():
            button["bg"] = REGULAR_COLOR
