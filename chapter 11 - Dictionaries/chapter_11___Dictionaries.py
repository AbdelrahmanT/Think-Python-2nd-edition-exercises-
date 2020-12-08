#page 128 couldnt solve                         TODO: solve
"""
import string

def histogram(s):
    d=dict.fromkeys(string.ascii_lowercase,0)
    for c in s:
        print(d.get(c,0),c)
        d[c]+=d.get(c,1)
    return d

print(histogram('brontosaurus'))
"""    

import time

def dictionary(fin):
    """takes a file as an input and returns it in a dictionary
    fin:file input"""
    d=dict()
    i=0
    for line in fin:
        word=line.strip()
        d[word]=i
        i+=1
    return d

#start_time=time.time()
#print('aah' in dictionary(fin))
#print(time.time()-start_time)

###############################################ex-11-2###############################################

def invert_dict(d):
    inverse = dict()
    for key in d:
        inverse.setdefault(d[key],key)
    return inverse

#print(invert_dict(d))

###############################################ex-11-3###############################################
ack_known={}

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

def ack_m(m,n):
    if m==0:
        return n+1
    if n==0:
        return ack_m(m-1,1)
    if (m in ack_known) and (n in ack_known):
        return ack_known[m,n]
    else:
        ack_known[m,n] = ack_m(m-1,ack_m(m,n-1))
        return ack_known[m,n]
    
#print(ack(3,6))

###############################################ex-11-4###############################################

def has_duplicates(t):
    """checks wether a list has duplicates using a loop
    t: list
    """
    d=dict()
    for element in t:
        if element in d:
            return True
        else:
            d[element]=1
    return False

def has_duplicates2(t):
    """checks wether a list has duplicates using sets
    t:list
    """
    return len(set(t)) !=len(t)

#t=list(range(29))
#t+=[23]
#print(has_duplicates2(t))

###############################################ex-11-5###############################################
def rotate_letter(letter,n): 
    """rotates the letter with respect to n (google ceaser cypher)
    letter: letter
    n: rotation factor"""
    n=n%26
    if letter.isupper():
       start=ord('A')
    elif letter.islower():
        start=ord('a')
    else:
        return letter
    alph_index= ord(letter)-start
    letter=chr(((alph_index+n)%26)+ord('a')-1)
    return letter

def rotate_word(word,n):
    res=''
    for letter in word:
        res+=rotate_letter(letter,n)
    return str(res)

fin=open('words.txt')

def rotate_pair():
    d=dictionary(fin)
    d_rotate_pairs={}
    for n in range(1,26):
        d_rotate_pairs[n]=[]
    n=1
    while n<26:
        for word in d:
            rotated= rotate_word(word,n)
            if rotated  in d:
                d_rotate_pairs[n]+=[[word,n,rotate_word(word,n)]]
        n+=1
    return d_rotate_pairs

start_time=time.time()
print(rotate_pair(),time.time()-start_time)