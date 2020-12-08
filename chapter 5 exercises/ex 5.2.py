import math

def check_fermat(a,b,c,n):
    """checks fermat's theorm
    the variables corrosponds to the variables in the theorm as in a^n+b^n=c^n
    """
    
    if (math.pow(a,n)+math.pow(b,n)==math.pow(c,n)):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")

def fermat_input():
    """asks the user to input the values of check_fermat function"""
    print("fermat's formula is : a^n+b^n=c^n")
    a=int(input("add a:"))
    b=int(input("add b:"))
    c=int(input("add c:"))
    n=int(input("add n:"))
    if n<=2:
        print("n shall not be less than or equal to 2, try again")
        fermat_input()
        
    check_fermat(a,b,c,n)

fermat_input()
