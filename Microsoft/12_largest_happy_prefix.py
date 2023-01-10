'''

    --> LeetCode 1392.: --Longest Happy Prefix--

    Ques. String is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).

           Given a string s, return the longest happy prefix of s. Return an empty string "" if no such prefix exists.
 
'''


class Solution:
    def longestPrefix(self, s):
        kBase = 26
        kMod = 1_000_000_007
        n = len(s)
        maxLength = 0
        pow = 1
        prefixHash = 0  # Hash of s[0..i]
        suffixHash = 0  # Hash of s[j..n]

        def val(c):
            return ord(c) - ord('a')

        j = n - 1

        for i in range(n-1):
            prefixHash = (prefixHash * kBase + val(s[i])) % kMod
            suffixHash = (val(s[i]) * pow + suffixHash) % kMod
            pow = pow * kBase % kMod
            if prefixHash == suffixHash:
                maxLength = i + 1
            
            j -= 1

        return s[:maxLength]


p = Solution()
print(p.longestPrefix("level"))