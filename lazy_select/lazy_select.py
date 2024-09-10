import random
from statistics import mode


def lazy_select(S:list, n: int, k: int):

    R = [i for i in S if random.uniform(0, 1)<(1/(n**(0.25)))]
    R.sort()
    
    a = int((n**(0.75))/2 - (5*(n**0.5)))
    b = int((n**(0.75))/2 + (5*(n**0.5)))
    
    S_ = [i for i in S if R[a]<i and R[b] > i]
    S_.sort()
    
    t = sum([1 if i <= R[a] else 0 for i in S])

    return S_[k - t - 1]

def main():
    n = 2**16

    S = random.sample(range(0, 2**17), n)

    print(f'Lazy select algorithm to find the k-th smallest element in a list of size {n}')
    # k = input(f'Enter value of k (Default is {int(n/2)}) - ')
    # k = int(k) if k != '' else n//2
    k = random.randint(0, 2**16)
    print(f'k = {k}')

    k_th = lazy_select(S, n, k)

    print(f'{k}-th smallest element upon running lazy select one time - {k_th}\n')

    sorted_S = sorted(S)
    print(f'{k}-th smallest element using the normal sort method - {sorted_S[k-1]}')
    
if __name__ == "__main__":
    main()