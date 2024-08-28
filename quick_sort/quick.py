import random

def quick(s:list):
    if len(s) <= 1:
        return s

    x = random.choice(s)

    Y = [i for i in s if i < x]
    Z = [i for i in s if i > x]

    Y_sorted = quick(Y)
    Z_sorted = quick(Z)

    return Y_sorted + [x] + Z_sorted
                     
            

def main():
    print('Quick Sort')
    n = 10
    print(f'n = {n}')
    
    s = random.choices(range(1, 101), k = n) 
    print(f'Unsorted List = {s}')

    sorted_s = quick(s)

    print(f'Sorted List = {sorted_s}')


if __name__  == '__main__':
    main()
