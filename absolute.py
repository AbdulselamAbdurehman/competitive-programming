def absoulte_dev(arr):
    total = sum(arr)
    n = len(arr)
    running_total = 0
    for k in range(1, n+1):
        result = total - 2 * running_total + (2 * k - n - 2) * arr[k-1]
        running_total += arr[k-1]
        arr[k-1] = result
    return arr
