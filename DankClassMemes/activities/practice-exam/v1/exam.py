#!/usr/bin/env python3

def q1(floatstr):
    #complete
    '''
    TLO: 112-SCRPY002, LSA 3,4
    Given the floatstr, which is a comma separated string of
    floats, return a list with each of the floats in the
    argument as elements in the list.
    '''

    ret = []
    nls = []

    ret = floatstr.split(',')

    for x in ret:
        nls.append(float(x))

    return nls

    pass

def q2(*args):
    #complete
    '''
    TLO: 112-SCRPY006, LSA 3
    TLO: 112-SCRPY007, LSA 4
    Given the variable length argument list, return the average
    of all the arguments as a float
    '''

    '''
    ret = []
    counter = 0
    sum = 0
    avg = 0

    for x in len(args):
        counter = len(args)
        sum += x[args]

    avg = sum / counter

    return avg
    '''
    return sum(args) / len(args)

    pass

def q3(lst,n):
    #complete
    '''
    TLO: 112-SCRPY004, LSA 3
    Given a list (lst) and a number of items (n), return a new
    list containing the last n entries in lst.
    '''
    new_lst = []
    new_lst = lst[-n:]
    return new_lst
    pass

def q4(strng):
    #complete
    '''
    TLO: 112-SCRPY004, LSA 1,2
    TLO: 112-SCRPY006, LSA 3
    Given an input string, return a list containing the ordinal numbers of
    each character in the string in the order found in the input string.
    '''

    ret = []

    for char in strng:
        ret.append(ord(char))
    return ret
    pass

def q5(strng):
    #complete
    '''
    TLO: 112-SCRPY002, LSA 1,3
    TLO: 112-SCRPY004, LSA 2
    Given an input string, return a tuple with each element in the tuple
    containing a single word from the input string in order.
    '''

    return tuple(strng.split(' '))
    pass

def q6():
    '''
    TLO: 112-SCRPY006, LSA 4
    Given an input string similar to the below, craft a regular expression
    pattern to match and extract the date, time, and temperature in groups
    and return this pattern. Samples given below.
    Date: 12/31/1999 Time: 11:59 p.m. Temperature: 44 F
    Date: 01/01/2000 Time: 12:01 a.m. Temperature: 5.2 C
    '''
    pass

def q7(filename):
    #complete
    '''
    TLO: 112-SCRPY005, LSA 1
    Given a filename, open the file and return the length of the first line
    in the file excluding the line terminator.
    '''
    with open() as fp:
        data = fp.readlines()

    return len(data[0])-1
    pass

def q8(filename,lst):
    #complete
    '''
    TLO: 112-SCRPY003, LSA 1
    TLO: 112-SCRPY004, LSA 1,2
    TLO: 112-SCRPY005, LSA 1
    Given a filename and a list, write each entry from the list to the file
    on separate lines until a case-insensitive entry of "stop" is found in
    the list. If "stop" is not found in the list, write the entire list to
    the file on separate lines.
    '''
    file = open(filename, 'w')
    for x in lst:
        if 'stop' not in x.lower():
            file.write(x + '\n')
        else:
            break
    file.close()
    pass

def q9(miltime):
    #complete
    '''
    TLO: 112-SCRPY003, LSA 1
    Given the military time in the argument miltime, return a string
    containing the greeting of the day.
    0300-1159 "Good Morning"
    1200-1559 "Good Afternoon"
    1600-2059 "Good Evening"
    2100-0259 "Good Night"
    '''

    if int(miltime) >= 300 and int(miltime) <= 1159:
        return 'Good Morning'
    elif int(miltime) >= 1200 and int(miltime) <= 1559:
        return 'Good Afternoon'
    elif int(miltime) >= 1600 and int(miltime) <= 2059:
        return 'Good Evening'
    else:
        return 'Good Night'

    pass

def q10(numlist):
    #complete
    '''
    TLO: 112-SCRPY003, LSA 1
    TLO: 112-SCRPY004, LSA 1
    Given the argument numlist as a list of numbers, return True if all
    numbers in the list are NOT negative. If any numbers in the list are
    negative, return False.
    '''

    for x in numlist:
        if x >= 0:
            return True
        else:
            return False
    pass
