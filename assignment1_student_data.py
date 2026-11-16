"""Assignment 1: Student Data Management using Dictionary, Tuple and List.

Structure used:
  Dictionary -> key = Roll Number, value = student record
  Tuple      -> each record is (name, branch, marks_list)  (immutable, so update = replace)
  List       -> marks of the student in different subjects
"""

students = {
    101: ("Amit Sharma", "Computer", [85, 90, 78]),
    102: ("Neha Patil", "IT", [72, 68, 80]),
    103: ("Rahul Verma", "Mechanical", [60, 75, 70]),
}


def display(title):
    print(f"\n--- {title} ---")
    print(f"{'Roll No':<10}{'Name':<15}{'Branch':<12}{'Marks':<20}{'Average'}")
    for roll, (name, branch, marks) in students.items():
        avg = sum(marks) / len(marks)
        print(f"{roll:<10}{name:<15}{branch:<12}{str(marks):<20}{avg:.2f}")


def add_student(roll, name, branch, marks):
    if roll in students:
        print(f"Roll No {roll} already exists!")
    else:
        students[roll] = (name, branch, marks)
        print(f"Student {roll} added.")


def delete_student(roll):
    if roll in students:
        del students[roll]
        print(f"Student {roll} deleted.")
    else:
        print(f"Roll No {roll} not found!")


def update_student(roll, name=None, branch=None, marks=None):
    if roll not in students:
        print(f"Roll No {roll} not found!")
        return
    old_name, old_branch, old_marks = students[roll]
    # Tuples are immutable, so we build a new tuple and replace the old one
    students[roll] = (name or old_name, branch or old_branch, marks or old_marks)
    print(f"Student {roll} updated.")


display("Initial Records")
add_student(104, "Sneha Kulkarni", "Electrical", [88, 92, 85])   # Add
delete_student(102)                                             # Delete
update_student(103, branch="Civil", marks=[65, 78, 74])         # Update
display("Final Records")
