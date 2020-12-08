import math

def mysqrt(a):
    x=a**0.5
    epsilon= 0.000001
    while True:
        y=(x+a/x)/2
        if abs(y-x)< epsilon:
            return y
        

def test_square_root(a,b):
    print('a   mysqrt(a)    math.sqrt(a)  diff')
    print('-   ---------    ------------  ----')
    space=' '
    a=1
    for i in range(b):
        if i==0:
            continue
        if len(space)<len(str(mysqrt(i))):
            space=space*len(str(mysqrt(i)))
            print(space)
    while a<=b:
        print(a,mysqrt(a),space[0:len(space)-len(str(mysqrt(a)))+1],math.sqrt(a),space[len(str(math.sqrt(a)))+1:],abs(math.sqrt(a)-mysqrt(a)))
        a+=1
        #todo: find why it creates alot of unwanted spaces

#test_square_root(1,9)

def eval_loop():
    string=''
    while True:
        string=input('Enter a string:')
        if string=='done':
            break
        result=eval(string)
        print(result)

    return result

#eval_loop()

def estimate_pi():
    a=(2*(2**0.5))/9801
    k=0
    pi=0
    summation=a*((math.factorial(4*k)*(1103+26390*k))/((math.factorial(4*k)**4)*(396**(4*k))))
    pi+=summation 
    while summation>1e-15:
        k+=1
        summation=a*((math.factorial(4*k)*(1103+26390*k))/((math.factorial(4*k)**4)*(396**(4*k))))
        pi+=summation 
        
    return 1/pi

print(estimate_pi())        