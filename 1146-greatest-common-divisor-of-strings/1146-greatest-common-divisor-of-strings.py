class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        # Find the greatest common divisor of the lengths of the two strings
        gcd_len = math.gcd(len(str1), len(str2))
        
        # The GCD string will be the prefix of str1 up to gcd_len
        return str1[:gcd_len]