from django.http import HttpResponse, JsonResponse
from ..repositories.AssignmentRepository import AssignmentRepository

class AssignmentService():
    def __init__(self):
        self.assignment_repository = AssignmentRepository()

    def get_all(self):
        return [assignment.to_dict() for assignment in self.assignment_repository.get_all()]

    def get_by_id(self, id):
        assignment = self.assignment_repository.get_by_id(id)
        return assignment.to_dict() if assignment else None

    def create(self, title, description, course_id, due_date, max_points):
        return self.assignment_repository.create(title, description, course_id, due_date, max_points)

    def update(self, id, title, description, course_id, due_date, max_points):
        assignment = self.assignment_repository.update(id, title, description, course_id, due_date, max_points)
        return assignment.to_dict() if assignment else None

    def delete(self, id):
        return self.assignment_repository.delete(id)
