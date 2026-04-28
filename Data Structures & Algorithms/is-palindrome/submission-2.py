class Solution:
    def isPalindrome(self, s: str) -> bool:
        together = ''

        for char in s:
            if char.isalnum():
                together += char.lower()
        
        l = len(together)

        for i in range(l // 2):
            left = together[i]
            right = together[l - i - 1]
            if left != right:
                return False

        return True

        