class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        pointer = len(arr)
        k_val = []
        while pointer > 0:
            max_index = 0
            for i in range(pointer):
                if arr[i] > arr[max_index]:
                    max_index = i
            if max_index != pointer:
                if max_index != 0:
                    arr = arr[:max_index+1][::-1] + arr[max_index+1:]
                    k_val.append(max_index+1)
                arr = arr[:pointer][::-1] + arr[pointer:]
                k_val.append(pointer)
            pointer -= 1
        return k_val
