# for any vowels, insert into a PQ 
# loop twice
class Solution:
    def sortVowels(self, s: str) -> str:
        heap = []
        result = []
        for l in s: 
            if l.lower() in ("a","e","i","o","u"): 
                heapq.heappush(heap, l)
        for l in s: 
            if l.lower() in ("a","e","i","o","u"): 
                result.append(heapq.heappop(heap))
            else: 
                result.append(l)
        return "".join(result)
