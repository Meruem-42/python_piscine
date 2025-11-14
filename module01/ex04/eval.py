

class Evaluator() :
    def zip_evaluate(coefs, words) :
        if len(coefs) != len(words) :
            return -1
        return sum(coef*len(word) for coef, word in zip(coefs, words))
    
    def enumerate_evaluate(coefs, words) :
        if len(coefs) != len(words) :
            return -1
        return sum(coef*len(words[i]) for i, coef in enumerate(coefs))


# def main() :
#     words = ["Le", "Lorem", "Ipsum", "est", "simple"]
#     coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
#     print(Evaluator.zip_evaluate(coefs, words))


# main()