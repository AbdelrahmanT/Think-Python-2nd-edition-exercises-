
def is_triangle(a,b,c):
    """checks if the 3 sides are can form a triangle or not
    a,b,c: 3 sides of the triangle
    """
    if(a+b)<c:
        print('No')
    elif(b+c)<a:
        print('No')
    elif(c+a)<b:
        print('No')
    else:
        print('Yes')

def is_triangle_input():
    """input function for is_triangle
    """
    print('Enter 3 sides of a triangle to know if it exists or not:-')
    a=int(input('Enter the 1st side :) :'))
    b=int(input('Enter the 2nd side :) :'))
    c=int(input('Enter the 3rd side :) :'))
    is_triangle(a,b,c)
        
is_triangle_input()
