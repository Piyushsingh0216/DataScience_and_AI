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

import csv
import os

FILE_NAME = 'students.csv'
FIELDNAMES = ['ID', 'Name', 'Age', 'Grade']

# ==========================================
# Data Handling (Auto-Save/Load)
# ==========================================
def load_students():
    """Loads student records from the CSV file."""
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)

def save_students(students):
    """Automatically saves changes back to the CSV file."""
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(students)

# ==========================================
# Core Operations
# ==========================================
def add_student(students):
    print("\n--- Add New Student ---")
    student_id = input("Enter Student ID: ").strip()
    
    # Check if ID already exists
    if any(s['ID'] == student_id for s in students):
        print("Error: Student ID already exists!")
        return

    name = input("Enter Name: ").strip()
    age = input("Enter Age: ").strip()
    grade = input("Enter Grade: ").strip()
    
    students.append({'ID': student_id, 'Name': name, 'Age': age, 'Grade': grade})
    save_students(students) # Auto-save
    print(f"Success: {name} has been added!")

def search_student(students):
    print("\n--- Search Student ---")
    search_id = input("Enter Student ID to search: ").strip()
    
    for student in students:
        if student['ID'] == search_id:
            print("\nStudent Found:")
            print(f"ID: {student['ID']} | Name: {student['Name']} | Age: {student['Age']} | Grade: {student['Grade']}")
            return
            
    print("Error: Student not found.")

def update_student(students):
    print("\n--- Update Student ---")
    update_id = input("Enter Student ID to update: ").strip()
    
    for student in students:
        if student['ID'] == update_id:
            print(f"Updating records for {student['Name']} (Leave blank to keep current value)")
            
            new_name = input(f"Enter new Name [{student['Name']}]: ").strip()
            new_age = input(f"Enter new Age [{student['Age']}]: ").strip()
            new_grade = input(f"Enter new Grade [{student['Grade']}]: ").strip()
            
            if new_name: student['Name'] = new_name
            if new_age: student['Age'] = new_age
            if new_grade: student['Grade'] = new_grade
            
            save_students(students) # Auto-save
            print("Success: Student details updated!")
            return
            
    print("Error: Student not found.")

def delete_student(students):
    print("\n--- Delete Student ---")
    delete_id = input("Enter Student ID to delete: ").strip()
    
    for i, student in enumerate(students):
        if student['ID'] == delete_id:
            confirm = input(f"Are you sure you want to delete {student['Name']}? (y/n): ").strip().lower()
            if confirm == 'y':
                del students[i]
                save_students(students) # Auto-save
                print("Success: Student deleted.")
            else:
                print("Deletion cancelled.")
            return
            
    print("Error: Student not found.")

def display_all(students):
    print("\n--- All Students ---")
    if not students:
        print("No student records found.")
        return
        
    print(f"{'ID':<8} | {'Name':<20} | {'Age':<5} | {'Grade':<10}")
    print("-" * 52)
    for s in students:
        print(f"{s['ID']:<8} | {s['Name']:<20} | {s['Age']:<5} | {s['Grade']:<10}")

# ==========================================
# Main Application Loop
# ==========================================
def main():
    # Load existing data on startup
    students = load_students()
    
    while True:
        print("\n" + "="*30)
        print("  STUDENT MANAGEMENT SYSTEM")
        print("="*30)
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Update Student Details")
        print("5. Delete Student Record")
        print("6. Exit")
        print("="*30)
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            display_all(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            update_student(students)
        elif choice == '5':
            delete_student(students)
        elif choice == '6':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 6.")

if __name__ == "__main__":
    main()