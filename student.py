
from course import Course
import random


class Student:
    def __init__(self, email, names, courses_registered=None, GPA=0.0):
        """
        Initialize a new Student object.

        Args:
            email (str): The email of the student.
            names (str): The names of the student.
        """
        self.email = email
        self.names = names
        self.courses_registered = courses_registered if courses_registered is not None else []
        self.GPA = GPA

    def register_for_course(self, course):
        """
        Register the student for a course.

        Args:
            course (dict): A dictionary with course details (name, credits, grade).
        """
        grade = random.randint(40, 100)
        self.courses_registered.append({
            'name': course.name,
            'trimester': course.trimester,
            'credits': course.credits,
            'grade': grade
        })
        

    def calculate_GPA(self):
        total_credits = 0
        total_grade_points = 0
        for course in self.courses_registered:

            total_credits += course['credits']
            total_grade_points += course['credits'] * course['grade']
        GPA = total_grade_points / total_credits if total_credits else 0.0
        return (GPA/100)*5