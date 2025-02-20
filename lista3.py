import cv2
import random
import numpy as np
import time
from threading import Thread

def paint_piece_red(real_image):
    lin = len(real_image)
    col = len(real_image[0])
    matrix = []

    for i in range(0,lin):
        line = []
        for j in range(0,col):
            converted = [0, 0, real_image[i][j][2]]
            pixel = np.array(converted, dtype="uint8")
            line.append(pixel)
        line = np.array(line, dtype="uint8")
        matrix.append(line)
    colored_image = np.array(matrix, dtype="uint8")
    return colored_image

def paint_piece_blue(real_image):
    lin = len(real_image)
    col = len(real_image[0])
    matrix = []

    for i in range(0,lin):
        line = []
        for j in range(0,col):
            converted = [0, real_image[i][j][1], 0]
            pixel = np.array(converted, dtype="uint8")
            line.append(pixel)
        line = np.array(line, dtype="uint8")
        matrix.append(line)
    colored_image = np.array(matrix, dtype="uint8")
    return colored_image

def paint_piece_green(real_image):
    lin = len(real_image)
    col = len(real_image[0])
    matrix = []

    for i in range(0,lin):
        line = []
        for j in range(0,col):
            converted = [real_image[i][j][0], 0, 0]
            pixel = np.array(converted, dtype="uint8")
            line.append(pixel)
        line = np.array(line, dtype="uint8")
        matrix.append(line)
    colored_image = np.array(matrix, dtype="uint8")
    return colored_image

def prepare_image(vector_image):
    new_image = np.empty([lines, columns, 3], dtype="uint8")
    image_line = 0
    row_line = len(vector_image[0][1])
    for i in range(0, len(vector_image), 5): # i = [0, 5, 10, 15, 20, 25]
        #  número de linhas para cada elemento a ser montado
        for lins in range(0, row_line): # lins = [0, 1, 2, ..., 108, 109 ]
            new_line = np.empty([0, 3], dtype="uint8") # array_vazio = [[0,0,0],[0,0,0]]
            for pos in range(i, i+5): # i = 0, cols = [0, 1, 2, 3, 4]
                line = vector_image[pos][1][lins]
                # print('id:' + str(vector_image[pos][0]) + ' ' + 'lenght:' + str(len(line)) )
                new_line = np.append(new_line, line, axis=0)
            new_image[image_line] = new_line
            image_line = image_line + 1
    return new_image

def partition(vector_image, low, high):
    #coloca o pivot como último elemento, que não será acessado pelo for
    pivot = vector_image[high]
    pivot_pos = high
    index_small = low-1 #Começa menor do que o primeiro elemento, pois alocará o primeiro menor que o pivot na primeira posiçao
    #print(pivot[0])
    pivot_id = pivot[0]
    size = len(vector_image)

    image_backup = [None] * size


    for i in range(low, high+1):
        real_image = vector_image[i][1]
        pos_id = vector_image[i][0]
        if(vector_image[i][0] == pivot_id):
            vector_image[i] = (pivot_id, paint_piece_red(real_image))
            image_backup[pos_id] = real_image
        else:
            vector_image[i] = (vector_image[i][0], paint_piece_blue(real_image))
            image_backup[pos_id] = real_image

    for pos in range(low, high):
        # vec_pos = pos
        # pos_id = vector_image[pos][0]
        # red_image = vector_image[pos][1]
        # vector_image[pos] = (pos_id, paint_piece_blue(image_backup[pos_id]) )
        # cv2.imshow('Quick Sort', prepare_image(vector_image))
        # cv2.waitKey(1)
        # time.sleep(0.3)


        if vector_image[pos][0] <= pivot[0]:
            # Garante que os primeiros elementos estarão no começo do vetor
            index_small = index_small + 1
            vector_image[index_small], vector_image[pos] = vector_image[pos], vector_image[index_small]
            # vec_pos = index_small
            cv2.imshow('Quick Sort', prepare_image(vector_image))
            cv2.waitKey(1)
            time.sleep(0.3)
        # vector_image[vec_pos] = (pos_id, red_image)


    pivot_pos = index_small+1
    vector_image[high], vector_image[pivot_pos] = vector_image[pivot_pos], vector_image[high]
    cv2.imshow('Quick Sort', prepare_image(vector_image))
    cv2.waitKey(1)
    time.sleep(0.3)
    vector_image[pivot_pos] = (pivot_id, image_backup[pivot_id])
    cv2.imshow('Quick Sort', prepare_image(vector_image))
    cv2.waitKey(1)
    time.sleep(0.3)

    for i in range(low, high+1):
        pos_id = vector_image[i][0]
        vector_image[i] = (pos_id, image_backup[pos_id])
    cv2.imshow('Quick Sort', prepare_image(vector_image))
    cv2.waitKey(1)
    time.sleep(0.3)

    return pivot_pos

def quick_sort(vector_image, low, high):

    if low < high:
        pivot_pos = partition(vector_image, low, high)
        quick_sort(vector_image, low, pivot_pos - 1)
        quick_sort(vector_image, pivot_pos+1, high)

    return
    # witao aqui

def mergeSort(vector_image, low, high):
    if low < 0 or high < 0:
        return
    if (high - low) > 1:
        mid = (high-low)//2 + low
        mergeSort(vector_image, low, mid) # Não vai atingir o valor de mid
        mergeSort(vector_image, mid, high) # Vai a partir de mid

        leftVector = []
        rightVector = []

        for i in range(low, mid):
            leftVector.append(vector_image[i])

        for j in range(mid, high):
            rightVector.append(vector_image[j])



        for i in range(low, high):
            real_image = vector_image[i][1]
            pos_id = vector_image[i][0]
            vector_image[i] = (vector_image[i][0], paint_piece_blue(real_image))

        cv2.imshow('Merge Sort', prepare_image(vector_image))
        cv2.waitKey(1)
        time.sleep(0.2)


        i = 0
        j = 0
        k = low
        while i < len(leftVector) and j < len(rightVector):
            if leftVector[i] < rightVector[j]:
                vector_image[k] = leftVector[i]
                cv2.imshow('Merge Sort', prepare_image(vector_image))
                cv2.waitKey(1)
                time.sleep(0.2)
                i+=1
            else:
                vector_image[k] = rightVector[j]
                cv2.imshow('Merge Sort', prepare_image(vector_image))
                cv2.waitKey(1)
                time.sleep(0.2)
                j+=1
            k+=1

        # Checking if any element was left
        while i < len(leftVector):
            vector_image[k] = leftVector[i]
            cv2.imshow('Merge Sort', prepare_image(vector_image))
            cv2.waitKey(1)
            time.sleep(0.2)
            i+=1
            k+=1

        while j < len(rightVector):
            vector_image[k] = rightVector[j]
            cv2.imshow('Merge Sort', prepare_image(vector_image))
            cv2.waitKey(1)
            time.sleep(0.2)
            j+=1
            k+=1
        # for v in vector_image:
        #     print(v[0], end=' ')
        # print('\n')

    return




def counting_sort(vector_image, maxval):
    n = len(vector_image) # obtendo o tamanho do vetor
    m = maxval + 1 # atribuindo o tamanho do vetor + 1 por começar a 0
    count = [0] * m # inicializando o  novo vetor com o tamanho definido
    for pos in range(n):  #contando quantas vezes os elementos se repetem dentro do vetor
        pos_id = vector_image[pos][0]
        pos_image = vector_image[pos][1]
        count[pos_id] =  vector_image[pos]
        vector_image[pos] = (pos_id, paint_piece_blue(pos_image))
        cv2.imshow('Counting Sort', prepare_image(vector_image))
        cv2.waitKey(1)
        time.sleep(0.2)
    i = 0
    for a in range(m):
        vector_image[i] = count[a]
        i += 1
        cv2.imshow('Counting Sort', prepare_image(vector_image))
        cv2.waitKey(1)
        time.sleep(0.3)
    return vector_image

def insertionSort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >=0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up
    return b

def bucketSort(vector_image):
    arr = []
    slot_num = 10 # 10 means 10 slots, each
                  # slot's size is 0.1
    for i in range(slot_num):
        arr.append([])

    # Put array elements in different buckets
    for j in vector_image:
        index_b = int(slot_num * j)
        arr[index_b].append(j)

    # Sort individual buckets
    for i in range(slot_num):
        arr[i] = insertionSort(arr[i])

    # concatenate the result
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            vector_image[k] = arr[i][j]
            k += 1
    return vector_image

def menu_principal():
    print("*******************************************")
    print("**            MENU - LISTA 3             **")
    print("*******************************************")
    print("**   1 - Merge Sort                      **")
    print("**   2 - Quick Sort                      **")
    print("**   3 - Counting Sort                   **")
    print("**   4 - Créditos                        **")
    print("**   0 - Sair                            **")
    print("*******************************************")
    escolha = input("Digite uma Escolha: ")
    return escolha



if __name__ == "__main__":
    img = cv2.imread('arya.jpeg')
    cv2.imshow('Arya, The Cat', img)
    #(img[0][0])

    lines = len(img)
    columns = len(img[0])
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
                    pixel = np.array(img[lin_pos][col_pos], dtype="uint8")
                    pos_line.append(pixel) # constrói linha por linha de cada elemento
                pos_line = np.array(pos_line, dtype="uint8")
                pos_matrix.append(pos_line)# adiciona a linha de cada elemento
            pos_matrix = np.array(pos_matrix, dtype="uint8")
            vector_image.append( (vec_pos, pos_matrix) )
            vec_pos = vec_pos + 1



    # ############### Realiza o shuffle do vetor
    random.shuffle(vector_image)

    new_image = prepare_image(vector_image)



    escolha = 0
    # Loop do menu do programa
    while escolha != '100':
        escolha = menu_principal()
        # escolha 1 - Jogo
        if escolha == '1':
            random.shuffle(vector_image)
            mergeSort(vector_image, 0, len(vector_image))
            # Escolha 2 - Buscas fora do jogo
        elif escolha == '2':
            random.shuffle(vector_image)
            quick_sort(vector_image, 0, len(vector_image) - 1)
        elif escolha == '3':
            random.shuffle(vector_image)
            counting_sort(vector_image, 24)
            # Créditos
        elif escolha == '4':
            random.shuffle(vector_image)
            print("\n**************************************")
            print("Esse trabalho foi feito com carinho pelos alunos:")
            print("Alexandre Miguel Rodrigues Nunes Pereira - Matricula: 16/0000840")
            print("Wictor Bastos Girardi - Matricula: 17/0047326")
            print("**************************************\n\n")
            # Sair do programa
        elif escolha == '0':
            random.shuffle(vector_image)
            print("Obrigado por usar, volte sempre!\n")
            cv2.waitKey(0)
            break
            # Caso o usuario tenha entrado com um valor invalido
        else:
            print('Opção Invalida! Tente novamente')



    #                     0     1
    # vector_image[0] = (id, image)
    # vector_image[pos][0] = id

    # counting_sort(vector_image, 24)

    # quick_sort(vector_image, 0, len(vector_image) - 1)

    # mergeSort(vector_image, 0, len(vector_image))

    cv2.waitKey(0)
