import string


#ex 13-1

def words_frequency(fin):
    """ returns a histogram with the frequency of each word in file
    fin: file input"""
    hist={}
    for line in fin:
        words_list=line_process(line)
        for word in words_list:
            if word in hist:
                hist[word]+=1
            else:
                hist[word]=1
    if '' in hist.keys():
        hist.pop('')
    return hist
        
def line_process(line):
    """takes a line and returns a list of the words in the line // also removes punctuations
    line: string"""
    line=line.strip()
    for char in string.punctuation:
        line= line.replace(char,' ') 
    line_list=line.split(' ')
    for blank in string.whitespace:
        if blank not in line_list:
            continue
        line_list.remove(blank)
    if '' in line_list:
        line_list.remove('')
    return line_list

#print(words_frequency(open('emma.txt')))    
    
#ex 13-2
#print(words_frequency(open('susan.txt')))

#ex 13-3

def frequent_20words(filename):
    """returns a dictionary with the top 20 most used words as values and their rank as a key
    filename: name of the text file"""
    fin=open(filename)
    hist=words_frequency(open(filename))
    top_20={}
    for ranked_v in hist:
        rank=len(hist)
        for v in hist:
            if ranked_v>v:
                rank-=1
        if rank<=20:
            top_20[rank]=ranked_v
    return top_20

#print(frequent_20words('emma.txt'))

#ex 13-4

def obscure_words(filename):
    """returns a dictionary with obscure words in a file
    filename: file with text"""
    text_list= list(words_frequency(open(filename)).keys())
    fin=open('words.txt')
    words_list=list(words_frequency(fin).keys())
    t=[]
    for s in text_list:
        if s.lower() not in words_list:
            t+=[s]
    return t
    

#print(obscure_words('emma.txt'))

#ex 13-5

import random
import itertools

def histogram(s):
    d={}
    for c in s:
        if c in d:
            d[c]+=1
        else:
            d[c]=1
    return d

def choose_from_hist(hist):
    t=[]
    for k,v in hist.items():
        for i in range(v):
            t+=[k]
    return random.choice(t)

print(choose_from_hist(histogram('aaabbc')))