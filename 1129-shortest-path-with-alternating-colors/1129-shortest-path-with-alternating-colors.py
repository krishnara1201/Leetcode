class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        q = deque()
        visit = set()
        q.append((0, None))
        res = [float("inf")] * n
        dist = 0
        
        adjset_blue = collections.defaultdict(list)
        adjset_red = collections.defaultdict(list)

        for a, b in redEdges:
            adjset_red[a].append(b)
        
        for u, v in blueEdges:
            adjset_blue[u].append(v)

        while q:
            qLen = len(q)
            for i in range(qLen):
                node, prev = q.popleft()
                
                if (node, prev) in visit:
                    continue

                res[node] = min(dist, res[node])
                visit.add((node, prev))

                if not prev:
                    for j in adjset_blue[node]:
                        q.append((j, "blue"))
                    for j in adjset_red[node]:
                        q.append((j, "red"))

                if prev == "red":
                    for j in adjset_blue[node]:
                        q.append((j, "blue"))

                else:
                    for j in adjset_red[node]:
                        q.append((j, "red"))
            dist += 1
        
        for r in range(n):
            if res[r] == float("inf"):
                res[r] = -1
        return res