class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        max_sum = 0
        max_heap = []
        for i in range(len(grid)):
            grid[i].sort(reverse=True)
            for j in range(limits[i]):
                heapq.heappush(max_heap, -grid[i][j])
        
        while k:
            max_sum += heapq.heappop(max_heap)
            k -= 1
        return -m
        ax_sum
