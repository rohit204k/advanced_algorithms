import random

def divide(s):
    if len(s) == 1:
        return s
    
    mid = len(s)//2
    left = divide(s[:mid])
    right = divide(s[mid:])
    sorted_s = merge(left, right)

    return sorted_s

def merge(left, right):
    i, j = 0,0
    combined = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            combined.append(left[i])
            i+=1
        else:
            combined.append(right[j])
            j+=1
    
    while i < len(left):
        combined.append(left[i])
        i+=1

    while j < len(right):
        combined.append(right[j])
        j+=1

    return combined

def main():
    print('Merge Sort')
    n = 10
    print(f'n = {n}')
    
    s = random.choices(range(1, 101), k = n) 
    print(f'Unsorted List = {s}')

    sorted_s = divide(s)

    print(f'Sorted List = {sorted_s}')


if __name__  == '__main__':
    main()