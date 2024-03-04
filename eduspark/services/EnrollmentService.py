from django.http import HttpResponse, JsonResponse
from ..repositories.EnrollmentRepository import EnrollmentRepository

class EnrollmentService():
    def __init__(self):
        self.enrollment_repository = EnrollmentRepository()
        
    def get_all(self):
        return [enrollment.to_dict() for enrollment in self.enrollment_repository.get_all()]

    def get_by_id(self, id):
        enrollment = self.enrollment_repository.get_by_id(id)
        return enrollment.to_dict() if enrollment else None

    def create(self, course_id, student_id):
        enrollment = self.enrollment_repository.create(course_id, student_id)
        # When attempting to assign instructor as student
        if enrollment == "instructor":
            return "instructor"
        return enrollment

    def update(self, id, course_id, student_id):
        enrollment = self.enrollment_repository.update(id, course_id, student_id)
        return enrollment.to_dict() if enrollment else None

    def delete(self, id):
        return self.enrollment_repository.delete(id)
