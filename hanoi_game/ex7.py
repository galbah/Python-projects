####################
# NAME: Gal Bahary #
# ID: 207297011    #
# Intro2CS ex7     #
####################

from ex7_helper import *
from typing import Any, List


def _mult_helper(x: float, y: int, z: int) -> float :
    if z == y :
        return x
    return add(x, _mult_helper(x, y, int(add(z, 1))))


def mult(x: float, y: int) -> float : # retruns the result of x*y
    if y == 0 or x == 0 :
        return 0
    z = 1
    return _mult_helper(x, y, z)


def is_even(n: int) -> bool : # checks if n is even
    if n == 0 :
        return True
    elif n == 1 :
        return False
    n = subtract_1(subtract_1(n))
    return is_even(n)


def log_mult(x: float, y: int) -> float : # calculates the results of x*y in a O(logn) run time
    if y == 0 or x == 0 :
        return 0
    z = log_mult(x, divide_by_2(y))
    if is_odd(y) :
        return add(x, add(z, z))
    else :
        return add(z, z)


def _is_power_helper(b: int ,new_b: int , x: int) -> int :
    if new_b >= x :
        return new_b
    return _is_power_helper(b, int(log_mult(b,new_b)), x)


def is_power(b: int, x: int) -> bool : # check if there is a number n that b**n = x
    if x == 1 :
        return True
    if (b == 1 and x != 1) or (b == 0 and x != 0):
        return False
    if x == _is_power_helper(b, b, x) :
        return True
    else :
        return False


def _reverse_helper(string: str, index : int, rev_str : str) -> str :
    if index == len(string) :
        return rev_str
    return append_to_end(_reverse_helper(string, index+1, rev_str), string[index])


def reverse(s: str) -> str :   # return the string from the input in the reverse order
    index = 0
    rev_str = ""
    return _reverse_helper(s, index, rev_str)



#-------------------- part 2 ---------------------------#


def play_hanoi(Hanoi: Any, n: int, src: Any, dst: Any, temp: Any) -> None :
    # solves the hanoi game
    if n <= 0 :
        return

    if n == 1 :
        Hanoi.move(src, dst)
        return

    play_hanoi(Hanoi, n-1, src, temp, dst)
    Hanoi.move(src, dst)
    play_hanoi(Hanoi, n-1, temp, dst, src)


def _check_how_much_ones(n: int) -> int :
    #returns the number of appearances of 1's in a specific number
    if n == 1 :
        return 1
    elif n < 10 :
        return 0
    elif n % 10 == 1 :
        return 1 + _check_how_much_ones(n//10)
    else:
        return _check_how_much_ones(n//10)

def number_of_ones(n: int) -> int :
    # returns the sum of appearances of 1's in all numbers from 1 to n
    if n == 1 :
        return 1
    if n == 0 or n is None:
        return 0
    num_of_1 = _check_how_much_ones(n)
    return num_of_1 + number_of_ones(n-1)


def _compare_1d_lists(l1: List[int], l2: List[int]) -> bool :
    # returns True if 2 lists are even and False otherwise
    if l1 == [] and l2 == []:
        return True
    if len(l1) == 1 and len(l2) == 1 :
        if l1[0] == l2[0] :
            return True
        else :
            return False
    if len(l1) != len(l2) :
        return False
    if l1[0] == l2[0] :
        del l1[0]
        del l2[0]
        return _compare_1d_lists(l1, l2)
    else:
        return False

def compare_2d_lists(l1: List[List[int]], l2: List[List[int]]) -> bool :
    #compares 2 2d lists and returns True if they are even and False otherwise
    if l1 == [] and l2 == [] :
        return True
    if len(l1) == 1 and len(l2) == 1 :
        if _compare_1d_lists(l1[0], l2[0]) :
            return True
        else :
            return False
    if len(l1) != len(l2) :
        return False
    if _compare_1d_lists(l1[0], l2[0]) :
        del l1[0]
        del l2[0]
        return compare_2d_lists(l1, l2)
    else:
        return False


def _list_copy(lst: List[Any]) -> List[Any] :
    # receives a list and returns a deep copy of the list
    new_lst = []
    for i in range(len(lst)) :
        if isinstance(lst[i], list) :
            new_lst.append(_list_copy(lst[i]))
        else:
            new_lst.append(lst[i])
    return new_lst

def _magic_list_helper(n: int, lst: List[Any]) -> List[Any] :
    # creates a magic list
    if n == 0 :
        return []
    lst.append(_magic_list_helper(int(n)-1, lst))
    return _list_copy(lst)

def magic_list(n: int) -> List[Any] :
    #receives a number and creat the magic list in the length of the number
    lst: list[Any] = []
    mag_lst = _magic_list_helper(n, lst)
    return mag_lst