from django.http import HttpResponse, JsonResponse
from ..repositories.ModuleRepository import ModuleRepository

class ModuleService():
    def __init__(self):
        self.module_repository = ModuleRepository()
        
    def get_all(self):
        return [module.to_dict() for module in self.module_repository.get_all()]

    def get_by_id(self, id):
        module = self.module_repository.get_by_id(id)
        return module.to_dict() if module else None

    def create(self, title, description, course_id):
        return self.module_repository.create(title, description, course_id)

    def update(self, id, title, description, course_id):
        module = self.module_repository.update(id, title, description, course_id)
        return module if module else None

    def delete(self, id):
        return self.module_repository.delete(id)
