import sys
import math

def main() :
    try :
        print ("Sum : ", int(sys.argv[1]) + int(sys.argv[2]))
        print ("Difference : ", int(sys.argv[1]) - int(sys.argv[2]))
        print ("Product : ", int(sys.argv[1]) * int(sys.argv[2]))
        try :
            print ("Quotient : ", int(sys.argv[1]) / int(sys.argv[2]))
        except ZeroDivisionError :
            print("Quotient : impossible")
        try :
            print ("Remainder : ", int(sys.argv[1]) % int(sys.argv[2]))    
        except ZeroDivisionError :
            print ("Remainder : impossible")    
    except ValueError :
        print ("only intergers")    



if __name__ == "__main__" :
    if (len(sys.argv) == 3) :
        main()
    elif (len(sys.argv) != 1 and len(sys.argv) != 3) :
        print("wrong number of argument")