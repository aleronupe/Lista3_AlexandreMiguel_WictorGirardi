import cv2
import random
import numpy as np
from threading import Thread

# def convert_image(img_tuple, lines, columns):
#     new_image = np.empty([lines, columns, 3], dtype="uint8")
#     for i in range(lines):
#         line = np.empty([columns, 3], dtype="uint8")
#         for j in range(columns):
#             line[j] = img_tuple[i][j][1]
#         new_image[i] = line
#     return new_image

# def convert_line(original_line):
#     size = len(original_line)
#     new_line = np.empty([size, 3], dtype="uint8")
#     for i in range(size):
#         new_line[i] = original_line[i][1]
#     return new_line



if __name__ == "__main__":
    img = cv2.imread('arya.jpeg')
    cv2.imshow('Arya, The Cat', img)
    print(img[0][0])

    lines = len(img)
    columns = len(img[0])
    new_image = np.empty([lines, columns, 3], dtype="uint8")
    vector_image = []

    row_columns = columns//5 #quantidade de elementos nas colunas de cada seção
    row_line = row_columns #quantidade de elementos nas linhas de cada seção
    vector_size = 5*(lines//row_line) # total_de_linhas / linhas_por_seção = quantidade de linhas de seção

    print(row_columns)
    print(row_line)
    print(vector_size)

    # Separação dos elementos nxn da imagem e preenchimento
    vec_pos = 0
    for i in range(0, lines, row_line):
        for j in range(0, columns, row_columns):
            pos_matrix = []
            for lin_pos in range(j, j+row_line):
                pos_line = []
                for col_pos in range(i, i+row_columns):
                    pos_line.append(img[lin_pos][col_pos]) # constrói linha por linha de cada elemento
                pos_matrix.append(pos_line) # adiciona a linha de cada elemento
            vector_image.append( (vec_pos, pos_matrix) )
            vec_pos = vec_pos + 1

    # random.shuffle(vector_image)

    # for i in range(0,len(vector_image)):
    #     print(vector_image[i][0])


    # vec_pos = 0
    # for i in range(0, vector_size//5):
    #     new_line = np.empty([0, 3], dtype="uint8")
    #     for j in range(0, 5):
    #         line = convert_line(vector_image[vec_pos][1][j])
    #         new_line.append(line)
    #         vec_pos = vec_pos + 1


    image_line = 0
    for i in range(0, len(vector_image), 5): # i = [0, 5, 10, 15, 20, 25]
        #  número de linhas para cada elemento a ser montado
        for lins in range(0, row_line): # lins = [0, 1, 2, ..., 108, 109 ]
            new_line = np.empty([0, 3], dtype="uint8") # array_vazio = [[0,0,0],[0,0,0]]
            for cols in range(i, i+5): # i = 0, cols = [0, 1, 2, 3, 4]
                line = vector_image[cols][1][lins]
                if(cols == 0 and lins == 0):
                    print(vector_image[cols][1][lins])
                    print('chocolate')
                    print(line)
                new_line = np.append(new_line, line, axis=0)
            new_image[image_line] = new_line
            image_line = image_line + 1



    cv2.imshow('Bubble Sort', new_image)
    print(new_image[0][0])


    cv2.waitKey(0)