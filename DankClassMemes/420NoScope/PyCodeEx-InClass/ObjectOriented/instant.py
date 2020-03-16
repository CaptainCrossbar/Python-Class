class MyClass:
    #class attributes, shared by all instances
    first = 'Albert'
    last = 'Einstein'

    #method, member function
    def print_name(self):
        print('{}, {}'.format(self.last, self.first))

if __name__ == '__main__':
    me = MyClass()
    my = Myclass()
    me.last = 'Dumas' # creates a new instance attribute
    me.print_name() #dumas, albert
    my.print_name() #einstein, albert 
