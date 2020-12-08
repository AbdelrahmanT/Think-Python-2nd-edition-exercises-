fin= open('words.txt')

def has_no_e(word):
    if word.find('e')==-1:
        return True
    return False


#ex9-3
def avoids(word,forbidden):
    for letter in forbidden:
        if letter in word:
            return False
    return True


def avoids_input():
    forbidden=input('Enter your forbidden string:')
    for line in fin:
        word = line.strip() 
        if avoids(word,forbidden)==True:
            print(word)


#ex9-4
def uses_only(word,used):
    for letter in word:
        if letter not in used:
            return False
    return True

def uses_only_input():
    uses=input('Enter the string u wanna use:')
    for line in fin:
        word = line.strip() 
        if uses_only(word,uses)==True:
            print(word)

#ex9-5
def uses_all(word,string):
    for letter in string:
        if letter in word:
            continue
        else:
            return False
    return True
        
def uses_all_input():
    string=input('Enter the string u wanna use:')
    for line in fin:
        word= line.strip()
        if uses_all(word,string)==True:
            print(word)

"""
wrong answer tyvm
def is_abecedarian(word):
    abcd='abcdefghijklmnopqrstuvwxyz'
    n=0

    for letter in abcd:
        for i in word:
            if letter ==i:
                x=True
                continue
            elif x:
                break
            else:
                return x
    return True
                
        

def is_the_list_abecedarian():
    for line in fin:
        word= line.strip()
        if is_abecedarian(word)==True:
            print(word)

is_the_list_abecedarian()
"""


"""
ex 9-5
uses_all_input()
ex 9-4
uses_only_input()
ex 9-2 and less
ewords=0
noewords=0
for line in fin:
    word = line.strip() 
    if has_no_e(word)==True:
        print(word)
        noewords+=1
    else:
        ewords+=1
words=noewords+ewords
noepercent=(noewords/words)*100
print('words with no e are:',noepercent,'%')
"""

# ex9-7

def function_output(function):
    for line in fin:
        word= line.strip()
        if function(word)==True:
            print(word)

def cartalk1(word):
    count=0
    letter=0
    while letter < len(word)-1:
        if word[letter]==word[letter+1]:
            count+=1
            letter+=2
        else:
            count=0
            letter+=1
        if count==3:
           return True
    return False

#function_output(cartalk1)
         
#ex 9-8
def is_palindrome(string):
    return string[::-1]==string

def string_add_one(string):
    string=int(string)
    string+=1
    string=str(string)
    return string

def cartalk2(number):
    number=str(number)
    if is_palindrome(number[2:]) == False:
        return False
    number=string_add_one(number)
    if is_palindrome(number[1:]) == False:
        return False
    number=string_add_one(number)
    if is_palindrome(number[1:5]) == False:
        return False
    number=string_add_one(number)
    if is_palindrome(number) == False:
        return False
    return True

""" BAD IDEA MAX RECURSION REACHED "FATAL ERROR"
def cartalk2_tester(number):
    \""" number must be equal or bigger than 100000 for the function to work properly\"""

    if number>999999:
        print('Done')
        return 0
    number+=1
    if cartalk2(number)== True:
        print(number)
    cartalk2_tester(number)
    """

def cartalk2_tester():
    number = 100000
    while number<999999:
        number+=1
        if cartalk2(number) == True:
            print(number)
    print('Done')

    
#cartalk2_tester()
#print('main')
########################################## END OF EX 9-8 #########################################################
# ex 9-9

def xandy(x,y):
    if  y=='Done' or x=='Done':
        return 'Done'
    if int(x)<99 and int(y)<99:
        x=string_add_one(x)
    elif int(x)>=99 :
        x='1'
        y=string_add_one(y)
    elif int(y)>=99:
        y='Done'
        x=y
    return x, y


def cartalk3():
    count=0
    x='01'
    y='01'
    print(x,y)
    while xandy(x,y)[0]!='Done':
        x=xandy(x,y)[0].zfill(2)
        y=xandy(x,y)[1].zfill(2)
        if x==y[::-1] or int(x)-1==int(y[::-1]):
            count+=1
        if count>=8:
            print('x:',x,'y:',y,'count:',count)
            count=0



cartalk3()

#last exercise' solution is wrong