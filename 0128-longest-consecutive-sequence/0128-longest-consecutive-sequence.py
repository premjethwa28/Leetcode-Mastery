class Solution:


    def longestConsecutive(self, a: List[int]) -> int:
        n = len(a)
        if n == 0:
            return 0

        a.sort()
        longest = 1
        lastSmaller = float('-inf')
        cnt = 0

        for i in range(n):
            if a[i]-1 == lastSmaller:
                cnt += 1
                lastSmaller = a[i]
            elif a[i] != lastSmaller:
                cnt = 1
                lastSmaller = a[i]
            longest = max(longest,cnt)
        return longest