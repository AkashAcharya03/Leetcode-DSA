class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right =longest= 0
        for char in s:
            if char == "(":
                left += 1
            else:
                right += 1
            if left == right:
                longest = max(longest, 2 * right)
            elif right > left:
                left = right = 0
        left = right = 0

        for char in reversed(s):
            if char == ")":
                right += 1
            else:
                left += 1
            if left == right:
                longest = max(longest, 2 * left)
            elif right < left:
                left = right = 0
        return longest
