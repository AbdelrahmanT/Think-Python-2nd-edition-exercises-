
def find(letter,string,index):
    """find a letter starting from the given index"""
    
    while index<len(string):
        if string[index]==letter:
            return index
        index+=1
    return -1

def count(letter,string):
    # county the amount of letter in string
    count=0
    index=0
    while index<len(string):
        index= find(letter,string,index)
        if index==-1:
            return count
        index+=1
        count+=1
    return count

#name='stop'
#print(name.find('b',0,1))
#'banana'.count('a')

def is_palindrome(string):
    return string[::-1]==string
    
#print(is_palindrome(name))


def any_lowercase2(s):
    for c in s:
        if c.islower():
            return 'True'
        else:
            return 'False'

        if num>122:
            num=num-26

def rotate_word(word,integer):
    #prepares integer to be =[0,25] for easier computation 
    while integer>=26:
        integer-=26
    while integer<0:
        integer+=26
    if integer==0:
        return word
    #prepares string for the encoding loop
    letter=0
    drow=''
    drow=chr(ord(word[letter])+integer)
    letter=1
    while letter<len(word):
        if not ((97<=ord(word[letter])<=122)or (65<=ord(word[letter])<=90)):
            drow=drow[:letter]+chr(ord(word[letter]))
            letter+=1
            continue
        elif ord(word[letter].lower())+integer>122:
            drow=drow[:letter]+chr(ord(word[letter])+integer-26)
            letter+=1
        else:
            drow=drow[:letter]+chr(ord(word[letter])+integer)
            letter+=1
    
    return drow


#print('This is a ROT13 encryptor')   
#string=input('Enter what you wish to encrypt:')
#print(rotate_word(string,13))
#word='BANANA'
#print(word[0].lower())
print(ord('v'))
print(rotate_word('videos are cool',13))
