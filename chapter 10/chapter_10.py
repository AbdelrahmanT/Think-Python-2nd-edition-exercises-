# ex 10-1
def nested_sum(t):
    total=0
    for ts in t:
        total+=sum(ts)
    return total

#t=[[3,1],[2],[]]
#print(nested_sum(t))

#################################ex10-2#####################################
def cumsum(t):
    total=0
    new_t=[]
    for ts in t:
        total+=ts
        new_t+=[total]
    return new_t

#t=[3,1,2,5]
#print(cumsum(t))
#################################ex10-3#####################################
def middle(t):
    if len(t)%2==0:
        x=(len(t)-1)/2
        print(x)
        t2=[t[int(x-0.5):int(x+1.5)]]
        return t2
    x=(len(t)/2)-1.5
    t2=[t[int(x)]]
    return t2

#t=[3,1,4,2,2,5,3,45,5,67,4,2,3,4,2,3,42]
#print(middle(t),t)
#################################ex10-4#####################################
def chop(t):
    del t[0],t[len(t)-1]

#t=[3,1,2,5]
#print(chop(t),t)
#print(t)
#################################ex10-5#####################################
def is_sorted(t):
    if t==sorted(t):
        return True
    return False

#t=[3,1,2,5]
#print(is_sorted(t),t)
#t=[1,2,5]
#print(is_sorted(t),t)
#################################ex10-6#####################################
def is_anagram(string1,string2):
    if (len(string1)==len(string2)):
        for letter in range(len(string1)):
            if letter==len(string1)-1:
                return x
            if string1[letter] in string2:
                x=True
                continue
            else:
                return False
    return False

#print(is_anagram('spar','rasp'))
#################################ex10-7#####################################
def has_duplicates(t):
    t2=t[:]
    for i in range(len(t2)):
        x= t2.pop(i)
        if x in t2:
            return True
        t2=t[:]
    return False

#t=[1,2,3,4,5,6,7,8,3,9,'c',0,8]
#print(has_duplicates(t))
#################################ex10-8#####################################
import random as rand
def birthday_paradox():
    t=list(range(1,366))
    true=0
    probability=[]
    birthday_matched=[]
    for i in range(10000):
        babies=[]
        birthday_matched+=[true]
        true=0
        for i in range(23):
            babies+=[rand.randint(1,365)]
        if has_duplicates(babies):
            true+=1
    probability=sum(birthday_matched)/len(birthday_matched)
    return probability        

#print(birthday_paradox())
#################################ex10-9#####################################
import time

def word_list1():
    t=[]
    fin= open('words.txt')
    for line in fin:
        word = line.strip()
        t.append(word)
    return t

def word_list2():
    t=[]
    fin= open('words.txt')
    for line in fin:
        word = line.strip()
        t=t+[word]
    return t

#start_time = time.time()
#t = word_list1()
#elapsed_time = time.time() - start_time

#print(len(t))
#print(t[:10])
#print(elapsed_time, 'seconds')

#start_time = time.time()
#t = word_list2()
#elapsed_time = time.time() - start_time

#print(len(t))
#print(t[:10])
#print(elapsed_time, 'seconds')

#################################ex10-10#####################################
def txt_to_list(file,t):
    """transforms a text file into a sorted list
    prerequesits: t must be empty or not important
    file: text file
    t: list that will contain the file
    """
    for line in file:
        line=line.strip()
        t+=[line]


def reverse_list(t):
    """returns a reversed list"""
    t2=[]
    for string in t:
        string=string.strip()
        t2+=string[::-1]
    return t2

def reverse_pairs(t):
    """returns a list with all reverse pairs"""
    t2=reverse_list(t)
    t3=[]
    for string in t2:
        string=string.strip()
        if string in t:
            t3+=string
    return t3

def in_bisect(t,word):
    """finds a word in a given list at a much faster rate 
    t:list
    word:word"""
    if len(t)==0:
        return False
    x= len(t)//2
    if t[x]==word:
        return True
    if t[x]<word:
        return in_bisect(t[x+1:],word)
    else:
        return in_bisect(t[:x],word)


#t=[2]
#if len(t):
#    print('ass')
#txt_to_list(open('words.txt'),t)
#for word in t:
#    print(in_bisect(t,word))

#################################ex10-11#####################################

def reverse_finder(t):
    """finds reverse pairs in a list and returns a new list with them.
    a reverse pair is words that are reverse of each other string wise.
    t: list"""
    t2=[]
    for i in range(len(t)-1):
        if in_bisect(t,str(t[i])[::-1]):
            t2+=[t[i]]
    return t2

#start_time=time.time()
#t=[]
#txt_to_list(open('words.txt'),t)
#t2=reverse_finder(t)
#print(t2)
#print(time.time()-start_time)

#################################ex10-12#####################################

"""wrong answer
def interlock_pair(t):
    t2=[]
    for i in range(len(t)-2):
        word=str(t[i])+str(t[i+1])
        if in_bisect(t,word):
            t2+=[word]
    return t2

def interlock_trair(t):
    t2=[]
    for i in range(len(t)-2):
        word=str(t[i])+str(t[i+1])+str(t[i+2])
        if in_bisect(t,word):
            t2+=[word]
    return t2

start_time=time.time()
t=[]
txt_to_list(open('words.txt'),t)
print(interlock_trair(t))
print(time.time()-start_time)
"""

def interlock(t):
    t2=[]
    for i in range(len(t)-1):
        if in_bisect(t,str(t[i])[::2]) and in_bisect(t,str(t[i])[1::2]):
            t2+=[t[i]]    
    return t2        

def interlock3(t):
    t2=[]
    for i in range(len(t)-1):
        if in_bisect(t,str(t[i])[::3]) and in_bisect(t,str(t[i])[1::3]) and in_bisect(t,str(t[i])[2::3]) :
            t2+=[t[i]]    
    return t2        

#start_time=time.time()
t=[]
txt_to_list(open('words.txt'),t)
#print(interlock3(t))
#print(time.time()-start_time)
############################################################################################################
start_time=time.time()
print(in_bisect(t,'aah'))
print(time.time()-start_time)