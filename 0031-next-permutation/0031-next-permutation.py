class Solution:
    def nextPermutation(self, A: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind = -1
        n = len(A)

        for i in range (n-2, -1, -1):
            if A[i] < A[i+1]:
                ind = i
                break
        
        if ind == -1:
            A.reverse()
            return A

        for i in range(n-1, -1, -1):
            if A[i] > A[ind]:
                A[i], A[ind] = A[ind], A[i]
                break
        
        A[ind+1:] = reversed(A[ind+1:])