class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        processed = 0
        queue = deque()
        for ind in range(numCourses):
            if indegree[ind] == 0: queue.append(ind)
        while queue:
            current_course = queue.popleft()
            processed += 1
            for next_course in graph[current_course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0: 
                    queue.append(next_course)
        return processed == numCourses

