from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        s = sorted(dict(Counter(s)).items(), key=lambda x: (x[1], x[0]), reverse=True)
        return "".join(x[0]*x[1] for x in s)