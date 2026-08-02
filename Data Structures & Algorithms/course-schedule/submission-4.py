class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #Initiate the adjance list to link course and its prerequisites
        courseMap = {i:[] for i in range(numCourses)}

        for course, preCourse in prerequisites:
            courseMap[course].append(preCourse)

        visited = set() #loop detector

        def dfs(course):
            if course in visited:
                return False
            #no prerequisites
            if courseMap[course] == []:
                return True
            
            visited.add(course)

            for preCourse in courseMap[course]:
                if not dfs(preCourse):
                    return False
            
            #this course have no conflict loop
            visited.remove(course)
            courseMap[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True