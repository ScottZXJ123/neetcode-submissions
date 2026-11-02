class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        nxt = [[] for _ in range(numCourses)]
        
        for a, b in prerequisites:
            nxt[b].append(a)
            indegree[a] += 1

        q = deque()
        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)
        
        order = []
        while q:
            c = q.popleft()
            order.append(c)
            for a in nxt[c]:
                indegree[a] -= 1
                if indegree[a] == 0:
                    q.append(a)
        return order if len(order) == numCourses else[]
            
            