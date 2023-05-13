from ex7 import *


def test_mult():
    # zero multiplication
    assert mult(0, 5) == 0
    assert mult(15, 0) == 0

    # negative multiplication
    assert mult(-7, 3) == -21

    # symmetricity
    assert mult(1, 1) == 1
    assert mult(3, 1) == 3
    assert mult(1, 3) == 3


def test_is_even():
    # zero
    assert is_even(0) == True

    # positive
    assert is_even(3) == False
    assert is_even(10) == True
    assert is_even(1) == False

    # negative
    assert is_even(-112) == True
    assert is_even(-1) == False


def test_log_mult():
    # zero multiplication
    assert log_mult(0, 5) == 0
    assert log_mult(15, 0) == 0

    # negative multiplication
    assert log_mult(-7, 3) == -21

    # symmetricallity
    assert log_mult(1, 1) == 1
    assert log_mult(3, 1) == 3
    assert log_mult(1, 3) == 3


def test_is_power():
    assert is_power(2, 16) == True
    assert is_power(3, 17) == False
    assert is_power(1, 1) == True
    assert is_power(1, 4) == False
    assert is_power(0, 10) == False
    assert is_power(5, 1) == True
    assert is_power(5, 0) == False
    assert is_power(2, 8) == True
    assert is_power(3, 6) == False
    assert is_power(3, 9) == True
    assert is_power(4, 4) == True


def test_reverse():
    assert reverse('') == ''
    assert reverse('intro') == 'ortni'
    assert reverse('hel') == 'leh'
    assert reverse('123') == '321'
    assert reverse(reverse('fdsafsace')) == 'fdsafsace'


def test_number_of_ones():
    assert number_of_ones(13) == 6
    assert number_of_ones(0) == 0
    assert number_of_ones(1) == 1
    assert number_of_ones(9) == 1
    assert number_of_ones(10) == 2
    assert number_of_ones(11) == 4
    assert number_of_ones(30) == 13


def test_compare_2d_lists():
    assert compare_2d_lists([[1, 2], [4, 5, 6]], [[1, 2], [4, 5, 8]]) == False
    assert compare_2d_lists([[1, 4], [2, 2, 2]], [[1, 4], [2, 2]]) == False
    assert compare_2d_lists([[1, 4], [2, 2, 2]], [[1, 4], [2, 2, 2]]) == True
    assert compare_2d_lists([[1, 4], [2, 2, 2]], [[1, 4], [1, 2, 2]]) == False
    assert compare_2d_lists([[1, 4], [2, 2, 2], []], [[1, 4], [2, 2, 2]]) == False
    assert compare_2d_lists([[1, 4], [2, 2, 2], [0]], [[1, 4], [2, 2, 2]]) == False
    assert compare_2d_lists([[]], [[]]) == True


def test_magic_list():
    assert magic_list(0) == []
    assert magic_list(1) == [[]]
    assert magic_list(2) == [[], [[]]]
    assert magic_list(3) == [[], [[]], [[], [[]]]]
    assert magic_list(4) == [[], [[]], [[], [[]]], [[], [[]], [[], [[]]]]]
    assert magic_list(5) == [[], [[]], [[], [[]]], [[], [[]], [[], [[]]]],
                             [[], [[]], [[], [[]]], [[], [[]], [[], [[]]]]]]
