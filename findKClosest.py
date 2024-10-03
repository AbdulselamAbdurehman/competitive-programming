class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #Time: O(logn + k) space: O(k) Result accounted for  
        n = len(arr)

        low, high = 0, n - 1
        insert_position = n
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] >= x:
                insert_position = mid
                high = mid - 1
            else:
                low = mid + 1

        left = insert_position - 1
        right = insert_position

        while right - left - 1 < k:
            if left < 0: 
                right += 1
            elif right >= n: 
                left -= 1
            elif x - arr[left] <= arr[right] - x:
                left -= 1
            else:
                right += 1

        return arr[left + 1:right]
