class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0: queue.append(i)
        order = []
        while queue:
            current_course = queue.popleft()
            order.append(current_course)
            for next_course in graph[current_course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0: 
                    queue.append(next_course)
        return order if len(order) == numCourses else []
        