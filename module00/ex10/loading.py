from tqdm import tqdm
import time



def ft_progress(listy) :
    for i in tqdm(
        listy, 
        desc="Loading",
        ):
        yield i
        time.sleep(0.0001)

def main() :
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        pass
        time.sleep(0.01)
    print()
    print(ret)

if __name__ == "__main__" :
    main()