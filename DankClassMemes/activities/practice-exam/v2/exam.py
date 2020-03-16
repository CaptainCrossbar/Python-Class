#!/usr/bin/env python3

def q1(sentence):
    #complete
    '''
    Given a string of multiple words separated by single spaces,
    return a new string with the sentence reversed. The words
    themselves should remain as they are. For example, given
    'it is accepted as a masterpiece on strategy', the returned
    string should be 'strategy on masterpiece a as accepted is it'.
    '''
    ret = []
    words = sentence.split()

    for w in words:
        ret.insert(0, w)

    return ' '.join(ret)

    pass

def q2(n):
    #complete
    '''
    Given a positive integer, return its string representation with
    commas seperating groups of 3 digits. For example, given 65535
    the returned string should be '65,535'.
    '''
    return '{:,}'.format(n)
    pass

def q3(lst0, lst1):
    #complete
    '''
    Given two lists of integers, return a sorted list that contains
    all integers from both lists in descending order. For example,
    given [3,4,9] and [8,1,5] the returned list should be [9,8,5,4,3,1].
    The returned list may contain duplicates.
    '''
    lst0.sort()
    lst1.sort()
    ret = lst0 + lst1
    ret.sort()
    ret.reverse()
    return ret
    pass

def q4(s1,s2,s3):
    #complete
    '''
    Given 3 scores in the range [0-100] inclusive, return 'GO' if
    the average score is greater than 50. Otherwise return 'NOGO'.
    '''
    avg = (s1 + s2 + s3) / 3
    if avg > 50:
        return 'GO'
    else:
        return 'NOGO'
    pass

def q5(integer, limit):
    #complete
    '''
    Given an integer and limit, return a list of even multiples of the
    integer up to and including the limit. For example, if integer==3 and
    limit==30, the returned list should be [0,6,12,18,24,30]. Note, 0 is
    a multiple of any integer except 0 itself.
    '''
    ret = [0]
    for x in range(integer,limit+1,integer):
        if x % 2 == 0:
            ret.append(x)

    return ret
    pass

def q6(f0, f1):
    '''
    Given two filenames, return a list whose elements consist of line numbers
    for which the two files differ. The first line is considered line 0.
    '''
    x = open(f0)
    y = open(f1)

    l1 = x.read().split('\n')
    l2 = y.read().split('\n')

    x.close()
    y.close()

    for i,z in enumerate(zip(l1, l2)):
        if z[0] != z[1]:
            yield i
    pass

def q7(lst):
    #complete
    '''
    Return the first duplicate value in the given list.
    For example, if given [5,7,9,1,3,7,9,5], the returned value should
    be 7.
    '''

    dup_lst = []
    for x in lst:
        if x in dup_lst:
            return x
        dup_lst.append(x)

    return None


def q8(strng):
    #complete
    '''
    Given a sentence as a string with words being separated by a single space,
    return the length of the shortest word.
    '''

    ans = 999999999999999999999999999999999999999999999999999999999999999999999
    s = strng.split()
    for word in s:
        if len(word) < ans:
            ans = len(word)

    return ans
    pass

def q9(strng):
    #complete
    '''
    Given an alphanumeric string, return the character whose ascii value
    is that of the integer represenation of all of the digits in the string
    concatenated in the order in which they appear. For example, given
    'hell9oworld7', the returned character should be 'a' which has
    the ascii value of 97.
    '''
    num = ''
    numlst = ['0','1','2','3','4','5','6','7','8','9']
    for ch in strng:
        if ch in numlst:
            num += ch
    return chr(int(num))
    pass

def q10(arr):
    #complete
    '''
    Given a list of positive integers sorted in ascending order, return
    the first non-consecutive value. If all values are consecutive, return
    None. For example, given [1,2,3,4,6,7], the returned value should be 6.
    '''
    x = arr.pop(0)
    for num in arr:
        x += 1
        if num != x:
            return num
    return None
    pass
