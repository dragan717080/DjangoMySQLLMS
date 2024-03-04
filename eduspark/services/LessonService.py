from django.http import HttpResponse, JsonResponse
from ..repositories.LessonRepository import LessonRepository

class LessonService():
    def __init__(self):
        self.lesson_repository = LessonRepository()
        
    def get_all(self):
        return [lesson.to_dict() for lesson in self.lesson_repository.get_all()]

    def get_by_id(self, id):
        lesson = self.lesson_repository.get_by_id(id)
        return lesson.to_dict() if lesson else None

    def create(self, title, content, module_id, order):
        return self.lesson_repository.create(title, content, module_id, order)

    def update(self, id, title, content, module_id, order):
        lesson = self.lesson_repository.update(id, title, content, module_id, order)
        return lesson.to_dict() if lesson else None

    def delete(self, id):
        return self.lesson_repository.delete(id)
