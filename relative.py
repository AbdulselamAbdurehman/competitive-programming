def relative_sort(arr1, arr2):
    temp = {}
    for i in arr1:
        temp[i] = temp.get(i, 0) + 1
    index = 0
    for j in arr2:
        arr1[index: index+temp[j]] = [j]*temp[j]
        index += temp[j]
        del temp[j]
    for k in sorted(temp.keys()):
        arr1[index: index+temp[k]] = [k]*temp[k]
        index += temp[k]
        del temp[k]
    return arr1
