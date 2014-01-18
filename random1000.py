import random
import sys




def main(argv):
    array = [0] * 10;
    for i in range(10):
        insert(random.randrange(0,10+1))
        print random.randrange(1,10+2)
    print ', '.join(array)

def insert(number):
    print "lol"
    array[number] = array[number] + 1


if __name__ == "__name__":
    main(argv[1:])
