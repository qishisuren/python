import pygame
import random
from pygame.locals import *
class Point:
    row = 0
    col = 0
    def __init__(self,row,col):
        self.row = row
        self.col = col
    def copy(self):
        return Point(self.row, self.col)

pygame.init()

w = 800
h = 600
ROW = 30
COL = 40
size = (w, h)
direct = "left"
window = pygame.display.set_mode(size)
pygame.display.set_caption("贪吃蛇")

def rect(point, color):
    w_cell = w/COL
    h_cell = h/ROW
    left = point.col*w_cell
    top = point.row*h_cell
    pygame.draw.rect(window,color,(left,top,w_cell,h_cell))

def food_exist():
    is_in =False
    while True:
        pos = Point(random.randint(0,ROW-1),random.randint(0, COL-1))
        if (pos.row ==head.row and pos.col == head.col):
            is_in =True
        for snake in snakes:
            if(pos.row == snake.row and pos.col == snake.col):
              is_in = True
        if is_in == False:
            break
    return pos


quit = True
clock =pygame.time.Clock()
head = Point(ROW / 2,COL / 2)
snakes =[Point(head.row,head.col+1),
         Point(head.row, head.col+2),
         Point(head.row, head.col+3)]
food = food_exist()
head_color = (0, 128, 128)
food_color = (255, 255, 0)
bk_color = (255, 255, 255)
snake_color = (200,200,200)

while quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = False
        elif event.type == pygame.KEYDOWN:
            print(event)
            if event.key == K_LEFT:
                if (direct == "up" or direct == "down"):
                    direct = "left"
            elif event.key == K_RIGHT:
                if (direct == "up" or direct == "down"):
                    direct = "right"
            elif event.key == K_UP:
                if (direct == "right" or direct == "left"):
                    direct = "up"
            elif event.key == K_DOWN:
                if (direct == "right" or direct == "left"):
                    direct = "down"
    dead = False
    if (head.row < 0 or head.col< 0 or head.row>ROW or head.col >COL):
        print("你死了")
        dead = True
    for snake in snakes:
        if(head.row == snake.row and head.col == snake.col):
            print("你死了")
            dead = True
    if dead ==True:
        break

    eat =(head.row == food.row and head.col == food.col)
    snakes.insert(0,head.copy())

    if eat:
        food = food_exist()
    else:
        snakes.pop()

    if direct == "left":
        head.col -= 1
    if direct == "down":
        head.row += 1
    if direct == "up":
        head.row -= 1
    if direct == "right":
        head.col += 1
    pygame.draw.rect(window,bk_color,(0,0,w,h))

    rect(head,head_color)
    rect(food,food_color)
    #生成蛇身体

    for snake in snakes:
        rect(snake,snake_color)
    pygame.display.update()
    clock.tick(10)    #通过控制画面每秒刷新次数调整速度，与电脑配置有关，数值越高速度越快
