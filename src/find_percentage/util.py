def avg_calculation(student_data, query_name):

    student_marks = {name: scores for name, scores in student_data}

    if query_name not in student_marks:
        raise ValueError("Student not found")

    avg = sum(student_marks[query_name]) / len(student_marks[query_name])
    return avg

