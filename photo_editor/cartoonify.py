####################################
#intro ex5                         #
# name : Gal Bahary                #
# ID : 207297011                   #
# mail : gal.bahary@mail.huji.ac.il#
####################################

import copy
import math
from ex5_helper import *
import sys



def separate_channels(image):
    """
    :param image: list of an image
    :return: list of list divided to separate channels
    """
    seperated_image = list()
    temp_col_lst = list()
    temp_row_lst = list()
    for i in range(0, len(image[0][0])):
        for row in range(0, len(image)):
            for col in range(0, len(image[0])):
                temp_col_lst.append(image[row][col][i])
            temp_row_lst.append(temp_col_lst)
            temp_col_lst = []
        seperated_image.append(temp_row_lst)
        temp_row_lst=[]
    return seperated_image



def combine_channels(channels):
    """
    :param channels: a list of an image divided to separate channels
    :return: the original list of the image, combines the channels
    """
    combined_img = list()
    temp_cnl = list()
    temp_row = list()
    for i in range(0, len(channels[0])):
        for j in range(0, len(channels[0][0])):
            for t in range(0, len(channels)):
                temp_cnl.append(channels[t][i][j])
            temp_row.append(temp_cnl)
            temp_cnl = []
        combined_img.append(temp_row)
        temp_row = []
    return combined_img




def RGB2grayscale(colored_image) :
    """
    :param colored_image: list of lists of an colored image
    replaces every list of RGB to a single number
    :return: the same picture list but with values of a black & white picture
    """
    gray_pic = list()
    temp_row = list()
    temp_gray_code = list()
    for row in range(0, len(colored_image)):
        for col in range(0, len(colored_image[0])):
            red = colored_image[row][col][0]
            green = colored_image[row][col][1]
            blue = colored_image[row][col][2]
            temp_gray_code = round(red*0.299+green*0.587+blue*0.114)
            temp_row.append(temp_gray_code)
            temp_gray_code = []
        gray_pic.append(temp_row)
        temp_row = []
    return gray_pic



def blur_kernel(size):
    """
    :param size: the size of the kernel the func should make
    :return: kernel, list of lists in the size of : sizeXsize with the value of 1/size**2
    """
    row_lst = list()
    kernel_lst = list()
    kernel = 1/(size**2)
    for j in range(0,size):
        row_lst.append(kernel)
    for i in range(0, size):
        kernel_lst.append(row_lst)
    return kernel_lst



def kernel_sum_of_image(image,row,col,kernel):
    """
    :param image: list of lists of a image
    :param row: the row index of the wanted pixel
    :param col: the collum index of the wanted pixel
    :param kernel: the kernel applied on the index
    :return: the sum of the square around the pixel (in the size of the kernel)
    """

    ker_len = len(kernel)
    radius = ker_len//2
    width = len(image[0])
    height = len(image)
    pixel = image[row][col]
    kernel_sum_lst = list()
    temp_row = list()

    if row-radius>=0 and col-radius>=0 and row+radius<height and col+radius<width:
        for i in range(row-radius, row+radius+1) :
            for j in range(col-radius, col+radius+1) :
                temp_row.append(image[i][j])
            kernel_sum_lst.append(temp_row)
            temp_row = []
        return kernel_sum_lst

    else:
        for i in range(row-radius, row+radius+1):
            for j in range(col-radius, col+radius+1):
                if i < 0 or j < 0 or i > height-1 or j > width-1 :
                    temp_row.append(pixel)
                else:
                    temp_row.append(image[i][j])
            kernel_sum_lst.append(temp_row)
            temp_row=[]
        return kernel_sum_lst



def apply_kernel(image, kernel):
    """
    :param image: list of an image (has to be 2D)
    :param kernel: a kernel in a size of KXK (k is odd)
    :return: the list of the image after multiplied each pixel with the kernel
    the returned picture should be blurred
    """
    new_image = list()
    temp_row = list()
    new_pixel = 0
    kernel_sum = 0
    for i in range(0,len(image)):
        for j in range (0, len(image[0])):
            kernel_sum_lst = kernel_sum_of_image(image, i, j, kernel)
            for x in range(len(kernel_sum_lst)) :
                for y in range(len(kernel_sum_lst[0])) :
                    new_pixel += kernel_sum_lst[x][y] * kernel[x][y]
            new_pixel = round(new_pixel)
            if new_pixel > 255 :
                new_pixel = 255
            elif new_pixel < 0 :
                new_pixel = 0
            temp_row.append(new_pixel)
            new_pixel=0
        new_image.append(temp_row)
        temp_row = []
    return new_image



def bilinear_interpolation(image, y, x) :
    """
    :param image: grayscale original image
    :param y: height index of a pixel in new image
    :param x: width index of a pixel in new image
    :return: the calculated pixel value of the index in the new picture based on the old one
    """

    width = len(image[0])-1
    height = len(image)-1
    y_mod = y % 1
    x_mod = x % 1
    a = image[int(y // 1)][int(x // 1)]

    if int(x//1) == width and int(y//1) == height :
        value = a

    elif int(x//1) == width :
        b = image[int(y // 1) + 1][int(x // 1)]
        value = round(a * (1-y_mod) + b * y_mod)

    elif int(y//1) == height :
        c = image[int(y // 1)][int(x // 1) + 1]
        value = round(a * (1-x_mod) + c * x_mod)

    else :
        b =image[int(y//1)+1][int(x//1)]
        c = image[int(y//1)][int(x//1)+1]
        d = image[int(y//1)+1][int(x//1)+1]
        value = round( a * (1-x_mod) * (1-y_mod) + b * y_mod * (1-x_mod) + c * x_mod * (1-y_mod) + d * x_mod * y_mod )

    return value



def corner(image, row, col):
    width = len(image[0])-1
    height = len(image)-1
    if row == 0 and col == 0 :
        value = image[0][0]
    elif row == 0 :
        value = image[0][width]
    elif col == 0 :
        value = image[height][0]
    else:
        value = image[height][width]
    return value


def resize(image, new_height, new_width) :
    """
    the func takes a pictures and returns a new one in the height and width given
    :param image: a grayscale image (list of lists)
    :param new_height: the height of the new image
    :param new_width: the width of the new image
    :return: a copy of the old image in the new height and width
    """

    img_height = len(image)
    img_width = len(image[0])
    temp_row = list()
    new_img = list()
    height_ratio = img_height / new_height
    width_ratio = img_width / new_width

    for i in range(0, new_height) :
        for j in range(0, new_width) :
            y, x = i * height_ratio , j * width_ratio
            if (i == new_height-1 or i == 0) and (j == 0 or j == new_width-1):
                new_pixel = corner(image, i, j)
            else:
                new_pixel = bilinear_interpolation(image, y, x)
            temp_row.append(new_pixel)
        new_img.append(temp_row)
        temp_row = []
    return new_img



def rotate_90(image, direction) :
    """
    :param image: RGB or grayscale image
    :param direction: which direction the image would rotate (L ot R)
    :return: the image rotated to the direction that was inserted
    """

    rot_pic = list()
    temp_row = list()

    if direction == "R" :
        for i in range(0, len(image[0])) :
            for j in range(len(image)-1, -1, -1) :
                temp_row.append(image[j][i])
            rot_pic.append(temp_row)
            temp_row = []
        return rot_pic

    else :
        for i in range(len(image[0])-1, -1, -1) :
            for j in range(0, len(image)) :
                temp_row.append(image[j][i])
            rot_pic.append(temp_row)
            temp_row = []
        return rot_pic




def sum_a_matrix(mat) :   # recives a 2D matrix and returns the sum of all parts of the matrix
    sum = 0
    for i in range(len(mat)) :
        for j in range(len(mat[0])):
            sum += mat[i][j]
    return sum


def get_edges(image, blur_size, block_size, c) :
    """
    :param image: grayscale image (list of lists)
    :param blur_size: the size of the kernel the blures the image
    :param block_size: the size of the block used to calculate the sum of neighbors
    :param c: a constant number that is reduced from the value of the pixel
    :return:a black and white image that emphasizes the edges of the picture
    """

    kernel = blur_kernel(blur_size)
    blurred_image = apply_kernel(image, kernel)
    block_size_kernel = blur_kernel(block_size)
    eged_image = list()
    temp_row = list()
    divide = 1/(block_size**2)
    height = len(blurred_image)
    width = len(blurred_image[0])
    threshold = 0

    for i in range(0, height) :
        for j in range(0, width) :
            threshold = (sum_a_matrix(kernel_sum_of_image(blurred_image, i, j, block_size_kernel)) * divide) - c
            if blurred_image[i][j] >= threshold :
                temp_row.append(255)
            else :
                temp_row.append(0)
        eged_image.append(temp_row)
        temp_row = []
    return eged_image



def quantize(image, N) :
    """
    :param image: a grayscale image (list of lists)
    :param N:number of shades wanted in the new image
    :return: the image with N shades of colors in it
    """

    qimg = list()
    temp_row = list()
    for i in range(0, len(image)) :
        for j in range(0, len(image[0])) :
            old_pixel = image[i][j]
            new_pixel = round(math.floor(old_pixel*(N/255))*(255/N))
            temp_row.append(int(new_pixel))
        qimg.append(temp_row)
        temp_row = []
    return qimg



def quantize_colored_image(image, N) :
    """
    :param image: a colored image list[lists[lists]]
    :param N: number of shades in the new image
    :return: the image with N shades in it
    """
    qimg = list()
    q_sep_img = list()
    seperated_img = separate_channels(image)
    cnls = len(seperated_img)
    for i in range(0, cnls) :
        q_sep_img.append(quantize(seperated_img[i], N))
    qimg = combine_channels(q_sep_img)
    return qimg



def add_mask(image1, image2, mask) :
    """
    :param image1: any image (colored or grayscale)
    :param image2: any image (colored or grayscale)
    :param mask: list of lists contains numbers in range [0,1]
    :return: a combination of the 2 images, every pixel is calculated by the value of the pixel in mask
    i added the option of combining colored image with grayscale because it helps me in the "cartoonify" function
    """

    sep_img1 = list()
    sep_img2 = list()
    comb_img = list()
    channel = list()
    all_cnls = list()
    temp_row = list()

    if type(image1[0][0]) is list and type(image2[0][0]) is list:   # if both images are colored image
        sep_img1 = separate_channels(image1)
        sep_img2 = separate_channels(image2)
        for cnl in range(0,len(sep_img1)) :
            for i in range(0, len(mask)):
                for j in range(0, len(mask[0])):
                    new_pixel = int(round(sep_img1[cnl][i][j] * mask[i][j] + sep_img2[cnl][i][j] * (1 - mask[i][j])))
                    temp_row.append(new_pixel)
                channel.append(temp_row)
                temp_row = []
            all_cnls.append(channel)
            channel = []
        comb_img = combine_channels(all_cnls)

    elif type(image1[0][0]) is list :   # if only the first image is colored and the second is grayscale
        sep_img1 = separate_channels(image1)
        for cnl in range(0, len(sep_img1)):
            for i in range(0, len(mask)):
                for j in range(0, len(mask[0])):
                    new_pixel = int(round(sep_img1[cnl][i][j] * mask[i][j] + image2[i][j] * (1 - mask[i][j])))
                    temp_row.append(new_pixel)
                channel.append(temp_row)
                temp_row = []
            all_cnls.append(channel)
            channel = []
        comb_img = combine_channels(all_cnls)

    elif type(image2[0][0]) is list:  # if only the second image is colored and the first is grayscale
        sep_img2 = separate_channels(image2)
        for cnl in range(0, len(sep_img2)):
            for i in range(0, len(mask)):
                for j in range(0, len(mask[0])):
                    new_pixel = int(round(image1[i][j] * mask[i][j] + sep_img2[cnl][i][j] * (1 - mask[i][j])))
                    temp_row.append(new_pixel)
                channel.append(temp_row)
                temp_row = []
            all_cnls.append(channel)
        comb_img = combine_channels(all_cnls)

    else:     # if both images are grayscale
        for i in range(0, len(mask)) :
            for j in range(0, len(mask[0])) :
                new_pixel = int(round(image1[i][j] * mask[i][j] + image2[i][j] * (1 - mask[i][j])))
                temp_row.append(new_pixel)
            comb_img.append(temp_row)
            temp_row = []

    return comb_img





def cartoonify(image, blur_size, th_block_size, th_c, quant_num_shades) :
    """
    takes the edges of the image and the quantize image and combines them using add mask
    :param image: any image (colored or grayscale)
    :param blur_size: the size of the kernel that is sent to "apply kernel" function
    :param th_block_size: the block size that is sent to "get edges" function
    :param th_c: the c value sent to "get edges" function
    :param quant_num_shades: the num of shades, sent to quantize function
    :return: the picture in a cartooned filter
    """

    kernel = blur_kernel(blur_size)
    gray_img = RGB2grayscale(image)
    img_edges = get_edges(gray_img, blur_size, th_block_size, th_c)
    q_img = quantize_colored_image(image, quant_num_shades)
    mask = list()
    temp_row = list()
    cartoned_img = list()

    for i in range(0, len(img_edges)):
        for j in range(0, len(img_edges[0])):
            if img_edges[i][j] == 0 :
                cur_pix = 0
            else :
                cur_pix = 1
            temp_row.append(cur_pix)
        mask.append(temp_row)
        temp_row = []

    cartoned_img = add_mask(q_img, img_edges, mask)

    return cartoned_img




if __name__=="__main__":

    if len(sys.argv)  == 8 :
        print("the input is invalid, try again")

    else:
        image_source = sys.argv[1]   # the path of the image uploaded
        cartoon_dest = sys.argv[2]   # the path where the cartoon image will be saved
        max_im_size = int(sys.argv[3])    # max size of picture
        blur_size = int(sys.argv[4])
        th_block_size = int(sys.argv[5])
        th_c = int(sys.argv[6])
        quant_num_shades = int(sys.argv[7])

        image = load_image(image_source)
        height = len(image)
        width = len(image[0])

        if image[0][0] is list :
            sep_img = separate_channels(image)

        if height > max_im_size and height >= width :
            img_ratio = width / height
            height = max_im_size
            width = round(height * img_ratio)
            if type(image[0][0]) is list :
                sep_img = separate_channels(image)
                resized_sep_img = list()
                for i in range(len(sep_img)) :
                    resized_sep_img.append(resize(sep_img[i]))
                resized_img = combine_channels(resized_sep_img)
            else:
                resized_img = resize(image, height, width)

        elif width > max_im_size and width >= height :
            img_ratio = height / width
            width = max_im_size
            height = round(width * img_ratio)
            if type(image[0][0]) is list :
                sep_img = separate_channels(image)
                resized_sep_img = list()
                for i in range(len(sep_img)) :
                    resized_sep_img.append(resize(sep_img[i], height, width))
                resized_img = combine_channels(resized_sep_img)
            else:
                resized_img = resize(image, height, width)

        else :
            resized_img = image

        cartooned_img = cartoonify(resized_img, blur_size, th_block_size, th_c, quant_num_shades)
        save_image(cartooned_img, cartoon_dest)
