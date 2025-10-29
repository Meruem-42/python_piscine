from datetime import datetime

kata = (2019, 9, 25, 3, 30)

def main() :
    dt = datetime(*kata)
    print(dt.strftime("%m/%d/%Y %H:%M"))

main()