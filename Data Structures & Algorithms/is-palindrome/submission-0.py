class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1

        while L < R:
            # Skip non-alphanumeric on the left
            if not s[L].isalnum():
                L += 1
                continue

            # Skip non-alphanumeric on the right
            if not s[R].isalnum():
                R -= 1
                continue

            # Compare characters
            if s[L].lower() != s[R].lower():
                return False

            L += 1
            R -= 1

        return True
