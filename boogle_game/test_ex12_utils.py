from ex12_utils import *
import os

TEST_DICT_ROOT = "test-dicts"


# noinspection Duplicates
def file_path(name):
    return os.path.join(TEST_DICT_ROOT, name)


# class TestLoadWordsDict:
#
#     def test_basic(self):
#         expected = {"dog": True, "cat": True, "meow": True}
#         assert load_words_dict(file_path("alpha.txt")) == expected
#
#     def test_non_alpha(self):
#         expected = {"123": True, "!@#": True, "***": True}
#         assert load_words_dict(file_path("non-alpha.txt")) == expected
#
#     def test_spaces(self):
#         expected = {"a a": True, "b b": True}
#         assert load_words_dict(file_path("spaces.txt")) == expected
#
#     def test_empty_line(self):
#         expected = {"bob": True, "": True, "cat": True}
#         assert load_words_dict(file_path("empty-line.txt")) == expected


# noinspection Duplicates
class TestIsValidPath:

    def test_basic_row(self):
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'I', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BIT': True}
        path = [(0, 0), (0, 1), (0, 2)]
        assert is_valid_path(board, path, word_dict) == "CAT"
#
    def test_basic_col(self):
        board = [['C', 'D', 'B', 'Q'],
                 ['A', 'O', 'I', 'Q'],
                 ['T', 'G', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BIT': True}
        path = [(0, 0), (1, 0), (2, 0)]
        assert is_valid_path(board, path, word_dict) == "CAT"
#
    def test_basic_diag_1(self):
        board = [['D', 'Q', 'Q', 'Q'],
                 ['Q', 'O', 'Q', 'Q'],
                 ['Q', 'Q', 'G', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BOT': True}
        path = [(0, 0), (1, 1), (2, 2)]
        assert is_valid_path(board, path, word_dict) == "DOG"

    def test_changed_direction(self):
        board = [['A', 'T', 'R', 'Q'],
                 ['Q', 'L', 'E', 'Q'],
                 ['Q', 'Q', 'B', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'ALBERT': True}
        path = [(0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1)]
        assert is_valid_path(board, path, word_dict) == "ALBERT"

    def test_valid_path_word_not_in_dict(self):
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'I', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'DOG': True, 'BIT': True}
        path = [(0, 0), (0, 1), (0, 2)]
        assert is_valid_path(board, path, word_dict) is None

    def test_valid_path_word_shorter_than_in_dict(self):
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'I', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BIT': True}
        path = [(0, 0), (0, 1)]
        assert is_valid_path(board, path, word_dict) is None

    def test_valid_path_word_longer_than_in_dict(self):
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'I', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BIT': True}
        path = [(0, 0), (0, 1), (0, 2), (0, 3)]
        assert is_valid_path(board, path, word_dict) is None

    def test_path_exits_board(self): ##
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'I', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BIT': True}
        path = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]
        assert is_valid_path(board, path, word_dict) is None

    def test_path_starts_outside_board(self): ###
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'I', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BIT': True}
        path = [(0, 4), (0, 3), (0, 2)]
        assert is_valid_path(board, path, word_dict) is None

    def test_same_point_twice_in_path(self):
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'I', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BIT': True}
        path = [(0, 0), (0, 1), (0, 0)]
        assert is_valid_path(board, path, word_dict) is None

    def test_not_adjacent_coordinates(self): ###
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'I', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BIT': True}
        path = [(0, 0), (0, 1), (2, 2)]
        assert is_valid_path(board, path, word_dict) is None

    def test_negative_coordinates(self):
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'I', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BIT': True}
        path = [(0, -2), (0, -1), (0, 0)]
        assert is_valid_path(board, path, word_dict) is None

    def test_empty_path(self):
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'I', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BIT': True}
        path = []
        assert is_valid_path(board, path, word_dict) is None

    def test_one_letter_in_dict(self):
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'I', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'C': True, 'DOG': True, 'BIT': True}
        path = [(0, 0)]
        assert is_valid_path(board, path, word_dict) == "C"

    def test_one_letter_not_in_dict(self):
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'I', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'P': True, 'DOG': True, 'BIT': True}
        path = [(0, 0)]
        assert is_valid_path(board, path, word_dict) is None

    def test_multi_letter_cells(self):
        board = [['Q', 'Q', 'Q', 'Q'],
                 ['DO', 'GS', 'Q', 'Q'],
                 ['Q', 'Q', 'Q', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'DOGS': True}
        path = [(1, 0), (1, 1)]
        assert is_valid_path(board, path, word_dict) == "DOGS"


def load_words_dict(file):
    milon = open(file)
    lines = set(line.strip() for line in milon.readlines())
    milon.close()
    return lines


# noinspection Duplicates
class TestFindWords:

    # Regular cases

    def test_basic_rows(self):
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'I', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BIT': True}
        expected = [[(0, 0), (0, 1), (0, 2)],
                    [(1, 0), (1, 1), (1, 2)],
                    [(2, 0), (2, 1), (2, 2)]]
        assert sorted(find_length_n_words(3, board, word_dict)) == \
               sorted(expected)

    def test_basic_cols(self):
        board = [['C', 'D', 'B', 'Q'],
                 ['A', 'O', 'I', 'Q'],
                 ['T', 'G', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BIT': True}
        expected = [[(0, 0), (1, 0), (2, 0)],
                    [(0, 1), (1, 1), (2, 1)],
                    [(0, 2), (1, 2), (2, 2)]]
        assert sorted(find_length_n_words(3, board, word_dict)) == \
               sorted(expected)

    def test_basic_diag_1(self):
        board = [['D', 'Q', 'Q', 'Q'],
                 ['Q', 'O', 'Q', 'Q'],
                 ['Q', 'Q', 'G', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BOT': True}
        expected = [[(0, 0), (1, 1), (2, 2)]]
        assert find_length_n_words(3, board, word_dict) == expected

    def test_basic_diag_2(self):
        board = [['Q', 'Q', 'D', 'Q'],
                 ['Q', 'O', 'Q', 'Q'],
                 ['G', 'Q', 'Q', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BOT': True}
        expected = [[(0, 2), (1, 1), (2, 0)]]
        assert find_length_n_words(3, board, word_dict) == expected

    def test_shared_letters(self):
        board = [['D', 'O', 'T', 'Q'],
                 ['O', 'Q', 'O', 'Q'],
                 ['G', 'Q', 'B', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'DOT': True, 'DOG': True, 'BOT': True}
        expected = [[(0, 0), (1, 0), (2, 0)],
                    [(0, 0), (0, 1), (0, 2)],
                    [(2, 2), (1, 2), (0, 2)]]
        assert sorted(find_length_n_words(3, board, word_dict)) == \
               sorted(expected)

    def test_changed_direction(self):
        board = [['A', 'T', 'R', 'Q'],
                 ['Q', 'L', 'E', 'Q'],
                 ['Q', 'Q', 'B', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'ALBERT': True}
        expected = [[(0, 0), (1, 1), (2, 2), (1, 2), (0, 2),
                                (0, 1)]]
        assert find_length_n_words(6, board, word_dict) == expected

    # Special cases

    def test_not_use_same_letter_twice(self):
        board = [['A', 'T', 'R', 'Q'],
                 ['Q', 'L', 'E', 'Q'],
                 ['Q', 'Q', 'B', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'ALBERTA': True}
        expected = []
        assert find_length_n_words(7, board, word_dict) == expected

    def test_words_not_in_board(self):
        board = [['Q', 'Q', 'Q', 'Q'],
                 ['Q', 'Q', 'Q', 'Q'],
                 ['Q', 'Q', 'B', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'DOT': True, 'DOG': True, 'BOT': True}
        expected = []
        assert find_length_n_words(3, board, word_dict) == expected

    def test_no_words_in_length_n_1(self):
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'O', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BOT': True}
        expected = []
        assert find_length_n_words(2, board, word_dict) == expected

    def test_no_words_in_length_n_2(self):
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'O', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CATH': True, 'DOGH': True, 'BOTH': True}
        expected = []
        assert find_length_n_words(3, board, word_dict) == expected

    def test_n_in_too_big(self):
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'O', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'CAT': True, 'DOG': True, 'BOT': True}
        expected = []
        assert find_length_n_words(1000, board, word_dict) == expected

    def test_finds_correct_length_1(self):
        board = [['Q', 'Q', 'Q', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['Q', 'Q', 'I', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'DOG': True, 'DOGI': True}
        expected = [[(1, 0), (1, 1), (1, 2)]]
        assert find_length_n_words(3, board, word_dict) == expected

    def test_finds_correct_length_2(self):
        board = [['Q', 'Q', 'Q', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['Q', 'Q', 'I', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'DOG': True, 'DOGI': True}
        expected = [[(1, 0), (1, 1), (1, 2), (2, 2)]]
        assert find_length_n_words(4, board, word_dict) == expected

    def test_multiple_options(self):
        board = [['Q', 'O', 'Q', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['Q', 'O', 'Q', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'DOG': True}
        expected_1 = [[(1, 0), (1, 1), (1, 2)]]
        expected_2 = [[(1, 0), (0, 1), (1, 2)]]
        expected_3 = [[(1, 0), (2, 1), (1, 2)]]
        actual = find_length_n_words(3, board, word_dict)
        assert sorted(actual) == sorted(expected_1 + expected_2 + expected_3)

    def test_palindrome(self):
        board = [['Q', 'Q', 'Q', 'Q'],
                 ['B', 'O', 'B', 'Q'],
                 ['Q', 'Q', 'Q', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'BOB': True}
        expected_1 = [[(1, 0), (1, 1), (1, 2)]]
        expected_2 = [[(1, 2), (1, 1), (1, 0)]]
        actual = find_length_n_words(3, board, word_dict)
        assert sorted(actual) == sorted(expected_1 + expected_2)

    def test_single_letter_word(self):
        board = [['Q', 'Q', 'Q', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['Q', 'Q', 'Q', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'D': True, 'O': True, 'G': True}
        expected = [[(1, 0)], [(1, 1)], [(1, 2)]]
        assert sorted(find_length_n_words(1, board, word_dict)) == \
               sorted(expected)

    # def test_n_is_0(self):
    #     board = [['Q', 'Q', 'Q', 'Q'],
    #              ['D', 'O', 'G', 'Q'],
    #              ['Q', 'Q', 'Q', 'Q'],
    #              ['Q', 'Q', 'Q', 'Q']]
    #     word_dict = {'D': True, 'O': True, 'G': True}
    #     expected = []
    #     assert find_length_n_words(0, board, word_dict) == expected

    def test_multi_letter_cells(self):
        board = [['Q', 'Q', 'Q', 'Q'],
                 ['DO', 'GS', 'Q', 'Q'],
                 ['Q', 'Q', 'Q', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'DOGS': True}
        expected = [[(1, 0), (1, 1)]]
        assert find_length_n_paths(2, board, word_dict) == expected

    def test_does_not_split_cells(self):
        board = [['Q', 'Q', 'Q', 'Q'],
                 ['DO', 'GS', 'Q', 'Q'],
                 ['Q', 'Q', 'Q', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = {'DOG': True}
        expected = []
        assert find_length_n_words(2, board, word_dict) == expected

    def test_long_dict(self):
        board = [['C', 'A', 'T', 'Q'],
                 ['D', 'O', 'G', 'Q'],
                 ['B', 'I', 'T', 'Q'],
                 ['Q', 'Q', 'Q', 'Q']]
        word_dict = load_words_dict(file_path("boggle_dict.txt"))
        expected = [[(0, 1), (1, 0), (1, 1)],
                    [(0, 1), (1, 2), (1, 1)],
                    [(2, 0), (2, 1), (1, 0)],
                    [(2, 0), (2, 1), (1, 2)],
                    [(2, 0), (2, 1), (1, 1)],
                    [(2, 0), (2, 1), (2, 2)],
                    [(2, 0), (1, 1), (0, 1)],
                    [(2, 0), (1, 1), (1, 0)],
                    [(2, 0), (1, 1), (1, 2)],
                    [(2, 0), (1, 1), (2, 1)],
                    [(2, 0), (1, 1), (0, 2)],
                    [(2, 0), (1, 1), (2, 2)],
                    [(0, 0), (0, 1), (1, 0)],
                    [(0, 0), (0, 1), (1, 2)],
                    [(0, 0), (0, 1), (0, 2)],
                    [(0, 0), (1, 1), (2, 0)],
                    [(0, 0), (1, 1), (1, 0)],
                    [(0, 0), (1, 1), (1, 2)],
                    [(0, 0), (1, 1), (0, 2)],
                    [(0, 0), (1, 1), (2, 2)],
                    [(1, 0), (0, 1), (1, 2)],
                    [(1, 0), (2, 1), (2, 0)],
                    [(1, 0), (2, 1), (1, 2)],
                    [(1, 0), (2, 1), (2, 2)],
                    [(1, 0), (1, 1), (2, 0)],
                    [(1, 0), (1, 1), (0, 0)],
                    [(1, 0), (1, 1), (1, 2)],
                    [(1, 0), (1, 1), (0, 2)],
                    [(1, 0), (1, 1), (2, 2)],
                    [(1, 2), (0, 1), (1, 0)],
                    [(1, 2), (0, 1), (0, 2)],
                    [(1, 2), (2, 1), (2, 0)],
                    [(1, 2), (2, 1), (1, 0)],
                    [(1, 2), (2, 1), (1, 1)],
                    [(1, 2), (2, 1), (2, 2)],
                    [(1, 2), (1, 1), (0, 1)],
                    [(1, 2), (1, 1), (2, 0)],
                    [(1, 2), (1, 1), (1, 0)],
                    [(1, 2), (1, 1), (0, 2)],
                    [(1, 2), (1, 1), (2, 2)],
                    [(1, 1), (0, 1), (0, 2)],
                    [(1, 1), (2, 0), (2, 1)],
                    [(1, 1), (0, 0), (0, 1)],
                    [(1, 1), (1, 0), (0, 1)],
                    [(0, 2), (0, 1), (1, 0)],
                    [(0, 2), (0, 1), (1, 2)],
                    [(0, 2), (0, 1), (1, 1)],
                    [(2, 2), (2, 1), (1, 0)],
                    [(2, 2), (2, 1), (1, 2)],
                    [(0, 2), (1, 1), (0, 0)],
                    [(2, 2), (1, 1), (0, 0)],
                    [(0, 2), (1, 1), (1, 0)],
                    [(2, 2), (1, 1), (1, 0)],
                    [(0, 2), (1, 1), (1, 2)],
                    [(2, 2), (1, 1), (1, 2)],
                    [(0, 2), (1, 1), (2, 2)],
                    [(2, 2), (1, 1), (0, 2)]]
        assert sorted(find_length_n_words(3, board, word_dict)) == sorted(expected)

    def test_full_dict_random_board(self):
        board = [['T', 'G', 'O', 'T'],
                 ['R', 'D', 'B', 'F'],
                 ['H', 'N', 'U', 'P'],
                 ['N', 'A', 'S', 'N']]
        word_dict = load_words_dict(file_path("boggle_dict.txt"))
        expected_3 = [[(3, 1), (2, 1), (1, 1)],
                      [(3, 1), (2, 1), (3, 0)],
                      [(3, 1), (3, 0), (2, 1)],
                      [(3, 1), (2, 1), (3, 2)],
                      [(3, 1), (3, 2), (2, 3)],
                      [(3, 1), (2, 2), (1, 3)],
                      [(1, 2), (0, 2), (1, 1)],
                      [(1, 2), (0, 2), (0, 1)],
                      [(1, 2), (0, 2), (0, 3)],
                      [(1, 2), (2, 2), (1, 1)],
                      [(1, 2), (2, 2), (2, 1)],
                      [(1, 2), (2, 2), (3, 3)],
                      [(1, 2), (2, 2), (3, 2)],
                      [(1, 1), (0, 2), (1, 2)],
                      [(1, 1), (0, 2), (1, 3)],
                      [(1, 1), (0, 2), (0, 1)],
                      [(1, 1), (0, 2), (0, 3)],
                      [(1, 1), (2, 2), (1, 2)],
                      [(1, 1), (2, 2), (2, 1)],
                      [(1, 1), (2, 2), (3, 3)],
                      [(1, 1), (2, 2), (2, 3)],
                      [(1, 3), (0, 2), (1, 2)],
                      [(1, 3), (0, 2), (0, 1)],
                      [(1, 3), (2, 2), (1, 2)],
                      [(1, 3), (2, 2), (1, 1)],
                      [(1, 3), (2, 2), (2, 1)],
                      [(1, 3), (2, 2), (3, 3)],
                      [(0, 1), (0, 2), (1, 2)],
                      [(0, 1), (0, 2), (1, 1)],
                      [(0, 1), (0, 2), (0, 3)],
                      [(2, 0), (3, 1), (2, 1)],
                      [(2, 0), (3, 1), (3, 0)],
                      [(2, 0), (3, 1), (3, 2)],
                      [(2, 1), (3, 1), (2, 0)],
                      [(3, 0), (3, 1), (2, 0)],
                      [(2, 1), (3, 1), (3, 0)],
                      [(3, 0), (3, 1), (2, 1)],
                      [(2, 1), (3, 1), (3, 2)],
                      [(3, 0), (3, 1), (3, 2)],
                      [(2, 1), (2, 2), (1, 2)],
                      [(3, 3), (2, 2), (1, 2)],
                      [(2, 1), (2, 2), (3, 3)],
                      [(3, 3), (2, 2), (2, 1)],
                      [(2, 1), (2, 2), (3, 2)],
                      [(3, 3), (2, 2), (3, 2)],
                      [(0, 2), (1, 3), (0, 3)],
                      [(2, 3), (2, 2), (1, 2)],
                      [(2, 3), (2, 2), (1, 1)],
                      [(2, 3), (2, 2), (2, 1)],
                      [(2, 3), (2, 2), (3, 3)],
                      [(2, 3), (2, 2), (3, 2)],
                      [(3, 2), (3, 1), (2, 1)],
                      [(3, 2), (3, 1), (3, 0)],
                      [(3, 2), (3, 1), (2, 2)],
                      [(3, 2), (2, 2), (1, 2)],
                      [(3, 2), (2, 2), (1, 1)],
                      [(3, 2), (2, 2), (2, 1)],
                      [(3, 2), (2, 2), (3, 3)],
                      [(3, 2), (2, 2), (2, 3)],
                      [(0, 3), (0, 2), (1, 1)],
                      [(0, 3), (0, 2), (0, 1)],
                      [(2, 2), (1, 1), (0, 2)],
                      [(2, 2), (1, 3), (0, 2)],
                      [(2, 2), (2, 1), (3, 2)],
                      [(2, 2), (3, 3), (3, 2)],
                      [(2, 2), (2, 3), (3, 2)]]
        expected_4 = [[(3, 1), (3, 0), (2, 1), (3, 2)],
                      [(3, 1), (2, 1), (2, 2), (3, 2)],
                      [(1, 2), (2, 2), (1, 1), (0, 2)],
                      [(1, 2), (2, 2), (1, 3), (0, 2)],
                      [(1, 2), (2, 2), (2, 1), (3, 1)],
                      [(1, 2), (2, 2), (2, 1), (1, 1)],
                      [(1, 2), (2, 2), (2, 1), (3, 0)],
                      [(1, 2), (2, 2), (2, 1), (3, 2)],
                      [(1, 2), (2, 2), (3, 3), (3, 2)],
                      [(1, 1), (2, 2), (3, 1), (2, 1)],
                      [(1, 1), (2, 2), (3, 1), (3, 0)],
                      [(1, 1), (2, 2), (2, 1), (3, 2)],
                      [(1, 1), (2, 2), (3, 3), (3, 2)],
                      [(1, 1), (2, 2), (2, 3), (3, 2)],
                      [(1, 3), (2, 2), (2, 1), (1, 1)],
                      [(1, 3), (2, 2), (2, 1), (3, 2)],
                      [(1, 3), (2, 2), (3, 3), (3, 2)],
                      [(2, 0), (3, 1), (2, 1), (1, 1)],
                      [(2, 0), (3, 1), (3, 2), (2, 3)],
                      [(2, 0), (3, 1), (2, 2), (1, 1)],
                      [(2, 0), (3, 1), (2, 2), (1, 3)],
                      [(2, 0), (3, 1), (2, 2), (2, 1)],
                      [(2, 0), (3, 1), (2, 2), (3, 3)],
                      [(3, 0), (3, 1), (2, 1), (3, 2)],
                      [(2, 1), (2, 2), (3, 3), (3, 2)],
                      [(3, 3), (2, 2), (2, 1), (3, 2)],
                      [(2, 3), (2, 2), (2, 1), (3, 1)],
                      [(2, 3), (2, 2), (2, 1), (3, 2)],
                      [(2, 3), (2, 2), (3, 3), (3, 2)],
                      [(3, 2), (3, 1), (2, 1), (1, 1)],
                      [(3, 2), (2, 1), (2, 2), (1, 2)],
                      [(3, 2), (3, 3), (2, 2), (1, 2)],
                      [(3, 2), (2, 3), (2, 2), (1, 1)],
                      [(3, 2), (2, 3), (2, 2), (2, 1)],
                      [(3, 2), (2, 3), (2, 2), (3, 3)],
                      [(3, 2), (2, 2), (2, 1), (3, 0)],
                      [(0, 3), (0, 2), (1, 3), (2, 2)],
                      [(2, 2), (2, 1), (1, 1), (0, 2)]]
        expected_5 = [ [(1, 2), (2, 2), (2, 1), (3, 1), (3, 2)],
                       [(1, 2), (2, 2), (2, 1), (1, 1), (2, 0)],
                       [(1, 2), (2, 2), (2, 1), (1, 1), (0, 0)],
                       [(1, 1), (2, 2), (3, 1), (2, 1), (3, 2)],
                       [(2, 0), (3, 1), (2, 2), (2, 1), (3, 2)],
                       [(2, 0), (3, 1), (2, 2), (3, 3), (3, 2)],
                       [(3, 0), (3, 1), (2, 1), (1, 1), (2, 2)],
                       [(2, 3), (2, 2), (2, 1), (3, 1), (3, 2)],
                       [(3, 2), (2, 2), (2, 1), (3, 0), (3, 1)],
                       [(0, 3), (0, 2), (1, 3), (2, 2), (3, 2)]]
        expected_6 = [
            [(3, 0), (3, 1), (2, 1), (1, 1), (2, 2), (3, 2)],
            [(3, 0), (2, 0), (3, 1), (2, 1), (1, 1), (2, 2)],
            [(3, 2), (3, 1), (3, 0), (2, 1), (2, 2), (2, 3)],
            [(3, 2), (2, 2), (2, 1), (1, 1), (0, 2), (0, 1)],
            [(3, 2), (2, 2), (2, 1), (3, 0), (3, 1), (2, 0)],
            [(2, 2), (2, 1), (2, 0), (3, 1), (3, 2), (2, 3)]]
        assert sorted(find_length_n_words(3, board, word_dict)) == sorted(expected_3)
        assert sorted(find_length_n_words(4, board, word_dict)) == sorted(expected_4)
        assert sorted(find_length_n_words(5, board, word_dict)) == sorted(expected_5)
        assert sorted(find_length_n_words(6, board, word_dict)) == sorted(expected_6)
