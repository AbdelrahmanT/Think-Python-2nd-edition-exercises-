import  turtle
import math
bob = turtle.Turtle()
print(bob)

def square(t,length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t,length,n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t,r,arc):
    length= 1
    n= math.pi * r
    for i in range(int(n)):
        t.fd(length)
        t.lt(arc/n)

circle(bob,30,30)
bob.fd(2000)

turtle.mainloop() 
