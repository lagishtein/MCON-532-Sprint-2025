import unittest

class TestStudentData(unittest.TestCase):

    def setUp(self):
        self.student_data = {
            1001: {"name": "Alice", "grades": [85, 92, 88, 95, 90]},
            1002: {"name": "Bob", "grades": [78, 85, 80, 88, 82]},
            1003: {"name": "Charlie", "grades": [90, 95, 92, 88, 87]}
        }

    def test_number_of_students(self):
        self.assertEqual(len(self.student_data), 3)

    def test_student_attributes(self):
        for student_id, student_info in self.student_data.items():
            self.assertIn("name", student_info)
            self.assertIn("grades", student_info)
            self.assertIn("gpa", student_info)

    def test_grades_are_integers(self):
        for student_id, student_info in self.student_data.items():
            for grade in student_info["grades"]:
                self.assertIsInstance(grade, int)

    def test_gpa_calculation(self):
        for student_id, student_info in self.student_data.items():
            expected_gpa = round(sum(student_info["grades"]) / len(student_info["grades"]) / 25, 2)
            self.assertEqual(student_info["gpa"], expected_gpa)

if __name__ == '__main__':
    unittest.main()

#To run the tests, save this code in a file (e.g., test_student_data.py) and run it using the command `python test_student_data.py

