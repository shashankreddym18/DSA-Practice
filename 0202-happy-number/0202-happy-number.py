class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1 :
            return True
        if n < 6:
            return False
       
        sumx = 0;
        for i in str(n):
            sumx = sumx + int(i)*int(i);
        
        return self.isHappy(sumx)
     




    #     visit = set()
    #     while n not in visit:
    #         visit.add(n)
    #         n = self.sumOfSquares(n)
    #         if n == 1:
    #             return True
    #         return False
    # def sumOfSquares(self, n : int) -> int:
    #     output = 0
    #     while n:
    #         d = n % 10
    #         d = d ** 2
    #         output += d
    #         n = n // 10
    #     return output
