def main():
    strng = input("enter pangram candidate: ")
    strng = strng.lower()
    d = {}
    status = True
    words = strng.split()
    exclude = set(string.punctuation) # ignore and delete punctuation
    exclude.add(' ') # ignore and delte space
    strng = ''.join(ch for ch in strng if ch not in exclude)
    length = len(strng)
    for c in strng:
        d[c] = d.get(c, 0) + 1
    for c in strng.ascii_lowercase:
        if d.get(c, 0) == 0:
            status = False
            print('Not Found: {}'.format(c))
    if status:
        print('\n{} pangram:    {}  leters\n'.format(status, length))
    return status

if __name__ == '__main__':
    main()
