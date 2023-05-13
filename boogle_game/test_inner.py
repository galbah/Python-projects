from ex12_utils import *


# def test_load_words_dict():
#     assert load_words_dict('./Data/words_dict1.txt') == {'ABC': True, 'RGAC': True, 'YTE': True}
#     assert load_words_dict('./Data/words_dict2.txt') == {'aDs': True}
#     assert load_words_dict('./Data/words_dict3.txt') == {'GtR': True, 'LoK': True}

def test_is_valid_path():
    board = [['a','b','c','d'],['a','b','c','d'],['a','b','c','d'], ['h', 'j', 'k', 'l']]
    path = [(0,0),(1,1)]
    words = {'ab':True,'cc': True}
    assert is_valid_path(board, path, words) == 'ab'

    board = [['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd'], ['h', 'j', 'k', 'l']]
    path = [(0, 0), (1, 1),(1,0),(0,0)]
    words = {'ab': True, 'cc': True, 'abaa': True}
    assert is_valid_path(board, path, words) == None

    board = [['a','b','c','d'],['a','b','c','d'],['a','b','c','d'], ['h', 'j', 'k', 'l']]
    path = [(0,0),(0,1)]
    words = {'ab':True,'cc': True}
    assert is_valid_path(board, path, words) == 'ab'

    board = [['a','b','c','d'],['a','b','c','d'],['a','b','c','d'], ['h', 'j', 'k', 'l']]
    path = [(0,0),(1,0)]
    words = {'ab':True,'aa': True}
    assert is_valid_path(board, path, words) == 'aa'

    board = [['a','b','c','d'],['a','b','c','d'],['a','b','c','d'], ['h', 'j', 'k', 'l']]
    path = [(0,0),(1,1), (5,0)]
    words = {'ab':True,'cc': True}
    assert is_valid_path(board, path, words) == None

    board = [['a','b','c','d'],['a','b','c','d'],['a','b','c','d'], ['h', 'j', 'k', 'l']]
    path = [(0,5),(1,1)]
    words = {'ab':True,'cc': True}
    assert is_valid_path(board, path, words) == None

    board = [['a','b','c','d'],['t','r','g','m'],['x','y','z','n'], ['h', 'j', 'k', 'l']]
    path = [(0,0),(1,1),(1,2)]
    words = {'ab':True,'cc': True, 'arg': True}
    assert is_valid_path(board, path, words) == 'arg'

    board = [['a','b','c','d'],['t','r','g','m'],['x','y','z','n'], ['h', 'j', 'k', 'l']]
    path = [(0,0),(1,1),(1,2),(1,3),(1,4)]
    words = {'ab':True,'cc': True, 'arg': True}
    assert is_valid_path(board, path, words) == None

    board = [['a','b','c','d'],['t','r','g','m'],['x','y','z','n'], ['h', 'j', 'k', 'l']]
    path = [(0,0),(1,1),(1,3)]
    words = {'ab':True,'cc': True, 'arg': True}
    assert is_valid_path(board, path, words) == None

    board = [['a','b','c','d'],['t','r','g','m'],['x','y','z','n'], ['h', 'j', 'k', 'l']]
    path = [(0,0),(1,1),(2,2)]
    words = {'ab':True,'cc': True, 'arg': True}
    assert is_valid_path(board, path, words) == None

    board = [['a','b','c','d'],['t','r','g','m'],['x','y','z','n'] ,['h', 'j', 'k', 'l']]
    path = [(0,0),(1,1),(2,2),(2,0)]
    words = {'ab':True,'cc': True, 'arg': True}
    assert is_valid_path(board, path, words) == None

    board = [['a', 'b', 'c', 'd'], ['t', 'r', 'g', 'm'], ['x', 'y', 'z', 'n'], ['h', 'j', 'k', 'l']]
    path = [(0, 0), (1, 1), (0, 0)]
    words = {'ab': True, 'cc': True, 'arg': True}
    assert is_valid_path(board, path, words) == None

    board = [['a', 'b', 'c', 'd'], ['t', 'r', 'g', 'm'], ['x', 'y', 'z', 'n'], ['h', 'j', 'k', 'l']]
    path = [(0, 0), (1, 1), (2, 2),(2,1), (1,0)]
    words = {'ab': True, 'cc': True, 'arg': True, 'arzyt':True}
    assert is_valid_path(board, path, words) == 'arzyt'

    board = [['a', 'b', 'c', 'd'], ['qe', 'r', 'g', 'm'], ['x', 'y', 'z', 'n'], ['h', 'j', 'k', 'l']]
    path = [(0, 0), (1, 1), (2, 2), (2, 1), (1, 0)]
    words = {'ab': True, 'cc': True, 'arg': True, 'arzyt': True}
    assert is_valid_path(board, path, words) == None

    board = [['a', 'b', 'c', 'd'], ['qe', 'r', 'g', 'm'], ['x', 'y', 'z', 'n'], ['h', 'j', 'k', 'l']]
    path = [(0, 0), (1, 1), (2, 2), (2, 1), (1, 0)]
    words = {'ab': True, 'cc': True, 'arg': True, 'arzyqe': True}
    assert is_valid_path(board, path, words) == 'arzyqe'

    board = [['a', 'b', 'c', 'd'], ['qe', 'r', 'g', 'm'], ['x', 'y', 'z', 'n'], ['h', 'j', 'k', 'l']]
    path = [(1,0)]
    words = {'ab': True, 'cc': True, 'qe': True, 'arzyqe': True}
    assert is_valid_path(board, path, words) == 'qe'

    board = [['a', 'b', 'c', 'd'], ['qe', 'r', 'g', 'm'], ['x', 'y', 'z', 'n'], ['h', 'j', 'k', 'l']]
    path = []
    words = {'ab': True, 'cc': True, 'qe': True, 'arzyqe': True}
    assert is_valid_path(board, path, words) == None

def test_find_length_n_words():
    board = [['a', 'b', 'c', 'd'], ['qe', 'r', 'g', 'm'], ['x', 'y', 'z', 'n'], ['h', 'j', 'k', 'l']]
    words = {'ab': True, 'cc': True, 'qe': True, 'arzyqe': True}
    assert sorted(find_length_n_words(0, board, words)) == sorted([])

    board = [['a', 'b', 'c', 'd'], ['qe', 'r', 'g', 'm'], ['x', 'y', 'z', 'n'], ['h', 'j', 'k', 'l']]
    words = {'ab': True, 'cc': True, 'qe': True, 'arzyqe': True}
    assert sorted(find_length_n_words(1, board, words)) == sorted([])

    board = [['a', 'b', 'c', 'd'], ['qe', 'r', 'g', 'm'], ['x', 'y', 'z', 'n'], ['h', 'j', 'k', 'l']]
    words = {'ab': True, 'cc': True, 'qe': True, 'arzyqe': True}
    assert sorted(find_length_n_words(2, board, words)) == sorted([[(0,0),(0,1)],[(1,0)]])

    board = [['a', 'b', 'c', 'd'], ['qe', 'r', 'g', 'm'], ['x', 'y', 'z', 'n'], ['h', 'j', 'k', 'l']]
    words = {'ab': True, 'cc': True, 'qe': True, 'arzyqe': True}
    assert sorted(find_length_n_words(6, board, words)) == sorted([[(0, 0), (1, 1), (2,2),(2,1),(1,0)]])

    board = [['a', 'b', 'c', 'd'], ['qe', 'r', 'g', 'm'], ['x', 'y', 'z', 'n'], ['h', 'j', 'k', 'l']]
    words = {'ab': True, 'cc': True, 'qe': True, 'bqerz': True, 'abcde': True}
    assert sorted(find_length_n_words(5, board, words)) == sorted(
        [[(0, 1), (1, 0), (1, 1), (2, 2)]])

    board = [['a', 'b', 'c', 'd'], ['q', 'r', 'g', 'm'], ['x', 'y', 'z', 'n'], ['h', 'j', 'k', 'l']]
    words = {'ab': True, 'cc': True, 'qe': True, 'bqxrz': True, 'abcde': True}
    assert sorted(find_length_n_words(5, board, words)) == sorted(
        [[(0, 1), (1, 0),(2,0), (1, 1), (2, 2)]])

    board = [['a', 'b', 'c', 'd'], ['q', 'r', 'g', 'm'], ['x', 'y', 'z', 'n'], ['h', 'j', 'k', 'l']]
    words = {'ab': True, 'cc': True, 'qe': True, 'bqxrz': True, 'dmnlk': True}
    assert sorted(find_length_n_words(5, board, words)) == sorted(
        [[(0, 1), (1, 0), (2, 0), (1, 1), (2, 2)], [(0,3),(1,3),(2,3),(3,3),(3,2)]])

    board = [['a', 'b', 'c', 'd'], ['qe', 'r', 'g', 'm'], ['x', 'y', 'z', 'n'], ['h', 'j', 'k', 'l']]
    words = {'ab': True, 'cc': True, 'qe': True, 'bqerz': True, 'aryqe': True,'abcd':True}
    assert sorted(find_length_n_words(5, board, words)) == sorted(
        [[(0,0),(1,1),(2,1),(1,0)],[(0, 1), (1, 0), (1, 1), (2, 2)]])

    board = [['a', 'b', 'c', 'd'], ['e', 'r', 'f', 't'], ['a', 'b', 'c', 'd'], ['l', 'o', 'u', 'r']]
    words = {'ab': True, 'cc': True, 'qe': True, 'bqerz': True, 'aryqe': True, 'abcd': True}
    assert sorted(find_length_n_words(4, board, words)) == sorted(
        [[(0, 0), (0, 1), (0, 2), (0, 3)],[(2,0),(2,1),(2,2),(2,3)]])

    board = [['a', 'b', 'c', 'd'], ['e', 'r', 'f', 't'], ['a', 'b', 'c', 'd'], ['e', 'r', 'f', 't']]
    words = {'ab': True, 'cc': True, 'qe': True, 'bqerz': True, 'aryqe': True, 'abcd': True, 'erft': True}
    assert sorted(find_length_n_words(4, board, words)) == sorted(
        [[(0, 0), (0, 1), (0, 2), (0, 3)], [(2, 0), (2, 1), (2, 2), (2, 3)], [(1,0),(1,1),(1,2),(1,3)], [(3,0),(3,1),(3,2),(3,3)]])

    board = [['a', 'dr', 'c', 'd'], ['qe', 'r', 'g', 'm'], ['x', 'y', 'z', 'n'], ['h', 'j', 'k', 'l']]
    words = {'ab': True, 'cc': True, 'qe': True, 'qedr': True, 'drqe': True, 'adrcrqed': True}
    assert sorted(find_length_n_words(4, board, words)) == sorted(
        [[(0,1),(1,0)], [(1,0),(0,1)]])

    board = [['a', 'dr', 'c', 'd'], ['qe', 'r', 'g', 'm'], ['x', 'y', 'z', 'n'], ['h', 'j', 'k', 'l']]
    words = {'ab': True, 'cc': True, 'qe': True, 'qedr': True, 'drqe': True, 'adrcrqex': True}
    assert sorted(find_length_n_words(8, board, words)) == sorted(
        [[(0, 0), (0, 1),(0,2),(1,1),(1,0),(2,0)]])

    board = [['a', 'dr', 'c', 'd'], ['qe', 'r', 'g', 'm'], ['x', 'y', 'z', 'n'], ['h', 'j', 'k', 'l']]
    words = {'ab': True, 'cc': True, 'qe': True, 'qedr': True, 'drqe': True, 'adrcrqea': True}
    assert sorted(find_length_n_words(7, board, words)) == sorted(
        [])

test_find_length_n_words()
test_is_valid_path()