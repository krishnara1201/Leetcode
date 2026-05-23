class Solution:
    def minimumKeypresses(self, s: str) -> int:
        mapping = [[] for _ in range(9)]
        visit = {}
        count = 0
        res = 0
        sorter = collections.Counter(s)
        s = "".join(sorted(s, reverse = True, key= lambda x:sorter[x]))

        for c in s:
            if c not in visit:
                mapping[count % 9].append(c)
                visit[c] = count % 9
                count += 1
            for i in range(3):
                if mapping[visit[c]][i] != c:
                    res += 1
                else:
                    break
            res += 1
        return res
