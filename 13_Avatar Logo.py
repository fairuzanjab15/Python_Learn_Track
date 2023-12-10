from turtle import *
speed (0)
bgcolor('black')
color('orange')
hideturtle()
n=3
p=True
while True:
    circle(n)
    if p:
        n=n-1
    else:
        n=n+1
    if n==0 or n==3s0:
        p=not p
    left(1)
    forward(3)