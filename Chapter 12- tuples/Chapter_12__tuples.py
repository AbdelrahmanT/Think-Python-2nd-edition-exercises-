def sumall(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

#print(sumall(2,34,3,2,34,3,2,4,4,2,-2))

#t=list(zip('abc','123','xyz'))
#print(t)
#for i,l,z in t:
#    print(i,l,z)

#from collections import Counter

def histogram(string):
    d={}
    for c in string:
        if c in d:
            d[c]+=1
        else:
            d[c]=1
    return d

def invert_dict(d):
    inverse = dict()
    for key in d:
        inverse.setdefault(d[key],key)
    return inverse

def most_frequent(s):
    """Sorts the letters in s in reverse order of frequency.

    s: string

    Returns: list of letters
    """
    hist = histogram(s)

    t = []
    for x, freq in hist.items():
        t.append((freq, x))

    t.sort(reverse=True)

    res = []
    for freq, x in t:
        res.append(x)

    return res
    

def most_freq(string): #TODO filter out symboles
    t=[]
    
    for key,value in histogram(string).items():
        t.append((value,key))

    t.sort(reverse=True)
    s=''
    
    for number,letter in t:
        s+=letter
    return s

def txt_to_string(file):
    string=''
    for line in file:
        string=string+line.strip().lower().replace(' ','')
    return string

"""#tried to find the most common letters in quran but it was a big big mistake lol
fin_quran=open('quran-simple-clean.txt',encoding='utf-8')
quran_string=txt_to_string(fin_quran)

print(most_freq(quran_string))
"""

#fin_emma=open('emma.txt')

#print(most_freq(txt_to_string(fin_emma)))


######################################################EX-12-2######################################################
#program #1

#from ch10
def is_anagram(string1,string2):
    if(sorted(string1)== sorted(string2)): 
        return True  
    return False

def can_be_spelt_with(file_name): #why does this not work #TODO
    fin=open(file_name)
    d={}
    key=''
    
    fin_list=[]
    for line in fin:
        fin_list+=[line.strip()]

    for string1,i in zip(fin_list,range(1,len(fin_list)+1)):
        fin_list=fin_list[i:]
        for string2 in fin_list:
            if is_anagram(string1,string2):
                anagram=string2
                for letter, i in zip(sorted(string2),range(len(string2))):
                    string2=string2[:i]+letter
                if string2 not in d:
                    d[string2]=[anagram,string1]
                else:
                    d[string2]+=[anagram,string1]
    return d

from collections import defaultdict

def find_anagrams(text_file):
    d={}
    for line in file:
        word=line.strip()
        word_signature=word.sorted()


def signature(s):
    """Returns the signature of this string.

    Signature is a string that contains all of the letters in order.

    s: string
    """
    # TODO: rewrite using sorted()
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t


def all_anagrams(filename):
    """Finds all anagrams in a list of words.

    filename: string filename of the word list

    Returns: a map from each word to a list of its anagrams.
    """
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)

        # TODO: rewrite using defaultdict
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d


def print_anagram_sets(d):
    """Prints the anagram sets in d.

    d: map from words to list of their anagrams
    """
    for v in d.values():
        if len(v) > 1:
            print(len(v), v)





import time
#start_time=time.time()
#print_anagram_sets(all_anagrams('words.txt'))

#print_anagram_sets(can_be_spelt_with('words.txt'))

#print(time.time()-start_time)

######################################################EX-12-3######################################################

def anagram_sets(d):
    """extracts anagram sets from d.

    d: map from signature to list of their anagrams
    returns : a map from signature to set of their anagrams
    """
    for v in d.values():
        if len(v) > 1:
            d_sets[signature(v[0])]=v

    return d_sets
            

def find_metathis_pairs(d):
    """finds metathis pair in a given dictionary
    d: dictionary
    returns: a list of lists of metathis pairs
    """
    for v in d.values():
        for word,i in zip(v,len(v)):
            print('b')
            
def word_reducer2(*s_args):
    reduced=()
    for s in s_args:
        if len(s)<1:
            reduced+=s
        mid=len(s)/2
        if len(s)//2==0:
             reduced+= s.replace(s[int(mid)],''),s.replace(s[int(mid-1)],'')
        else:
             reduced+= s.replace(s[int(mid-0.5)],'')
        reduced+=s.replace(s[int(len(s)-1)],'')
    return reduced,word_reducer(reduced)


def word_reducer(s):
    reduced=[]
    if len(s)<2:
        reduced+= [s]
        return reduced
        mid=len(s)/2
        if len(s)//2==0:
            reduced+= [s.replace(s[int(mid)],''),s.replace(s[int(mid-1)],''),word_reducer(s.replace(s[int(mid)],'')),tuple(word_reducer(s.replace(s[int(mid-1)],'')))]
        else:
            reduced+= [s.replace(s[int(mid-0.5)],''),tuple(word_reducer(s.replace(s[int(mid-0.5)],'')))]
    reduced+=[s.replace(s[int(len(s)-1)],''),tuple(word_reducer(s.replace(s[int(len(s)-1)],'')))]
    return reduced

print(word_reducer('base'))


"""
def word_reducer_end(s):
        return s.replace(len(s)-1,'') 

def word_reducer(*args,t):
    if len(s)<1:
        return s
    for string in *args:
        string_reduced+= word_reducer_mid(s),word_reducer_end(s)

    reduced_strings=word_reducer_mid(s),word_reducer_end(s)
    word_reducer(reduced_strings,t)
 """  



