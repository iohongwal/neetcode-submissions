class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sdCnt = len(students)
        for sd in sandwiches:
            counter = 0
            while counter < len(students) and students[0] != sd:
                cur = students.pop(0)
                students.append(cur)
                counter +=1

            if students[0] == sd and len(students) > 0:
                students.pop(0)
                sdCnt -= 1
            else:
                break
        return sdCnt
