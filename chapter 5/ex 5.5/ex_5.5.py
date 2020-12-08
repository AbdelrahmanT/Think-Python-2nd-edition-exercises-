import turtle


def draw(t,length,n):
    angle=50
    if n==0:
        return
    t.fd(length*n)
    t.lt(angle)
    draw(t,length,n-1)
    t.rt(2*angle)
    draw(t,length,n-1)
    t.lt(angle)
    t.bk(length*n)

turtle.tracer(0,0)
draw(turtle,2,100)