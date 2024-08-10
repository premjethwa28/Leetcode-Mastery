class Solution:
    def rob(self, A):
        @cache
        def rob(i):
            return max(rob(i+1), A[i] + rob(i+2)) if i < len(A) else 0
        return rob(0)