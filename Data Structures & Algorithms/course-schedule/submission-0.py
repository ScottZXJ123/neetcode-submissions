class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        nxt = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            nxt[b].append(a)
            indegree[a] += 1
        
        q = deque()
        taken = 0

        for a in range(numCourses):
            if indegree[a] == 0:
                q.append(a)

        while q:
            c = q.popleft()
            taken += 1
            for a in nxt[c]:
                indegree[a] -= 1
                if indegree[a] == 0:
                    q.append(a)
        return taken == numCourses
