class StudentRecordSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age, grade):
        if student_id not in self.students:
            self.students[student_id] = {'name': name, 'age': age, 'grade': grade, 'attendance': {}, 'test_scores': []}
            print(f"Student {name} added successfully.")
        else:
            print(f"Student with ID {student_id} already exists.")

    def update_student(self, student_id, new_name=None, new_age=None, new_grade=None):
        if student_id in self.students:
            student = self.students[student_id]
            if new_name:
                student['name'] = new_name
            if new_age:
                student['age'] = new_age
            if new_grade:
                student['grade'] = new_grade
            print(f"Student information updated successfully.")
        else:
            print(f"Student with ID {student_id} not found.")

    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print(f"Student with ID {student_id} deleted successfully.")
        else:
            print(f"Student with ID {student_id} not found.")

    def search_student(self, keyword):
        results = []
        for student_id, student_info in self.students.items():
            if keyword.lower() in student_info['name'].lower() or keyword == student_id:
                results.append((student_id, student_info))
        return results if results else []  # Return an empty list if no results are found

    def calculate_gpa(self, student_id):
        if student_id in self.students:
            test_scores = self.students[student_id]['test_scores']
            if test_scores:
                average_score = sum(test_scores) / len(test_scores)
                gpa = 4.0 * (average_score / 100)
                return gpa
            else:
                return 0.0  # Return a default value when there are no test scores
        else:
            return None
        
    def display_student_details(self, student_id):
        if student_id in self.students:
            student_info = self.students[student_id]
            print(f"Student ID: {student_id}")
            print(f"Name: {student_info['name']}")
            print(f"Age: {student_info['age']}")
            print(f"Grade: {student_info['grade']}")
            print(f"Attendance: {student_info['attendance']}")
            print(f"Test Scores: {student_info['test_scores']}")
        else:
            print(f"Student with ID {student_id} not found.")

    def generate_student_reports(self):
        for student_id, student_info in self.students.items():
            gpa = self.calculate_gpa(student_id)
            if gpa > 0.0:
                print(f"Student ID: {student_id}, Name: {student_info['name']}, GPA: {gpa:.2f}")

    def mark_attendance(self, student_id, date):
        if student_id in self.students:
            if date not in self.students[student_id]['attendance']:
                self.students[student_id]['attendance'][date] = True
                print(f"Attendance marked for student {student_id} on {date}.")
            else:
                print(f"Attendance for student {student_id} on {date} already marked.")
        else:
            print(f"Student with ID {student_id} not found.")

    def calculate_average_test_scores(self):
            total_scores = 0
            total_students = 0
            for student_id, student_info in self.students.items():
                test_scores = student_info['test_scores']
                if test_scores:
                    total_scores += sum(test_scores)
                    total_students += 1

            if total_students > 0:
                average_score = total_scores / total_students
                return average_score
            else:
                return None


# Example Usage:
# Initialize the StudentRecordSystem
srs = StudentRecordSystem()

# Add students
srs.add_student("101", "John Doe", 18, "A")
srs.add_student("102", "Jane Smith", 17, "B")

# Update student information
srs.update_student("101", new_name="John Johnson")
srs.update_student("102", new_grade="A+")

# Delete a student
srs.delete_student("101")

# Search for students
search_results = srs.search_student("Jane")
print("Search Results:")
for student_id, student_info in search_results:
    print(f"Student ID: {student_id}, Name: {student_info['name']}")

# Calculate GPA
gpa = srs.calculate_gpa("102")
print(f"GPA for student 102: {gpa:.2f}")

# Display student details
srs.display_student_details("102")

# Generate student reports
srs.generate_student_reports()

# Mark attendance
srs.mark_attendance("102", "2023-01-01")

# Calculate average test scores
srs.calculate_average_test_scores()
