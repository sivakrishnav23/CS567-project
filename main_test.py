import unittest


from main import StudentRecordSystem

class TestStudentRecordSystem(unittest.TestCase):
    def setUp(self):
        self.srs = StudentRecordSystem()

    def test_add_student(self):
        self.srs.add_student("101", "John Doe", 18, "A")
        self.assertTrue("101" in self.srs.students)

    def test_update_student(self):
        self.srs.add_student("101", "John Doe", 18, "A")
        self.srs.update_student("101", new_name="John Johnson")
        self.assertEqual(self.srs.students["101"]["name"], "John Johnson")

    def test_delete_student(self):
        self.srs.add_student("101", "John Doe", 18, "A")
        self.srs.delete_student("101")
        self.assertTrue("101" not in self.srs.students)

    def test_search_student(self):
        self.srs.add_student("101", "John Doe", 18, "A")
        self.srs.add_student("102", "Jane Smith", 17, "B")
        results = self.srs.search_student("Jane")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][0], "102")

    def test_mark_attendance(self):
        self.srs.add_student("101", "John Doe", 18, "A")
        self.srs.mark_attendance("101", "2023-01-01")
        self.assertTrue("2023-01-01" in self.srs.students["101"]["attendance"])

    def test_calculate_average_test_scores(self):
        self.srs.add_student("101", "John Doe", 18, "A")
        self.srs.students["101"]["test_scores"] = [90, 85, 92]
        self.srs.add_student("102", "Jane Smith", 17, "B")
        self.srs.students["102"]["test_scores"] = [75, 80, 85]
        avg_scores = self.srs.calculate_average_test_scores()
        self.assertAlmostEqual(avg_scores, 83.5, places=1)

if __name__ == '__main__':
    unittest.main()
