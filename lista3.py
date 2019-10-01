import cv2
import random
import numpy as np
from threading import Thread

#ordenation funcions

def selection_sort(img_tuple):
    size = len(img_tuple)
    for i in range(size):
        for j in range(i+1, size):
            if img_tuple[j][0] < img_tuple[i][0]:
                aux = img_tuple[i]
                img_tuple[i] = img_tuple[j]
                img_tuple[j] = aux

    return img_tuple

def bubble_sort(img_tuple):
    #subtraimos por um para sempre compararmos com os proximos valores
    size = len(img_tuple) - 1
    #realiza o calculo de quantas vezes vai ser necessaria
    #a passagem pelo tamanho do vetor
    for i in range(size):
        #realiza a troca de posicoes dentro dos vetores
        for j in range(size -i):
            if img_tuple[j][0] > img_tuple[j+1][0]:
                img_tuple[j], img_tuple[j+1] = img_tuple[j+1], img_tuple[j]
    return img_tuple

def shell_sort(img_tuple):
 size = len(img_tuple)
 gap = int(size/2)
 while(gap >= 1):
  i = gap
  while(i < size):
   value = img_tuple[i]
   j = i
   while(j-gap >= 0 and value < img_tuple[j - gap]):
    img_tuple[j] =  img_tuple[j - gap]
    j -= gap
   img_tuple[j] = value
   i+=1
  gap = int(gap/2)
 return img_tuple

# Como se a cada elemento encontrado, o algorítmo percorre o vetor do fim pro começo para encontrar a posição adequada de inserção
def insertion_sort(img_tuple):
    size = len(img_tuple)
    for index in range(1,size): # Considering that the fist element is in the right position
        current = img_tuple[index][0] #Stablish fixed element for comparison [(**id**, RGB)]
        current_tuple = img_tuple[index] # [**(id, RGB)**]
        position = index
        #comparing one element to the one that is behind the current element
        while  position > 0 and img_tuple[position-1][0] > current:
           # Doing the swaping
           img_tuple[position] = img_tuple[position-1]
           position -= 1
        img_tuple[position] = current_tuple #Tuple being swapped from current_tuple
    # return the sorted tupl
    return img_tuple

def convert_image(img_tuple, lines, columns):
    new_image = np.empty([lines, columns, 3], dtype="uint8")
    for i in range(lines):
        line = np.empty([columns, 3], dtype="uint8")
        for j in range(columns):
            line[j] = img_tuple[i][j][1]
        new_image[i] = line
    return new_image

def convert_line(original_line):
    size = len(original_line)
    new_line = np.empty([size, 3], dtype="uint8")
    for i in range(size):
        new_line[i] = original_line[i][1]
    return new_line



if __name__ == "__main__":
    img = cv2.imread('arya.jpeg')
    cv2.imshow('Arya, The Cat', img)

    lines= len(img)
    columns = len(img[0])
    new_image = np.empty([lines, columns, 3], dtype="uint8")
    vector_image = []

    row_columns = columns//5
    row_line = row_columns
    vector_size = 5*(lines//row_line)

    print(row_columns)
    print(row_line)
    print(vector_size)

    # Ordenação das tuplas
    vec_pos = 0
    for i in range(0, lines, row_line):
        for j in range(0, columns, row_columns):
            pos_matrix = []
            for lin_pos in range(j, j+row_line):
                pos_line = []
                for col_pos in range(i, i+row_columns):
                    pos_line.append(img[lin_pos][col_pos])
                pos_matrix.append(pos_line)
            vector_image.append( (vec_pos, pos_matrix) )
            vec_pos = vec_pos + 1

    random.shuffle(vector_image)

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
    for i in range(0, len(vector_image), 5):
        for lins in range(0, row_line):
            new_line = np.empty([0, 3], dtype="uint8")
            for cols in range(i, i+5):
                line = convert_line(vector_image[cols][1][lins])
                new_line = np.append(new_line, line, axis=0)
            new_image[image_line] = new_line
            image_line = image_line + 1



    cv2.imshow('Bubble Sort', new_image)


    cv2.waitKey(0)
