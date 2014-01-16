import sys, getopt
from string import ascii_lowercase
from collections import Counter

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"ih:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'asci.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'Inputfile: asci.py -i <inputfile> -o <outputfile>'
            print 'Stdin: asci.py -s -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt == '-s':
            inputfile = sys.stdin
    print 'input "', inputfile
    print 'output "', outputfile
    if(inputfile != ''):
        readff(inputfile)


def readff(filed):
    with open(filed) as f:
        print Counter(letter for line in f
                for letter in line)


if __name__ == "__main__":
    main(sys.argv[1:])


#with open(sys) as f:
#    print Counter(letter for line in inf
#            for letter in line)
#f.close()

#if inf is not sys.stdin:
#    inf.close()


