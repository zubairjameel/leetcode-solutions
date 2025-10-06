class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        reslen = 0

        for i in range(len(s)):
            # odd length palindrome (center = i)
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > reslen:
                    res = s[left:right+1]
                    reslen = right - left + 1
                left -= 1
                right += 1

            # even length palindrome (center between i and i+1)
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > reslen:
                    res = s[left:right+1]
                    reslen = right - left + 1
                left -= 1
                right += 1

        return res
