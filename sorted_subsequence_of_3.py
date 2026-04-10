class Solution:
    def find3Numbers(self, arr):
        n = len(arr)
        if n<3:
            return []
            
        first = float("inf")
        second = float("inf")
        prevFirst = float("inf")
        for i in range(n):
            x = arr[i]
            
            if x <= first:
                first = x
            elif x<= second:
                second = x
                prevFirst = first
            else:
                return [prevFirst, second, x]
                
        return []
        