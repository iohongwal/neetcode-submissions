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
            
            visited.add(course)

            for precourse in precourse_hash[course]:
                if dfs(query_course, precourse):
                    return True
            
            return False

        answer = []
        for precourse, course in queries:
            #Record the visited node
            #Aimed to detect looped graph
            visited = set()
            answer.append(dfs(precourse, course))
        
        return answer



