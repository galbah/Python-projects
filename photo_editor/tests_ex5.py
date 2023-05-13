##############################################################################
# How to run:
# Place in same folder as cartoonify.py
# Run the tests. Recommended to use PyTest but not necessary
# Disclaimer: This does not test all edge cases, nor does it test full images,
# parameter inputs, use of ex5_helper functions.
# THIS ONLY TESTS THE PRIMARY FUNCTIONS OF cartoonify.py
# These tests allow for rounding errors (+-1)
# The best way to test for full images is simply to run your own program
# You can quickly edit the configurations with PyCharm by selecting
# The downwards arrow next to cartoonify.py and add your params
# Everything is straightforward so I added no documentation
##############################################################################
from cartoonify import *


def in_margin(item1, item2):
    """
    checks if all int are within 1 of their corresponding indexes in the
    given items, used to account for rounding errors. Solved recursively
    :param item1: either a list, or an int
    :param item2: either a list, or an int
    :return: True if all ints are within 1 of their corresponding index
             False otherwise
    """
    if type(item1) == int:
        if abs(item1 - item2) <= 1:
            return True
        else:
            return False
    if type(item1) == list:
        for i, x in enumerate(item1):
            if not in_margin(x, item2[i]):
                return False
        return True
    else:
        print(TypeError)


def test_separate_channels():
    example1 = [[[1, 2]]]
    sep1 = separate_channels(example1)
    assert sep1 == [[[1]], [[2]]]
    example1[0][0][0] = 0
    assert sep1 == [[[1]], [[2]]]
    example2 = [[[170, 20, 35], [45, 154, 161], [175, 28, 9]],
                [[251, 210, 134], [74, 105, 46], [79, 183, 139]]]
    result2 = [[[170, 45, 175], [251, 74, 79]],
               [[20, 154, 28], [210, 105, 183]],
               [[35, 161, 9], [134, 46, 139]]]
    sep2 = separate_channels(example2)
    assert sep2 == result2


def test_combine_channels():
    example1 = [[[1]], [[2]]]
    com1 = combine_channels(example1)
    example1[0][0][0] = 0
    assert com1 == [[[1, 2]]]
    example2 = [[[170, 45, 175], [251, 74, 79]],
                [[20, 154, 28], [210, 105, 183]],
                [[35, 161, 9], [134, 46, 139]]]
    result2 = [[[170, 20, 35], [45, 154, 161], [175, 28, 9]],
               [[251, 210, 134], [74, 105, 46], [79, 183, 139]]]
    com2 = combine_channels(example2)
    assert result2 == com2


def test_rbg2grayscale():
    example1 = [[[100, 180, 240]]]
    gray1 = RGB2grayscale(example1)
    example1[0][0][0] = 0
    assert in_margin(gray1, [[163]])
    example2 = [[[170, 20, 35], [45, 154, 161], [175, 28, 9]],
                [[251, 210, 134], [74, 105, 46], [79, 183, 139]]]
    result2 = [[67, 122, 70], [214, 89, 147]]
    gray2 = RGB2grayscale(example2)
    assert in_margin(gray2, result2)


def test_blur_kernel():
    blur3 = [[1 / 9 for _ in range(3)] for _ in range(3)]
    assert blur_kernel(3) == blur3
    blur5 = [[1 / 25 for _ in range(5)] for _ in range(5)]
    assert blur_kernel(5) == blur5


def test_apply_kernel():
    example1 = [[0, 128, 255]]
    blurred1 = apply_kernel(example1, blur_kernel(3))
    example1[0][0] = 1
    assert in_margin([[14, 128, 241]], blurred1)
    example2 = [[67, 122, 70], [214, 89, 147]]
    result2 = [[79, 121, 82], [191, 96, 140]]
    blurred2 = apply_kernel(example2, blur_kernel(5))
    assert in_margin(result2, blurred2)
    kernel = [[0.01, 0.02, 0.03], [0.04, 0.05, 0.06], [0.07, 0.08, 0.09]]
    blurred3 = apply_kernel(example2, kernel)
    result3 = [[47, 56, 41], [83, 48, 62]]
    assert in_margin(result3, blurred3)


def test_bilinear_interpolation():
    example1 = [[0, 64], [128, 255]]
    assert bilinear_interpolation(example1, 0, 0) == 0
    assert bilinear_interpolation(example1, 1, 1) == 255
    assert in_margin(bilinear_interpolation(example1, 0.5, 0.5), 112)
    assert in_margin(bilinear_interpolation(example1, 0.5, 1), 160)
    example2 = [[67, 122, 70], [214, 89, 147]]
    assert in_margin(bilinear_interpolation(example2, 1.3, 0.8), 114)


def test_resize():
    example1 = [[67, 122, 70], [214, 89, 147]]
    result1 = [[67, 100, 112, 80, 70], [126, 116, 107, 102, 101], [185, 131, 103, 124, 132], [214, 139, 101, 135, 147], [214, 139, 101, 135, 147]]
    assert in_margin(result1, resize(example1, 5, 5))
    example2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    result2 = [[1, 3], [6, 8], [12, 14]]
    assert in_margin(result2, resize(example2, 3, 2))

#
def test_rotate_90():
    example1 = [[1, 2, 3], [4, 5, 6]]
    right1 = [[4, 1], [5, 2], [6, 3]]
    left1 = [[3, 6], [2, 5], [1, 4]]
    assert rotate_90(example1, 'R') == right1
    assert rotate_90(example1, 'L') == left1
    example2 = [[[170, 20, 35], [45, 154, 161], [175, 28, 9]],
                [[251, 210, 134], [74, 105, 46], [79, 183, 139]]]
    result2 = [[[251, 210, 134], [170, 20, 35]],
               [[74, 105, 46], [45, 154, 161]],
               [[79, 183, 139], [175, 28, 9]]]
    result3 = [[[175, 28, 9], [79, 183, 139]],
               [[45, 154, 161], [74, 105, 46]],
               [[170, 20, 35], [251, 210, 134]]]
    right2 = rotate_90(example2, 'R')
    left2 = rotate_90(example2, 'L')
    assert right2 == result2
    assert left2 == result3


def test_get_edges():
    example1 = [[200, 50, 200]]
    edge1 = get_edges(example1, 3, 3, 10)
    assert edge1 == [[255, 0, 255]]
    example2 = [[67, 122, 70], [214, 89, 147]]
    result2 = [[0, 255, 0], [255, 255, 255]]
    assert get_edges(example2, 3, 5, 5) == result2
    example3 = [[67, 94, 122, 96, 70],
                [104, 109, 114, 102, 89],
                [140, 123, 106, 107, 108],
                [177, 137, 97, 112, 128],
                [214, 152, 89, 118, 147]]
    result3 = [[0, 0, 255, 255, 0],
               [255, 255, 255, 255, 255],
               [255, 255, 0, 255, 255],
               [255, 255, 0, 255, 255],
               [255, 255, 0, 255, 255]]
    assert get_edges(example3, 1, 3, 5) == result3


def test_quantize():
    example1 = [[0, 50, 100], [150, 200, 250]]
    result1 = [[0, 32, 96], [128, 191, 223]]
    quant1 = quantize(example1, 8)
    example1[0][0] = 0
    assert in_margin(quant1, result1)
    example2 = [[67, 122, 70], [214, 89, 147]]
    result2 = [[66, 120, 69], [212, 87, 145]]
    assert in_margin(quantize(example2, 100), result2)


def test_quantize_colored_image():
    example1 = [[[170, 20, 35], [45, 154, 161], [175, 28, 9]],
                [[251, 210, 134], [74, 105, 46], [79, 183, 139]]]
    result1 = [[[159, 0, 32], [32, 128, 159], [159, 0, 0]],
               [[223, 191, 128], [64, 96, 32], [64, 159, 128]]]
    assert in_margin(quantize_colored_image(example1, 8), result1)
    example2 = [[[50, 100, 150]]]
    result2 = [[[32, 96, 128]]]
    assert in_margin(quantize_colored_image(example2, 8), result2)
    example3 = [[[1, 10], [2, 20], [3, 30], [4, 40]],
                [[5, 50], [6, 60], [7, 70], [8, 80]],
                [[9, 90], [10, 100], [11, 110], [12, 120]],
                [[13, 130], [14, 140], [15, 150], [16, 160]]]
    result3 = [[[0, 8], [0, 20], [0, 28], [4, 40]],
               [[4, 48], [4, 60], [4, 68], [8, 80]],
               [[8, 88], [8, 100], [8, 108], [12, 120]],
               [[12, 128], [12, 139], [12, 147], [16, 159]]]
    assert in_margin(quantize_colored_image(example3, 64), result3)


def test_add_mask():
    example1a = [[50, 50, 50]]
    example1b = [[200, 200, 200]]
    example1c = [[0, 0.5, 1]]
    result1 = [[200, 125, 50]]
    assert in_margin(add_mask(example1a, example1b, example1c), result1)
    example2a = [[[170, 20, 35], [45, 154, 161], [175, 28, 9]],
                 [[251, 210, 134], [74, 105, 46], [79, 183, 139]]]
    example2b = [[[1, 10, 1], [2, 20, 4], [3, 30, 9]],
                 [[4, 40, 16], [5, 50, 25], [6, 60, 36]]]
    example2c = [[1.0, 0.5, 0.33], [0.25, 0.2, 0.17]]
    result2 = [[[170, 20, 35], [24, 87, 82], [60, 29, 9]],
               [[66, 82, 46], [19, 61, 29], [18, 81, 54]]]
    assert in_margin(add_mask(example2a, example2b, example2c), result2)


def test_cartoonify():
    example1 = [[[170, 20, 35], [45, 154, 161], [175, 28, 9]],
                [[251, 210, 134], [74, 105, 46], [79, 183, 139]]]
    result1 = [[[0, 0, 0], [32, 128, 159], [0, 0, 0]],
               [[223, 191, 128], [0, 0, 0], [64, 159, 128]]]
    cartoon1 = cartoonify(example1, 3, 3, 1, 8)
    assert in_margin(cartoon1, result1)


if __name__ == '__main__':
    test_separate_channels()
    test_combine_channels()
    test_rbg2grayscale()
    test_blur_kernel()
    test_apply_kernel()
    test_bilinear_interpolation()
    test_resize()
    test_rotate_90()
    test_get_edges()
    test_quantize()
    test_quantize_colored_image()
    test_add_mask()
    test_cartoonify()
    print("Passed all Tests")
