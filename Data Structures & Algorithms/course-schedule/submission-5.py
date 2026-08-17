class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preCourses = collections.defaultdict(list)

        for course, preCourse in prerequisites:
            preCourses[course].append(preCourse)
        
        visit = set()

        def dfs(course):
            if preCourses[course] == []:
                return True
            if course in visit:
                return False
            
            visit.add(course)
            for pre in preCourses[course]:
                if not dfs(pre):
                    return False
            visit.remove(course)
            preCourses[course] = []
            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return False
        
        return True
