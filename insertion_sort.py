from numpy import random
x = random.randint(1, 100, 30)
print(x)
'''[12, 11, 13, 5, 6] --->[11, 12, 13, 5, 6] ---> [5, 11, 12, 13, 6] ---> [5, 6, 11, 12, 13]'''  
def insertion_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        for r in range(1, len(arr)):
            key = arr[r] #Беремо змінну яку нам треба переставити(якщо менше попередньої)
            l = r - 1 # індекс на 1 менше за поточний r індекс
            while l >= 0 and arr[l] > key: #Якщо ключева змінна змінна з індексом r менша за змінну з індексом l(r-1)
                arr[l + 1] = arr[l]  # місце поточної змінной замінюється на змінну з індексом l(r-1)
                l -= 1 #r-2
            arr[l + 1] = key 
        return arr
print(insertion_sort(x))
        

        
