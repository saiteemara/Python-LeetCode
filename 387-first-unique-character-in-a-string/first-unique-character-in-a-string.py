class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch,0)+1
        for i,char in enumerate(s):
            if freq[char] == 1:
                return i
        return -1
        