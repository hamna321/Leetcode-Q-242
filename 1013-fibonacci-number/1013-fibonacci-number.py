class Solution:
    def fib(self, n: int) -> int:
        res=0
        if n==0:
            return 0
        if n==1:
            return 1
        else:
            res=Solution.fib(self,n-1)+Solution.fib(self,n-2)
        return res