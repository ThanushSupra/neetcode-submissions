class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first,second = sorted(s), sorted(t)
        if first == second: return True
        return False