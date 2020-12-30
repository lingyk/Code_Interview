class solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = {}
        for prereq in prerequisites:
            if prereq[0] in graph:
                graph[prereq[0]].append(prereq[1])
            else:
                graph[prereq[0]] = [prereq[1]]
        for course in range(numCourses):
            if self._hasCycle(graph, course, set()):
                return False
        return True
    def _hasCycle(self, graph, course, seen):
        if course in seen:
            return True
        if course not in graph:
            return False
        seen.add(course)
        for neighbor in graph[course]:
            if self._hasCycle(graph, neighbor, seen):
                return True
        seen.remove(course)
        return False
print(solution().canFinish(2, [[1,0]]))

print(solution().canFinish(2, [[1,0],[0,1]]))