from collections import Counter as c

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        return [k for k, v in c(A.split() + B.split()).items() if v == 1]