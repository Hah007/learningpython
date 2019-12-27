from  turtle import *
from math import cos,radians
import time,random

def randomcolor():
    colorArr=['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color=""
    for i in range(6):
        color+=colorArr[random.randint(0,14)]
    return '#'+color

def square(b):
    #绘制正方形
    fillcolor(randomcolor())
    # begin_fill()
    for i in range(4):
        fd(b)
        right(90)
    end_fill()
        
def draw(b):
    #画一个勾股树
    if b<15:return
    pencolor(randomcolor())
    square(b)
    #第二个正方形
    fd(b)
    left(30)
    draw(b*cos(radians(30)))
    square(b*cos(radians(30)))
    #第三个正方形
    right(90)
    fd(b*cos(radians(30)))
    draw(b*cos(radians(60)))
    square(b*cos(radians(60)))
    #移动画笔到第三个正方形右端
    right(90)
    fd(b*cos(radians(60)))
    #画笔归位
    right(30)
    fd(b)
    right(90)
    fd(b)
    right(90)



if __name__ == '__main__':
    # colormode(255)
    speed(0)
    up()
    goto(50,-250)
    down()
    seth(90)  
    draw(100)
    time.sleep(3)
  
