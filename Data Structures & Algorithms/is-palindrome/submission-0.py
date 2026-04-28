class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphas = set('abcdefghijklmnopqrstuvwxyz1234567890')
        together = ''

        for char in s:
            c = char.lower()
            if c in alphas:
                together += c
        
        l = len(together)

        for i in range(l // 2):
            left = together[i]
            right = together[l - i - 1]
            if left != right:
                return False

        return True

        