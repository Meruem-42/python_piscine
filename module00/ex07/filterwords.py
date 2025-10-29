import sys

def main() :
    list_word = sys.argv[1].split()
    try : 
        list_final = [x for x in list_word if len(x) > int(sys.argv[2])]
    except ValueError :
        print("Error")
        return
    print(list_final)

if __name__ == "__main__" :
    if len(sys.argv) != 3 :
        print("ERROR")
    else :
        main()
