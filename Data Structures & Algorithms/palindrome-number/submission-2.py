class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        str_x = str(x)
        left = 0
        right = len(str_x) - 1
        while (left < right):
            if (str_x[right] == str_x[right]):
                left += 1
                right -= 1
            return False
        return True
            
