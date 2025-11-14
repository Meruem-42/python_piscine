option_lst = ["shuffle", "ordered", "unique"]

def generator(text, sep=" ", option=None) :
    if not isinstance(text, str) or not option in option_lst :
        return (yield "ERROR")
    if not text.isprintable() :
        raise TypeError(f"the text should be only printable characters")
    lst = text.split(sep)
    if(option == "shuffle") :
        for elem in set(lst) :
            yield elem
    elif(option == "ordered") :
        for elem in sorted(lst) :
            yield elem
    elif option == "unique" :
        unique_lst = []
        for elem in lst :
            if not elem in unique_lst :
                unique_lst.append(elem)
                yield elem
    else :
        for elem in lst :
            yield elem

# def main() :
#     text = "Le Lorem Ipsum est simplement du faux texte."
#     for word in generator(text, sep=" ", option="ordered") :
#         print(word)

# main()