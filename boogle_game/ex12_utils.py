import boggle_board_randomizer
import itertools

BOARD_SIZE = boggle_board_randomizer.BOARD_SIZE


def is_valid_path(board, path, words):
    """if the path is valid, returns the word that is created by the path, None otherwise"""
    if len(path) != len(set(path)):
        return None  # --- not legal path, a coordinate used more than once ---
    cur_word = ''
    cur_path = []
    for i in range(len(path)):
        coor = path[i]
        cur_path.append(coor)
        if _check_current_coor(coor, i, path, cur_path):
            cur_word += str(board[coor[0]][coor[1]])
        else:
            return None

    if cur_word in words:
        return cur_word
    else:
        return None  # --- not legal word ---


def _check_current_coor(coor, i, path, cur_path):
    """if coordinate is in board borders and the next one is a neighbor returns True, otherwise False"""
    if i == len(path) - 1:
        if _check_in_borders(coor):
            return True
    elif _check_in_borders(coor):
        if path[i + 1] in get_neighbors_coors(coor[0], coor[1], cur_path):
            return True
    return False


def _check_in_borders(coor):
    """True if coordinate is in board border, False otherwise"""
    if 0 <= coor[0] < BOARD_SIZE and 0 <= coor[1] < BOARD_SIZE:
        return True
    return False


def find_length_n_paths(n, board, words):
    """return all paths in length n that contains words from words list"""
    if n < 2:
        return []

    all_paths = []
    optional_words = []
    for word in words:
        if n <= len(word) <= n + 1:
            optional_words.append(word)

    if optional_words == []:
        return []

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            _creat_pathes_from_point(board, row, col, n, [], all_paths, optional_words)
    return all_paths


def _creat_pathes_from_point(board, row, col, n, cur_path, all_paths, words):
    """checks all paths available from a coordinate. if path is valid, adds it to all_paths"""
    if len(cur_path) == n :
        if _check_word_by_coors(board, cur_path, words):
            if cur_path not in all_paths:
                all_paths.append(cur_path)
                return True
        return False

    cur_path.append((row, col))
    new_coors = get_neighbors_coors(row, col, cur_path)
    if not new_coors:
        return False
    for coor in new_coors:
        if _creat_pathes_from_point(board, coor[0], coor[1], n, cur_path[:], all_paths, words):
            break


def _check_word_by_coors(board, path, words):
    """True if the word in coordinates of the path is valid, False otherwise"""
    word = ''
    for coor in path:
        word += board[coor[0]][coor[1]]
    if word in words:
        return True
    return False


def get_neighbors_coors(row, col, path):
    """returns all coordinates of neighbors that are in board borders"""
    rows = [row, row + 1, row - 1]
    cols = [col, col + 1, col - 1]
    optional_coors = list(itertools.product(rows, cols))  # all combinations between rows & cols
    neighbors_coors = []
    for coor in optional_coors:
        if coor not in path and _check_in_borders(coor):
            neighbors_coors.append(coor)
    return neighbors_coors


def find_length_n_words(n, board, words):
    """returns all paths that creates words from list in length n"""
    n_words = []
    for word in words:
        if len(word) == n:
            n_words.append(word)

    all_paths = []
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            _find_words_from_point(board, row, col, n, '', all_paths, n_words, [])
    return all_paths


def _find_words_from_point(board, row, col, n, cur_word, all_paths, words, used_coors):
    """findes every word in length n that starts in given row and col, and adds it to all paths"""
    coor = (row, col)
    cur_path = used_coors[:] + [coor]
    cur_word += board[row][col]
    if not _check_in_borders(coor):
        return
    if n == len(cur_word) :
        if cur_word in words and cur_path not in all_paths:
            all_paths.append(cur_path)
        return

    new_coors = get_neighbors_coors(row, col, cur_path)
    for coor in new_coors:
        _find_words_from_point(board, coor[0], coor[1], n, cur_word, all_paths, words, cur_path)


def max_score_paths(board, words):
    """return all paths that makes the maximum score in game"""
    longest_word = 0
    for word in words:
        if len(word) > longest_word:
            longest_word = len(word)
    score_dict = {}
    for i in range(2, longest_word + 1):
        all_paths = find_length_n_paths(i, board, words)
        for path in all_paths:
            cur_word = _get_word(path, board)
            score_dict[cur_word] = path
    return list(score_dict.values())


def _get_word(path, board):
    """returns the word created by adding the items in the path given"""
    word = ''
    for coor in path:
        word += board[coor[0]][coor[1]]
    return word
