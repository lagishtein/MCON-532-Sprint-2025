{
    student_id: {
        "name": student_data["name"],
        "grades": student_data["grades"],
        "gpa": round(sum(student_data["grades"]) / len(student_data["grades"]) / 25, 2)
    }
    for student_id, student_data in {
        1001: {"name": "Alice", "grades": [85, 92, 88, 95, 90]},
        1002: {"name": "Bob", "grades": [78, 85, 80, 88, 82]},
        1003: {"name": "Charlie", "grades": [90, 95, 92, 88, 87]}
    }.items()
}

from pprint import pprint

student_data = {
    student_id: {
        "name": student_data["name"],
        "grades": student_data["grades"],
        "gpa": round(sum(student_data["grades"]) / len(student_data["grades"]) / 25, 2)
    }
    for student_id, student_data in {
        1001: {"name": "Alice", "grades": [85, 92, 88, 95, 90]},
        1002: {"name": "Bob", "grades": [78, 85, 80, 88, 82]},
        1003: {"name": "Charlie", "grades": [90, 95, 92, 88, 87]}
    }.items()
}

pprint(student_data)