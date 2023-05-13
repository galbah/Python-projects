 ##############################################################################
# FILE: ex5_helper_old.py
# EXERCISE: Intro2cs ex5 2021-2022
# WRITER: Intro2CS 1 2021-2022 staff
# DESCRIPTION:A helper file for ex5 that masks handling with images
##############################################################################

##############################################################################
#                                   Imports                                  #
##############################################################################
import copy
import os
import sys
from PIL import Image


##############################################################################
#                                 CONSTANTS                                  #
##############################################################################
ERR_MSG = 'no such file'
ERR_CODE = -1


##############################################################################
#                              Helper Functions                              #
##############################################################################
def load_image(image_filename):
    """
    Loads the image stored in the path image_filename and return it as a list
    of lists.
    :param image_filename: a path to an image file. If path doesn't exist a
    massage is printed and the program terminates.
    :return: a multi-dimensional list representing the image in the format
    rows X cols X channels. The list is 2D in case of a grayscale image and 3D
    in case it's colored.
    """
    if not os.path.exists(image_filename):
        raise FileNotFoundError
    img = Image.open(image_filename).convert('RGB')
    image = lists_from_pil_image(img)
    return image


def show_image(image):
    """
    Displays an image
    :param image: an image represented as a multi-dimensional list of the
    format rows X cols X channels
    """
    pil_image_from_lists(image).show()


def save_image(image, filename):
    """ save an image (as list of lists) to a file """
    img = pil_image_from_lists(image)
    output_dir = os.path.dirname(filename)

    if output_dir != "" and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    img.save(filename)


def lists_from_pil_image(image):
    """ Turn an Image obj to a list of lists """
    width, height = image.size
    pixels = list(image.getdata())
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    if type(pixels[0][0]) == tuple:
        for i in range(height):
            for j in range(width):
                pixels[i][j] = list(pixels[i][j])
    return pixels


def pil_image_from_lists(image_as_lists):
    """ Generate an Image obj from list of lists """
    image_as_lists_copy = copy.deepcopy(image_as_lists)
    height = len(image_as_lists_copy)
    width = len(image_as_lists_copy[0])

    if type(image_as_lists_copy[0][0]) == list:
        for i in range(height):
            for j in range(width):
                image_as_lists_copy[i][j] = tuple(image_as_lists_copy[i][j])
        im = Image.new("RGB", (width, height))
    else:
        im = Image.new("L", (width, height))

    for i in range(width):
        for j in range(height):
            im.putpixel((i, j), image_as_lists_copy[j][i])
    return im

