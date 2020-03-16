#.format example
#cleaning junk example
#case insentative


#open and close a file
fp = open("test.text")
fp.close()

#context manager (with)
with open("test.txt") as fp:
    pass

#write 5 lines to the file using two methods
with open('test.txt', 'w') as fp:
    fp.write('First line\n')
    lines = ['Second line\n', 'Third line\n', 'Fourth line\n', 'Last line\n']
    fp.writelines(lines)

#read the entire file
with open('test.txt', 'r') as fp:
    fp.read()

#reads 5 bytes
with open('test.txt') as fp:
    fp.read(5)

#reads on eline then all lines
with open('test.txt') as fp:
    fp.readline()
    fp.readlines()

#read and print each line single spaced
with open('test.txt') as fp:
    for line in fp:
        print(line, end='') #without the end='', output will double spaced

import os
with open("test.txt") as fp:
    fp.tell()
    fp.read(5)
    fp.tell()
    fr.read()
    fo.tell()
    fp.seek(0, os.SEEK_SET) #reset to begining
    fp.tell()

with open("test.txt") as source, open("copy.txt", 'w') as destination:
    destination.write(source.read())

#write user supplied data to File
with open("user.txt", 'w') as destination:
    while True:
        data = input("Text for file or EOF?")
        if data == 'EOF':
            break
        destination.write(data + \n)

#find total characters
num = len(open('travel_plan.txt').read())

#find total words
num_words = len(open('emotion_words.txt').read().split())

#find number of lines
num_lines = len(open('school_prompt.txt').readlines())

#assign the first 30 characters of school_prompt.txt as a string to the variable beginnning_chars
beginnning_chars = open('school_prompt.txt').read()[:30]

#using the file school_prompt.txt, assign the third word of every line to a list called three
three = []
with open('school_prompt.txt') as fp:
    for line in fp:
        three.append(line.split()[2])

#solutiion 2
three = [line.split()[2] for line in open('school_prompt.txt')]


#create a list called emotions that contains the first word of every line in emotion_words.txt
emotions = []
with open('emotion_words.txt') as fp:
    for line in fp:
        emotions.append(line.split()[0])

#solution 2
emotions = [line.split()[0] for line in open('emotion_words.txt')]

#assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars
first_chars = open('travel_plans.txt').read()[:33]

#efficiency solution
first_chars = open('travel_plans.txt').read([:33])

#using the file school_prompt.txt, if the character p is in a word, then add the word to a list called p_words
p_words = []
with open('school_prompt.txt') as fp:
    for line in fp:
        for word in line.split():
            if 'p' in word:
                p_words.append(word)

#read and return the longest line in the file specificied by the filenmae arguement
with open(filename) as fp:
    longest = ''
    for line in fp:
        if len(line) > len(longest):
            longest = line
return longest

#solution 2
return max(open(filename), key=len)

def writeMe(filename, lst, dict_key_val):
    #given a filename to write to, list of the keys (lst) specifying keys in the dictionary to be written to the file, and a dictionary (dict_key_val) containing
    #values to be written, write the values from the dictionary to the file on  seperate lines in the order of the keys in lst.
    #example:
    #filename = 'output.txt'
    #lst = ['monkey', 'peanut', 'socks']
    #dict_key_val = {'monkey':1, 'drill':2, 'peanut':3, 'doggy':4, 'pirate':5, 'socks':6}
    #contents of output.txt would be:
    #1
    #3
    #6
    with open(filename, 'w') as fp:
        fp.write('\n'.join([dict_key_val[k] for k in lst]))

def myFunc(*args, **kwargs):
    #retunr a list of all of the keywords passed to this function as keyword arguements
    return kwargs.keys()
