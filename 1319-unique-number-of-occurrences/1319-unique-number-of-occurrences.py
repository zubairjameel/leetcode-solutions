class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        occur = list(freq.values())
        return len(occur) == len(set(occur))
        