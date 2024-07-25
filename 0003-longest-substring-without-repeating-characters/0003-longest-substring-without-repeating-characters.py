class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mpp = [-1] *256
        left = 0
        right = 0
        n = len(s)
        length = 0

        while right < n:
            if mpp[ord(s[right])] != -1:
                left = max(mpp[ord(s[right])] + 1, left)

            mpp[ord(s[right])] = right

            length = max(length, right - left + 1)
            right += 1

        return length