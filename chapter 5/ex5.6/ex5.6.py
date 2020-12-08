import turtle

def koch(t,x):
    if x<3:
        t.fd(x)
        return
    koch(t,x/3)
    t.lt(60)
    koch(t,x/3)
    t.rt(120)
    koch(t,x/3)
    t.lt(60)
    koch(t,x/3)

turtle.tracer(10,10)
koch(turtle,200)

























"""
def koch_curve(t,x):
    draws a koch curve 
    t: turtle
    x: length
    
    if x<3:
        t.fd(x)
    else:
        m/3
        t.fd(x/3)
        t.lt(60)

    koch_curve(t,x/3)
    t.rt(120)
    koch_curve(t,x/3)
    t.lt(60)
    koch_curve(t,x/3)


def snowflake(t,x,z):
    for i in range(z):
        koch_curve(t,x)

snowflake(turtle,30,200)
"""

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

#draw(turtle,20,3)

turtle.mainloop()
