class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #create adjancet list to link prerequisit course and the course
        preCourse = {i:[] for i in range(numCourses)}

        for course, pre_course in prerequisites:
            preCourse[course].append(pre_course)

        visited = set()

        def dfs(course):
            #check if loop
            if course in visited:
                return False
            #if no prerequisites
            if not preCourse[course]:
                return True
            
            visited.add(course)

            for pre_course in preCourse[course]:
                #check if the prerequisites is in loop
                if not dfs(pre_course):
                    return False

            visited.remove(course)
            #clear the prerequisites list if the course is not in loop
            preCourse[course] = []
            return True
                
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
