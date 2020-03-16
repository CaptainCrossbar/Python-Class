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

    '''
    #option 2
    return ' '.join(reversed(sentence.split()))

    #option 3
    words = sentence.split()
    rev = []
    for i in range(len(words)-1,-1,-1):
        rev.append(words[i])
    return ' '.join(rev)
    '''
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

    '''
    #option 2
    return sorted((lst0 + lst1), reverse=True)

    #option 3
    return list(reversed(sorted(lst0+lst1)))
    '''

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

    #return "GO" if (s1+s2+s3)/3 > 50 else "NOGO"
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

    #option 2
    #return [x for x in range(0,limit+1,integer) if x % 2 == 0]
    '''
    #option 3
    multiples = []
    for i in range(0, limit + 1):
        if (i % integer == 0) and ( i % 2 == 0):
            multiples.append(i)
    return multiples
    '''
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

    '''
    #option 2
    file1 = open(f0)
    data1 = file1.readlines()
    file2 = open(f1)
    data2 = file2.readlines()
    ans = []
    zipped = list(zip(data1,data2))
    for index,value in enumerate(zipped):
        if value[0] != value[1]:
            ans.append(index)
    return ans

    #option 3
    with open(f0) as file0, open(f1) as file1:
        return [ln for ln,lines in enumerate(zip(file0,file1)) if lines[0] != lines[1]]

    '''
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

    '''
    #option 2
    seen = set()
    for i in lst:
        if i in seen:
            return i
        else:
            seen.add(i)

    #option 3
    #return [n for i,n in enumerate(lst) if n in set(lst[:i])][0]

    #option 4
    #return [n for i,n in enumerate(lst) if n in lst[:i]][0]
    '''

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

    '''
    #option 2
    return len(min(strng.split(' '), key=len))

    #option 3
    return min([len(w) for w in strng.split()])
    '''
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

    '''
    #option 2
    #return chr(int(''.join([c for c in strng if c.isnumeric()])))

    #option 3
    import string
    chars = []
    for c in strng:
        if c in string.digits():
            chars.append(c)
    return chr(int(''.join(chars)))
    '''
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

    '''
    #option 2
    return [arr[x] for x in range(1,len(arr)) if arr[x-1] + 1 != arr[x]] [0]

    #option 3
    for i in range(0,len(arr)):
        if arr[i] +1 == arr[i+1]:
            pass
        else:
            return arr[i] + 2
    return None

    #option 4
    one_by_one = arr.pop(0)
    for numbers in arr:
        one_by_one += 1
        if numbers != one_by_one:
            return numbers
    return None

    #option 5
    for i, num in enumerate(arr):
        if i != 0:
            if arr[i] - 1 != arr[i-1]:
                return num
    return None

    #option 6
    for i range(arr[0], arr[-1]):
        if arr[i] != i:
            return arr[i]
    return None

    #option 7
    return [arr[i] for i in range(arr[0], arr[-1]) if arr[i] != i][0]
    '''
    pass
