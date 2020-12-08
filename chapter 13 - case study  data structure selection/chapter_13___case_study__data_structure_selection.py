import string


#ex 13-1
def word_extractor(filename):
    hist={}
    fp=open(filename)
    for line in fp:
        words_list=line_process(line)
        for word in words_list:
            if word in hist:
                hist[word]+=1
            else:
                hist[word]=1
    return hist
        
def line_process(line):
    line=line.strip()
    #TODO: couldnt strip punctuations out from the lines 
    line.replace('-',' ')
    for char in string.punctuation:
        line.replace(char,' ') 
    line_list=line.split(' ')
    return line_list

print(word_extractor('emma.txt'))    
    
#ex 13-2

