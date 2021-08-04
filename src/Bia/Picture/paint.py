def paint(img, side, HEIGHT, WIDTH):

    point1 = (HEIGHT - side)//2 - 1
    point2 = HEIGHT - (HEIGHT - side)//2
    point3 = (WIDTH - side)//2 - 1
    point4 = WIDTH - (WIDTH - side)//2

    for i in range(HEIGHT):
        for j in range(WIDTH):
            if i <= point1 or i >= point2 or j <= point3 or j >= point4:
                img[i][j] = (0,0,0)