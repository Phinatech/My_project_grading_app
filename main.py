

from grade_book import GradeBook
import re

grade_book = GradeBook()


def get_valid_email():
    # Define a regular expression for validating an Email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    while True:
        email = input("Enter student email: ")
        # Check if the email matches the pattern
        if re.match(pattern, email):
            return email  # Return the valid email and exit the function
        else:
            print("Invalid email format. Please enter a valid email.")


def display_menu():
    print("Welcome to Chinemerem's Grade Book Application!")
    print("Please choose an action:")
    print("1. Add a student")
    print("2. Add a course")
    print("3. Register a student for a course")
    print("4. Calculate student ranking")
    print("5. Search by grade")
    print("6. Generate transcript")
    print("7. Print student list")
    print("8. Print course list")
    print("9. Exit")


while True:
    display_menu()
    choice = input("Enter your choice (1-9): ")

    if choice == "1":
        email = get_valid_email()
        names = input("Enter student names: ")
        grade_book.add_student(email, names)

    elif choice == "2":
        name = input("Enter course name: ")
        trimester = input("Enter course trimester: ")
        credits = int(input("Enter course credits: "))
        grade_book.add_course(name, trimester, credits)

    elif choice == "3":
        student_email = get_valid_email()
        course_name = input("Enter course name: ")
        grade_book.register_student_for_course(student_email, course_name)

    elif choice == "4":
        grade_book.calculate_ranking()
        print("Student ranking calculated successfully.")
  
    elif choice == "5":
        min_grade = float(input("Enter minimum grade: "))
        max_grade = float(input("Enter maximum grade: "))
        students = grade_book.search_by_grade(min_grade, max_grade)
        if students:
            print("Students found:")
            for student, grade in students:
                print(f"Name: {student.names}, Email: {student.email}, Grade: {grade}")
        else:
            print("No students found within the specified grade range.")

    elif choice == "6":
        email = get_valid_email()
        student = next(
            (s for s in grade_book.student_list if s.email == email), None)
        if student:
            grade_book.generate_transcript(student)
        else:
            print("Student not found.")

    elif choice == "7":
        print("Printing student list...")
        print('----------------------------------------------------')
        for student in grade_book.student_list:
            print(f"Name: {student.names}", f"Email: {student.email}")
        print('----------------------------------------------------')

    elif choice == "8":
        print("Printing course list...")
        print('----------------------------------------------------')
        for course in grade_book.course_list:
            print(f"Name: {course.name}", f"Trimester: {course.trimester}")
        print('----------------------------------------------------')

    elif choice == "9":
        print("Exiting Grade Book Application...")
        break

    else:
        print("Invalid choice. Please try again.")

    # Ask if the user wants to perform another action
    while True:
        continue_choice = input("Do you want to perform another action? (yes/no): ").strip().lower()
        if continue_choice == 'yes':
            break  
        elif continue_choice == 'no':
            print("Exiting Grade Book Application...")
            exit() 
        else:
            print("Invalid response. Please enter 'yes' or 'no'.")