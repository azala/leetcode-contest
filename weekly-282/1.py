class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ret = 0
        for w in words:
            if w.startswith(pref):
                ret += 1
        return ret