class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = [char.lower() for char in s if char.isalnum()]
        left, right = 0, len(new_str) - 1

        while left < right:
            if new_str[left] != new_str[right]:
                return False
            left, right = left + 1, right - 1
        return True


s = "A man, a plan, a canal: Panama"
obj = Solution()
print(obj.isPalindrome(s))
