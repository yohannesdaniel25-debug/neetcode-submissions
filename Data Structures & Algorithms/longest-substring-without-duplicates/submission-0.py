class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        max_len = 0

        for r in range(len(s)):
            while s[r] in seen: #Checks if duplicates is in seen set
                seen.remove(s[l])
                l+=1        #Moves left up in the string
            seen.add(s[r]) #adds current character
            max_len = max(max_len, r - l +1)

        return max_len