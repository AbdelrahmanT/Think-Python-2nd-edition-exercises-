from __future__ import print_function, division

import string
import math
import turtle
import secrets

def move(t,length):
    """moves forwards without drawing
    t: turtle
    length: movement length
    """
    t.pu()
    t.fd(length)
    t.pd()

def move_inclined(t,length,angle):
    """inclined movement without drawing
    t: turtle
    length: movement length
    ange: inclination angle
    """
    t.pu()
    t.lt(angle)
    t.fd(length)
    t.pd()



def square(t, length):
    """Draws a square with sides of the given length.

    Returns the Turtle to the starting position and location.
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    """Draws a polygon with n sides.

    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def circle(t, r):
    """Draws a circle with the given radius.

    t: Turtle
    r: radius
    """
    arc(t, r, 360)

def petal(t,r,angle):
    """Draws petals
    t: turtle
    r: radius of arc
    angle: angle of arc
    """
    turn_angle=180-angle
    for i in range(2):
        arc(bob,r,angle)
        t.lt(turn_angle)



def flower(t,n,r,angle):
    """Draws flowers
    t: turtle
    n: number of petals
    r: radius of arc
    angle: angle of arc
    """
    for i in range(n):
        petal(t,r,angle)
        t.lt(angle)



def six_char_hex(n):
    intn=int(n)
    nstr=str(intn)
    if len(nstr)==6:
        return nstr
    elif len(nstr)-6<6:
        for i in range(len(nstr)-6):
            '0'+nstr
    return nstr



def isosceles_triangle(t,small_side,angle):
    """Draws an icosceles triangle with the turtle looking down at the base angle
    t: turtle
    small_side: not the base lol
    angle: peak angle
    """

    x = angle
    angle = ( angle/180 ) * math.pi
    small_angle = (math.pi-angle)/2
    base = ( math.sin(angle) / math.sin(small_angle) ) * small_side 
    small_angle= (small_angle/math.pi)* 180
    angle = x
    t.rt(small_angle)
    t.fd(small_side)
    t.rt(180-small_angle)
    t.fd(base)    
    t.rt(180-small_angle)
    t.fd(small_side)
    t.lt(180)
    print(base, small_side, small_angle, angle, x)


def polypie(t, n ,r):
    """
    t: turtle
    n: number of iso triangles
    r: length
    """
    angle=360/n
    sangle=(180-angle)/2
    for i in range(n):
        isosceles_triangle(t,r,angle)
        t.lt(sangle)


#PREMITIVES PREMITIVES PREMITIVES PREMITIVES PREMITIVES PREMITIVESPREMITIVES PREMITIVES PREMITIVES

#cancelled due to being tedious AND MAKING IT AND TESTING IT WRONG


def vertical(t,n):
    t.lt(90)
    t.fd(n)
    t.rt(90)

def backandforth(t,n):
    t.fd(n)
    t.bk(n)

    def skip(t, n):
        """lift the pen and move"""
        t.pu
        t.fd(n*2)
        t.pu
    
#LETTERS LETTERS LETTERS LETTERS LETTERS LETTERS LETTERS LETTERS LETTERS LETTERS LETTERS LETTERS 

class letters: #cancelled due to being tedious + I MADE IT AND TESTED IT INCORRECTLY
#  A-B-C-D-E-F-G-H-I-J-K-L-M-N-O-P-Q-R-S-T-U-V-W-X-Y-Z
    def draw_a(t,n):
        t.lt(60)
        t.fd(2*n)
        t.lt(180)
        polygon(t,3,n)
        t.rt(120)
        t.bk(2*n)
        t.lt(180+60)
    
    def draw_b(t,n):
        draw_p(t,n)
        t.lt(90)
        t.fd(n)
        arc(t,3*n/5,-120)
        t.rt(60)
        t.fd(6*n/4)
    
    
    def draw_p(t,n):
        vertical(t,n*2)
        t.fd(n)
        t.rt(45)
        arc(t,3*n/4,-90)
        t.rt(45)
        t.fd(n)
        t.lt(90)

    def draw_c(t,n):
        t.pu()
        vertical(t,n*2)
        t.pd()
        t.rt(180)
        arc(t,n,180)

    def draw_d(t,n):
        vertical(t,n*2)
        arc(t,n,-180)

    def draw_e(t,n):
        vertical(t,n)
        backandforth(t,n)
        t.rt(90)
        t.fd(n)
        t.lt(90)
        backandforth(t,n)
        t.rt(90)
        t.fd(n)
        t.lt(90)
        backandforth(t,n)

    def draw_f(t,n):
        vertical(t,n)
        backandforth(t,n)
        t.rt(90)
        t.fd(n)
        t.lt(90)
        backandforth(t,3*n/4)
        t.rt(90)
        t.fd(n)
        t.lt(90)

    def draw_g(t,n):
        move_inclined(t,n,90)
        t.rt(90)
        t.fd(n)
        t.rt(90)
        arc(t,n,-300)

    def draw_h(t,n):
        vertical(t,n)
        move_inclined(t,n/2,-90)
        t.lt(90)    
        backandforth(t,n/2)
        move_inclined(t,n/2,-90)
        t.lt(90)    
        move(t,n/2)
        vertical(t,n)
        vertical(t,-n)

    def draw_i(t,n):
        backandforth(t,n/4)
        t.lt(180)
        backandforth(t,n/4)
        t.lt(180)
        vertical(t,n)
        backandforth(t,n/4)
        t.lt(180)
        backandforth(t,n/4)

def spiral(t):
    time=0
    omega=0.1
    nu=1
    c=1
    for i in range(10000):
        time+=1
        x=(nu*time+c)*math.cos(omega*time)
        y=(nu*time+c)*math.sin(omega*time)
        t.goto(x,y)


def trianglar_spiral(t):
    time=0
    for i in range(10000):
        omega=23
        nu=4
        time+=1
        c=4
        turtle.speed(time+1)
        x=(nu*time+c)*math.cos(omega*time)
        y=(nu*time+c)*math.sin(omega*time)
        
        t.goto(x,y)


# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':
    
    bob = turtle.Turtle()

    #speeds up the drawing speed becareful , it brings bugs when highspeed isnt needed
    #note: speed=0 is more of an instant speed and might cause some glitches
    speed=3
    turtle.tracer(speed,speed)
    turtle.bgcolor('black')
    bob.color('brown')
    #bob.begin_fill()
    
    

    
    #draws a trianglar spiral
    """
    trianglar_spiral(bob)
    """
    
    #draws a spiral
    """
    spiral(bob)
    """

    #draws 3 pies
    """
    move(bob,-100)
    polypie(bob,5,100)
    move(bob,200)
    polypie(bob,6,100)
    move(bob,200)
    polypie(bob,7,100)
    """

    #draws 3 flowers 
    
    move(bob,-200)
    bob.write('x')
    flower(bob,7,200,51.4)
    move(bob,300)
    flower(bob,10,100,80)
    move(bob,300)
    flower(bob,20,300,360/20)
    


    #draws a rose curve
    """
    flower(bob,20,100,370)
    """
    
    # wait for the user to close the window
    turtle.mainloop() 

   

