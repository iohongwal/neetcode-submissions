class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        #Adjacency List
        precourse_hash = {i:[] for i in range(numCourses)}

        for precourse, course in prerequisites:
            precourse_hash[course].append(precourse)
        
        #Set of ALL its prerequisites
        prerequisite_map = {}

        def dfs(course):
            #Base case:
            if course in prerequisite_map:
                return prerequisite_map[course]

            prerequisite_map[course] = set()

            for precourse in precourse_hash[course]:
                prerequisite_map[course].add(precourse)
                prerequisite_map[course].update(dfs(precourse))
            
            return prerequisite_map[course]

        for c in range(numCourses):
            dfs(c)

        answer = []
        for query_course, course in queries:
            answer.append(query_course in prerequisite_map[course])
        
        return answer



