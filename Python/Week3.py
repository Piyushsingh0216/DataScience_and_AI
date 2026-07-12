class Student:
    """
    Represents an individual student.
    """
    def __init__(self, student_id: str, name: str, grade: str):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def __str__(self):
        # This determines how the object looks when we print() it
        return f"[{self.student_id}] {self.name} (Grade: {self.grade})"


class StudentManager:
    """
    Manages a collection of Student objects.
    """
    def __init__(self):
        # Dictionary to store students: {student_id: Student_Object}
        self.students = {}

    def add_student(self, student_id: str, name: str, grade: str):
        """Adds a new student to the system."""
        if student_id in self.students:
            print(f"⚠️ Error: Student ID '{student_id}' already exists.")
            return
        
        # Create the new Student object and add it to the dictionary
        new_student = Student(student_id, name, grade)
        self.students[student_id] = new_student
        print(f"✅ Added: {new_student.name}")

    def remove_student(self, student_id: str):
        """Removes a student by their ID."""
        if student_id in self.students:
            # .pop() removes the key and returns the value (the Student object)
            removed_student = self.students.pop(student_id)
            print(f"❌ Removed: {removed_student.name}")
        else:
            print(f"⚠️ Error: Student ID '{student_id}' not found.")

    def search_student(self, student_id: str):
        """Searches for and displays a student by their ID."""
        student = self.students.get(student_id)
        if student:
            print(f"🔍 Found: {student}")
        else:
            print(f"⚠️ Not Found: No student matches ID '{student_id}'.")

    def display_all(self):
        """Displays all students currently in the system."""
        if not self.students:
            print("📭 The system is currently empty.")
            return
        
        print("\n--- Current Student Roster ---")
        for student in self.students.values():
            print(student)
        print("------------------------------\n")


# ---------------------------------------------------------
# Execution: Testing the System
# ---------------------------------------------------------
if __name__ == "__main__":
    # 1. Initialize the system
    school = StudentManager()

    # 2. Add Students
    school.add_student("S001", "Alice Smith", "10th")
    school.add_student("S002", "Bob Johnson", "11th")
    school.add_student("S003", "Charlie Brown", "10th")
    
    # Try to add a duplicate ID
    school.add_student("S001", "Duplicate Alice", "12th") 

    # 3. Display All Students
    school.display_all()

    # 4. Search for a Student
    school.search_student("S002")
    school.search_student("S999") # ID that doesn't exist

    # 5. Remove a Student
    print("\n")
    school.remove_student("S003")

    # 6. Final Display to verify removal
    school.display_all()