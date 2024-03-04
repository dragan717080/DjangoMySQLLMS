from django.http import HttpResponse, JsonResponse
from ..repositories.CourseRepository import CourseRepository

class CourseService():
    def __init__(self):
        self.course_repository = CourseRepository()
        
    def get_all(self):
        return [course.to_dict() for course in self.course_repository.get_all()]

    def get_by_id(self, id):
        course = self.course_repository.get_by_id(id)
        return course.to_dict() if course else None

    def create(self, title, description, instructor_id, start_date, end_date):
        return self.course_repository.create(title, description, instructor_id, start_date, end_date)

    def update(self, id, title, description, instructor_id, start_date, end_date):
        course = self.course_repository.update(id, title, description, instructor_id, start_date, end_date)
        return course if course else None

    def delete(self, id):
        return self.course_repository.delete(id)
