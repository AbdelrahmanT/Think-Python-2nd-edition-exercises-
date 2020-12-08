def compare(x,y):
    if x>y:
        return 1
    elif x<y:
        return -1
    else:
        return 0

def hypotenuse(x,y):
    return(x**2+y**2)**0.5
    
def is_between(x,y,z):
    return x<=y<=z

def b(z):
    prod =  a(z,z)
    print(z, prod)
    return prod

def a(x,y):
    x=x+1
    return x*y

def c(x,y,z):
    total=x+y+z
    square=b(total)**2
    return square

"""
x=1
y=x+1
print(c(x,y+3,x+ys))
"""

def ack(m,n):
    if not (isinstance(m,int) and isinstance(n,int)):
        print("arguements of the ackerman's function must be integers")
        return None
    elif (m<0) or (n<0):
        print("arguements of the ackerman's function can not be negative")
    if m==0:
        return (n+1)
    elif m>0 and n==0:
        return ack(m-1,1)
    elif m>0 and n>0:
        return ack(m-1,ack(m,n-1))

# palindrome palindrome palindrome palindrome palindrome palindrome palindrome palindrome 

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(string):
    if len(string)<2:
        return True
    elif ((len(string)<=3) and (first(string)==last(string))):
        bool=((len(string)<=3) and (first(string)==last(string)))
        return bool
    elif not ((first(string)==last(string)) and is_palindrome(middle(string))):
        return False
    else:
        return True

    # a solution that makes more sense
"""def is_palindrome(word):
    Returns True if word is a palindrome
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))
    """

def is_power(a,b):
    #page 73 exercise 6-4 and finds if a is a power of b
    if (a%b)!=0:
        return False
    elif int((a/b))==1:
        return True
    elif a!=int(a):
        return False
    else:
        print('1',a)
        return is_power(a//b,b)
        
def gcd(a,b):
    """calculates the gcd of 2 numbers 
    a: is bigger than b
    b: is less than a
    """
    if b==0:
        return a
    return gcd(b,a%b)

#gcd(28,20) #= 4
