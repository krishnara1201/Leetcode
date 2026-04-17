class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    
        adj_set = collections.defaultdict(list)

        for i, j, w in times:
            adj_set[i].append([j,w])
        
        
        visit = set()
        time = 0
        heap = [(0,k)]
    
        while heap:
            w, u = heapq.heappop(heap)

            if u in visit:
                continue

            visit.add(u)
            for v,wt in adj_set[u]:
                if v not in visit:
                    heapq.heappush(heap, (wt+w,v))
     
            time = w
        
        return time if len(visit) == n else -1
