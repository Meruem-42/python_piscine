kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

def main() :
    for key, value in kata.items() :
        print(key ," was created by ", value)

main()