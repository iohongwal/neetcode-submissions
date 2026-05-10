class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        swCnt = len(sandwiches)
        time = len(sandwiches)*len(students)
        while time and sandwiches and students:
            student1st = students.pop(0)
            sandwiches1st = sandwiches[0]
            if student1st == sandwiches1st:
                sandwiches.pop(0)
                swCnt -=1
            else:
                students.append(student1st)
            time -=1
        return swCnt
