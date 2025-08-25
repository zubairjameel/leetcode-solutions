class Solution:
    def isVowel(self, char):
        return char in "AEIOUaeiou"

    def reverseVowels(self, s: str) -> str:
        s = list(s)  # convert string to list
        left, right = 0, len(s) - 1

        while left < right:
            if not self.isVowel(s[left]):
                left += 1
            elif not self.isVowel(s[right]):
                right -= 1
            else:
                # swap vowels
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        return "".join(s)
