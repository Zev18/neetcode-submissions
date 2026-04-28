class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        numZeroes = 0
        totalProduct = 1

        for n in nums:
            if n != 0:
                totalProduct *= n
            else:
                numZeroes += 1
        
        for n in nums:
            if numZeroes > 1:
                res.append(0)
            elif numZeroes == 1:
                if n == 0:
                    res.append(totalProduct)
                else:
                    res.append(0)
            else:
                res.append(totalProduct // n)

        return res
        