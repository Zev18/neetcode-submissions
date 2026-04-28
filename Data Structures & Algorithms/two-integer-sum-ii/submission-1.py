class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = 1

        while left < right and right < len(numbers):
            lnum = numbers[left]
            rnum = numbers[right]
            if lnum + rnum == target:
                return [left + 1, right + 1]
            elif left < right - 1:
                left += 1
            else:
                left = 0
                right += 1
        