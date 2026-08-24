class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visit = set()
        
        def dfs(room):
            if room in visit:
                return
            
            visit.add(room)

            for i in rooms[room]:
                dfs(i)


        dfs(0)
        
        return len(visit) == len(rooms)
