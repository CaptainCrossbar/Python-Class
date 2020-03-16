#Exam Topics:

#1. Perform a calculation given one or more arguments and a     formula.

'''
example:
def q1(lenght,width):
    #given the length and width of a rectangle, calculate and return its surface area. A = L * W
'''
def q1(length, width):
    return length * width

#2. Determine certain properties of an IPv4 address.
'''
example:
given an ipv4 address as a string in dotted decimal notation, retunr true idf the address is a private address begginning with 192.168, otherwise return False
'''
def q2(addr):
    add_lst = addr.split('.')
    if addr_lst[0] == '192' and addr_lst[1] == '168':
        return True
    else:
        return False

#3. Correlate information, i.e. map.
def q3(lst):
    #given a list of comma separated floats as strings, return a new list of floats
    return list(map(float,lst))

#4. Construct a complicated string from component parts. str    .format, format()
def q4():
    #prompt the user to enter a number and ensure only numbers were entered by removing everything else. convert the final number to an integer
    nums = []
    user = input("Enter a whole number: ")
    if not user.isnumeric():
        for ch in user:
            if ch.isnumeric():
                nums.append(ch)
        nums_str = ''.join(nums)
        return int(nums_str)
    else:
        return int(user)

#5. Filter and convert data.
def q5(make,model,year):
    #print a sentence formatted as follows by using this functions input pararmeters: I drive a (year) (make) (model)
    print("I drive a {} {} {}.".format(year,make,model)) #[0] takes first character

#6. File IO
def q6():
    #open the file provided and print the 3rd line
    with open(filename) as fp:
        for _ in range(3):
            line = fp.readline()
        print(line)

#7. Deconstruct a string into component parts. split(), join    (), slicing
def q7(email_addr):
    #given an email, deconstruct it into a list
    email_split = email_addr.split('@')
    email_join = '.'.join(email_split)

    return email_join.split('.')

    #or

    #dots = email_addr.replace('@','.')
    #return dots.split('.')

#8. Construct a dictionary.
def q8(strng):
    #given a string, return a dictionary that contains all of the characters from the string as keys with values that represent the number of times that character occurred
    d = {}
    for ch in strng:
        d[ch] = d.get(ch,0) + 1
    return d

#9. Construct a tuple.
def q9():
    #retrun a tuple with the day of the week as the first element and the day of the week reversed as the second element.
    return ('Friday' , 'yadirF')

#10. Try an operation and if it fails do something else.
def q10():
    #attempt to open the file provided. if you open the file successfully, return true, else return false
    try:
        open(filename)
    except:
        retrun False
    return True

#11. Perform an operation on variable length arguments.
def q11(*args):
    #inspect the arguments provided and return true if one of the arguments is a 7, otherwise return false
    for n in args:
        if n == 7:
            return True
    return False

#12. Socket IO.
def q12():
    #connect to the server located by the given argument using ipv4 and tcp. send the bytes object b'hello'. recieve and return the entire respomse from the server as bytes or bytearray object
    s = socket.socket()
    s.connect((address,port))
    s.sendall(b'hello')
    msg = bytearray()
    data = s.recv(1)
    while data:
        msg.extend(data)
        data = s.recv(1)
    return msg

#13. Define a class according to a specification. OOP
class blallon:
    def __init__(self):
        self.altitude = 0

    def climb(self):
        self.altitude += 1

    def dive(self):
        if self.altitude > 0:
            self.altitude -= 1

    def crashland(self):
        self.altitude = 0

    def setaltitude(self,newaltitude):
        if newaltitude >= 0:
            self.altitude = newaltitude

    def getaltitude(self):
        return self.altitude

    def __str__(self):
        return 'Current altitude: {}'.format(self.altitude)

if __name__ == '__main__':
    b = balloon()

#14. Bitwise operators.
def q14(var1, flag, class_size):
    #create and return ret based off following conditions for bits
    ret = 0
    if var1 == '':
        ret |= 0x1
    if flag:
        ret |= 0x20
    if class_size > 10:
        ret |= 0x100
    return ret
    pass
