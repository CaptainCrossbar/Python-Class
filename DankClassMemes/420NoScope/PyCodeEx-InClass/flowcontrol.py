import time
import sys

if __name__ = '__main__':
    while True:
        try:
            fp = open('test.txt')
        except:
            print('test.txt not found', file = sys.stderr)
            time.sleep(3)
        else:
            break

    for liine in fp:
        print(line, end='')
    fp.close()
