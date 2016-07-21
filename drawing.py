'''
Author:Adylova Ayana
'''

from turtle import *
from math import *
from random import *

def Tree(size,depth):
    if depth<0:
        pass
    else:
        speed(0)
        if (depth%2==0) :
            color("brown")
        else:
            color("maroon")

        fd(size)
        lt(30)
        Tree(size/1.5,depth-1)
        rt(60)
        Tree(size/1.5,depth-1)
        lt(30)
        bk(size)

def partFlower(depth,size):
    if depth<=0:
        pass
    else:
        if (depth%2==0) :
            color(240,128,128)
        else:
            color(105,105,105)
        speed(0)
        begin_fill()
        lt(36)
        fd(size)
        rt(20)
        fd(size/3)
        rt(20)
        fd(size/3)
        rt(20)
        fd(size/3)
        rt(20)
        fd(size/3)
        lt(10)
        fd(size/2)

        rt(112)

        fd(size/2)
        lt(10)
        fd(size/3)
        rt(20)
        fd(size/3)
        rt(20)
        fd(size/3)
        rt(20)
        fd(size/3)
        rt(20)
        fd(size)
        rt(180-36)
        end_fill()
        partFlower(depth-1,size-8)


def Flower():
    setheading(90)
    partFlower(5,40)
    rt(72)
    partFlower(5,40)
    rt(72)
    partFlower(5,40)
    rt(72)
    partFlower(5,40)
    rt(72)
    partFlower(5,40)


def onePart(size):
    fd(size)
    rt(30)
    fd(size)
    rt(30)
    fd(size)
    rt(30)
    fd(size)
    rt(30)
    fd(size)
    rt(30)
    fd(size)
    rt(30)
    fd(size)
    rt(30)
    fd(size)
    rt(30)
    lt(120)

def Triple(depth):
    if depth<0:
        pass
    else:
        hideturtle()
        color('yellow')
        onePart(130)
        onePart(130)
        onePart(130)
        rt(15)
        Triple(depth-1)



def Border():
    color('black')
    begin_fill()
    up()
    setpos(-1250,1600)
    down()
    fd(2500)
    rt(90)
    fd(3200)
    rt(90)
    fd(2500)
    rt(90)
    fd(3200)
    end_fill()
    up()
    setpos(0,0)
    down()

def reccircle(depth,r):
    hideturtle()
    if (depth%2==0) :
            color("orange")
    else:
            color("brown")
    speed(0)
    if depth<=0:
        pass
    else:
        circle(r)
        lt(15/2)
        reccircle(depth-1,r)


def wingr(size,depth):
    hideturtle()
    if depth<0:
        pass
    else:
        if (depth%2==0) :
            color(205,92,92)
        else:
            color(139,0,0)
        begin_fill()
        rt(30)
        fd(size/sqrt(2+sqrt(3)))
        rt(30)
        fd(size/sqrt(2+sqrt(3)))
        rt(15)
        fd(size)
        rt(150)
        fd(size)
        rt(30)
        fd(size)
        rt(130)
        end_fill()
        wingr(size/2,depth-1)


def wingl(size,depth):
    hideturtle()
    if depth<0:
        pass
    else:
        if (depth%2==0) :
            color(205,92,92)
        else:
            color(139,0,0)
        begin_fill()
        lt(30)
        fd(size/sqrt(2+sqrt(3)))
        lt(30)
        fd(size/sqrt(2+sqrt(3)))
        lt(15)
        fd(size)
        lt(150)
        fd(size)
        lt(30)
        fd(size)
        lt(130)
        end_fill()
        wingl(size/2,depth-1)

def star(x,y):
    speed(0)
    color('white')
    up()
    goto(x,y)
    down()
    fd(14)
    rt(144)
    fd(14)
    rt(144)
    fd(14)
    rt(144)
    fd(14)
    rt(144)
    fd(14)



def stars():
    for i in range(500):
        x=randint(-1200,1200)
        y=randint(-1600,1600)
        star(x,y)

def main():
    colormode(255)
    setworldcoordinates(-1250,-1600,1250,1600)
    Border()
    stars()
    up()
    goto(0,0)
    down()

    Tree(450,8)
    rt(120)
    Tree(450,8)
    rt(60)
    Tree(450,8)
    rt(60)
    Tree(450,8)

    Triple(23)
    reccircle(48,90)

    rt(120)
    up()
    setpos(180,0)
    down()
    wingr(600,3)

    up()
    setpos(-180,0)
    down()
    lt(100)
    wingl(600,3)

    for i in range(-1100,1300,200):
        up()
        setpos(i,-1500)
        down()
        Flower()
    for i in range(-1100,1300,200):
        up()
        setpos(i,1500)
        down()
        Flower()



title('Ayana Adylova')
main()
input("press Enter to exit")