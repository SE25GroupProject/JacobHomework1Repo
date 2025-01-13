def myFunction(arr):
    if len(arr) == 0:
        return 0
    
    if len(arr) % 2 == 1:
        return sum(arr)
    
    else:
        return arr[0] + arr[len(arr) - 1]