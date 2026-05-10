class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        sdCnt = n
        for sd in sandwiches:
            counter = 0
            while counter < n and students[0] != sd:
                cur = students.pop(0)
                students.append(cur)
                counter +=1
                
            if students[0] == sd:
                students.pop(0)
                sdCnt -= 1
            else:
                break
        return sdCnt
