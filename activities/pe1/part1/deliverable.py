#!/usr/bin/env python3

def invert(l):
    '''Inverts the given list
    Args:
        l (list): list of strings representing integers in the range [0-255]
    Returns:
        None
    '''
    x = 0
    for x in range(len(l)):
        l[x] = str(255 - int(l[x]))

    pass

def inverted(l):
    '''Returns a new list that is the given list inverted
    Args:
        l (list): list of strings representing integers in the range [0-255]
    Returns:
        list: new list that is the given list inverted
    '''

    newl = l.copy()
    invert(newl)

    return newl

    pass

if __name__ == '__main__':
    pass


"""
Another way of solving it using append
###############################################################################
def invert(l):
    for n in range(0,len(l)):
        l[n] = str(255 - int([n]))
    return None
    pass

def inverted(l):
    newl = []
    for n in l:
        newl.append(str(255-int(n)))
    return newl
    pass

if __name__ == '__main__':
    pass
###############################################################################
"""

"""
Another way of solving it with enumerate
###############################################################################
def invert(l):
    for idx,pixel in emumerate(l):
        l[idx] = str(255-int(pixel))
    pass

def inverted(l):
    return [str(255-int(n)) for n in l]
    pass

if __name__ == '__main__':
    pass
###############################################################################
"""
