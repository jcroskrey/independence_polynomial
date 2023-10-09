def check_unimodality(array):
    """
    Checks for unimodality of an array. 
    """
    i = 0
    n = len(array)
    if n < 3:
        return False

    # Traverse increasing values
    while i + 1 < n and array[i] <= array[i + 1]:
        i += 1
    
    if i == 0 or i == n - 1:
        return False

    # Traverse decreasing values
    while i + 1 < n and array[i] >= array[i + 1]:
        i += 1

    return i == n - 1 

if __name__ == '__main__':
    res = check_unimodality([23, 93, 151, 125, 55, 12, 1])
    print(res)