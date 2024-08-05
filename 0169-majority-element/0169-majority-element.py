class Solution:
    def majorityElement(self, arr: List[int]) -> int:
        n = len(arr)
        cnt = 0
        el = None

        for i in range (n):
            if cnt == 0:
                cnt = 1
                el = arr[i]
            elif el == arr[i]:
                cnt +=1
            else:
                cnt -=1
        
        cnt1 = 0
        for i in range (n):
            if arr[i] == el:
                cnt1 += 1
        
        if cnt1 > (n//2):
            return el
        
        return -1
        