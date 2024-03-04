from ..models import Enrollment, Course, User
from .CourseRepository import CourseRepository
from .UserRepository import UserRepository
from .BaseRepository import BaseRepository

class EnrollmentRepository(BaseRepository):
    def __init__(self):
        self.course_repository = CourseRepository()
        self.user_repository = UserRepository()
        self.model = Enrollment

    def create(self, course_id, student_id):
        # When querying other repository get by id do not wrap in try except
        course = self.course_repository.get_by_id(course_id)
        if not course:
            return "Course does not exist"
        student = self.user_repository.get_by_id(student_id)
        if not student:
            return "Student does not exist"

        # If posted student is an instructor, don't process it
        if student.status == "instructor":
            return "Cannot assign instructor as a student"

        enrollment = Enrollment(course_id=course.id, student_id=student.id)
        enrollment.save()
        return enrollment

    def update(self, id, course_id, student_id):
        try:
            enrollment = Enrollment.objects.get(pk=id)
        except Enrollment.DoesNotExist:
            return "Enrollment does not exist"
        
        if course_id:
            course = self.course_repository.get_by_id(course_id)
            if not course:
                return "Course does not exist"
            enrollment.course = course

        if student_id:
            student = self.student_repository.get_by_id(student_id)
            if not student:
                return "Student does not exist"
            enrollment.student = student

        enrollment.save()
        return enrollment
