class Solution:
    def merge(self, arr1: List[int], n: int, arr2: List[int], m: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = n - 1
        j = m - 1
        k = m + n -1

        # Swap the elements until arr1[left] is smaller than arr2[right]:
        while i >= 0 and j >= 0:
            if arr1[i] > arr2[j]:
                arr1[k] = arr1[i]
                i -= 1
                
            else:
                arr1[k] = arr2[j]
                j -= 1
            k -= 1

        while j >= 0:
            arr1[k] = arr2[j]
            j -= 1
            k -= 1