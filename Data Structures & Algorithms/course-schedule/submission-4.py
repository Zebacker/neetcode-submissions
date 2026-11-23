class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        indegree = [0]*numCourses
        for cour, pre in prerequisites:
            graph[pre].append(cour)
            indegree[cour] += 1
        queue = deque()
        for ind in range(numCourses):
            if indegree[ind] == 0: queue.append(ind)
        process = 0
        while queue:
            current_cour = queue.popleft()
            process += 1
            for nextcour in graph[current_cour]:
                indegree[nextcour] -= 1
                if indegree[nextcour] == 0:
                    queue.append(nextcour)
        return process == numCourses

