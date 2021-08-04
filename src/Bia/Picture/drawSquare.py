def drawSquare(img, side, HEIGHT, WIDTH):

    point1 = (HEIGHT - side)//2 - 1
    point2 = HEIGHT - (HEIGHT - side)//2
    point3 = (WIDTH - side)//2 - 1
    point4 = WIDTH - (WIDTH - side)//2

    for i in range(point1, point2+1):
        img[i][point3] = (0,255,0)
        img[i][point4] = (0,255,0)
    
    for j in range(point3, point4):
        img[point1][j] = (0,255,0)
        img[point2][j] = (0,255,0)

