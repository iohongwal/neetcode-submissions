class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        precourse_hash = {i:[] for i in range(numCourses)}
        for course, precourse in prerequisites:
            precourse_hash[course].append(precourse)
        
        #record the course is took
        took_course = set()
        #record the course node is visiting in the current dfs loop
        taking_course = set()

        course_order = []

        def dfs(course):
            #Check if the course is took
            if course in took_course:
                return True

            if course in taking_course:
                return False
            
            taking_course.add(course)

            for precourse in precourse_hash[course]:
                if not dfs(precourse):
                    return False

            taking_course.remove(course)
            took_course.add(course)
            course_order.append(course)

            return True
            
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return course_order
