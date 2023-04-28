from datetime import datetime
class Student:
    def __init__(self, name):
        self._name = name
        self._enrollments = []

    def enroll(self, course):
        if isinstance(course, Course):
            enrollment = Enrollment(self, course)
            self._enrollments.append(enrollment)
            course.add_enrollment(enrollment)
        else:
            raise TypeError("course must be an instance of Course")

    def get_enrollments(self):
        return self._enrollments.copy()

class Course:
    def __init__(self, title):
        self._title = title
        self._enrollments = []

    def add_enrollment(self, enrollment):
        if isinstance(enrollment, Enrollment):
            self._enrollments.append(enrollment)
        else:
            raise TypeError("enrollment must be an instance of Enrollment")

    def get_enrollments(self):
        return self._enrollments.copy()

    def get_title(self):
        return self._title

class Enrollment:
    def __init__(self, student, course):
        if isinstance(student, Student) and isinstance(course, Course):
            self._student = student
            self._course = course
            self._enrollment_date = datetime.now()
        else:
            raise TypeError("Invalid types for student and/or course")

    def get_student(self):
        return self._student

    def get_course(self):
        return self._course

    def get_enrollment_date(self):
        return self._enrollment_date