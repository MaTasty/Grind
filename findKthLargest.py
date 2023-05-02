# given arr, k, return kth largest element 
# O(n) complexity 
# minheap that only keeps k values at most
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums: 
            if len(heap)<k: 
                heapq.heappush(heap, num)
            elif heap[0]<num: 
                heapq.heappushpop(heap, num)
        return heap[0]
