from django.http import HttpResponse, JsonResponse
from ..repositories.SubmissionRepository import SubmissionRepository

class SubmissionService():
    def __init__(self):
        self.submission_repository = SubmissionRepository()
        
    def get_all(self):
        return [submission.to_dict() for submission in self.submission_repository.get_all()]

    def get_by_id(self, id):
        submission = self.submission_repository.get_by_id(id)
        return submission.to_dict() if submission else None

    def create(self, title, content, module_id, order):
        return self.submission_repository.create(title, content, module_id, order)

    def update(self, id, title, content, module_id, order):
        submission = self.submission_repository.update(id, title, content, module_id, order)
        return submission.to_dict() if submission else None

    def delete(self, id):
        return self.submission_repository.delete(id)
