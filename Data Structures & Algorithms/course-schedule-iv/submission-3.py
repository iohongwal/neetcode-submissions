class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        precourse_hash = {i:[] for i in range(numCourses)}

        for precourse, course in prerequisites:
            precourse_hash[course].append(precourse)
        
        
        answer = []

        def dfs(query_course, course):
            #Base case:
            if course == query_course:
                return True

            #loop detected
            if course in visited:
                return False
            
            # if course in visiting:
            #     return False

            # visiting.add(course)
            visited.add(course)
            for precourse in precourse_hash[course]:
                if dfs(query_course, precourse):
                    return True
            
            visited.add(course)
            #visiting.remove(course)
            return False

        answer = []
        for precourse, course in queries:
            #Record the visited node
            visited = set()
            #Record the visting node of current dfs loop
            #Aimed to detect looped graph
            #visiting = set()
            answer.append(dfs(precourse, course))
        
        return answer



