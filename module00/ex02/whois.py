import sys
import math

def main():
    if len(sys.argv) == 2 :
        try :
            if int(sys.argv[1]) % 2 == 0 :
                print("I'm even")
            else :
                print("I'm odd")
        except ValueError :
                print("Problem with the conversion")            
    else :
        print ("Wrong number of arguments")

if __name__ == "__main__" :
    main()