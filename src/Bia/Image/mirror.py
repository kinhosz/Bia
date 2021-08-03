def mirror(img):

    for i in range(len(img)):
        aux = img[i]
        img[i] = aux[::-1]