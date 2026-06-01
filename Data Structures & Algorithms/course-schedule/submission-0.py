class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for course, preCourse in prerequisites:
            preMap[course].append(preCourse)

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if preMap[course] == []:
                return True
    
            visited.add(course)
            for preCourse in preMap[course]:
                if not dfs(preCourse): 
                    return False
            visited.remove(course)
            preMap[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course): 
                return False

        return True