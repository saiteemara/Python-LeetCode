class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        count = 0
        len_ = len(pref)
        for i in words:
            if i[:len_] == pref:
                count += 1
        return count