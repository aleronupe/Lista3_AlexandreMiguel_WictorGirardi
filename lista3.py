import cv2
import random
import numpy as np
from threading import Thread


# def convert_vector()

# def quick_sort(vector_image, low, high):
#     pivot = vector_image[0]

    





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

    ################### Cria vetor de pedaços da imagem, de forma ordenada
    vec_pos = 0
    for i in range(0, lines, row_line):
        for j in range(0, columns, row_columns):
            pos_matrix = []
            for lin_pos in range(i, i+row_line):
                pos_line = []
                for col_pos in range(j, j+row_columns):
                    pos_line.append(img[lin_pos][col_pos]) # constrói linha por linha de cada elemento
                pos_matrix.append(pos_line) # adiciona a linha de cada elemento
            vector_image.append( (vec_pos, pos_matrix) )
            vec_pos = vec_pos + 1


    ############### Realiza o shuffle do vetor
    random.shuffle(vector_image)

    ##################### Converte vetor em imagem
    image_line = 0
    for i in range(0, len(vector_image), 5): # i = [0, 5, 10, 15, 20, 25]
        #  número de linhas para cada elemento a ser montado
        for lins in range(0, row_line): # lins = [0, 1, 2, ..., 108, 109 ]
            new_line = np.empty([0, 3], dtype="uint8") # array_vazio = [[0,0,0],[0,0,0]]
            for pos in range(i, i+5): # i = 0, cols = [0, 1, 2, 3, 4]
                line = vector_image[pos][1][lins]
                if lins == 0:
                    print(vector_image[pos][0])
                new_line = np.append(new_line, line, axis=0)
            new_image[image_line] = new_line
            image_line = image_line + 1



    cv2.imshow('Sorted Vector', new_image)
    # cv2.imshow('try', vector_image[0][1])
    # piece_image = np.empty([110,110,3], dtype="uint8")
    # for i in range(0, row_line):
    #     line = vector_image[23][1][i]
    #     piece_image[i] = line
    
    # cv2.imshow('Piece', piece_image)
    
    


    cv2.waitKey(0)
