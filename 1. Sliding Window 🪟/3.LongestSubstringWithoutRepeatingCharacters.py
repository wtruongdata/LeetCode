class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        last_pos={}
        output = 0
        left = 0
        for right in range(len(s)):
            char = s[right]
            if char in last_pos and last_pos[char]>=left:
                left = last_pos[char]+1
            
            last_pos[char] = right

            output = max(output,right-left+1)
        return output
            
        