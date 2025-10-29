import string
import sys

def print_analyzer(dico_count) :
    print("The string contain", dico_count["printable"]," printable characters")
    print("The string contain", dico_count["lower"]," lower letter(s)")
    print("The string contain", dico_count["upper"]," upper letter(s)")
    print("The string contain", dico_count["punct"]," punctuation mark(s)")
    print("The string contain", dico_count["space"]," space(s)")

def text_analyzer(text=None) :
    """This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""
    count = {"printable" : 0, "upper" : 0, "lower" : 0, "punct" : 0, "space" : 0}

    try :
        if text is None :
            print ("Input a string to analyze")
            text = input(">> ")
        for ch in text :
            if ch.isprintable() :
                if ch.isupper() :
                    count["upper"] += 1
                elif ch.islower() :
                    count["lower"] += 1
                elif ch.isspace() :
                    count["space"] += 1
                elif ch in string.punctuation :
                    count["punct"] += 1
                count["printable"] += 1
        print_analyzer(count)
    except (TypeError, SyntaxError):
        print("argument is not a string")

if __name__ == "__main__" :
    if (len(sys.argv) == 2):
        text_analyzer(sys.argv[1])
    else :
        print("wrong number of argument")