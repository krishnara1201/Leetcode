class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) == 0 and n == 1:
            return 1
        
        adj_set = {}
        trust_set = {}
        for i, j in trust:
            adj_set[i] = adj_set.get(i, 0) + 1
            adj_set[j] = adj_set.get(j, 0)
            trust_set[i] = trust_set.get(i, 0)
            trust_set[j] = trust_set.get(j, 0) + 1

        print(adj_set)
        for i in adj_set.keys():
            if adj_set[i] == 0 and trust_set[i] == n-1:
                return i
        
        return -1   