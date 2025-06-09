from collections import namedtuple
def named_tuple(total_student, columns, student_data):
    Student = namedtuple('Student', columns)
    info_student = [Student(*data.split()) for data in student_data]
    avg = sum(int(student.MARKS) for student in info_student) / total_student
    return avg
