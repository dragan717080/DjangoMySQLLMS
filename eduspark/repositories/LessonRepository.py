from ..models import Lesson
from .ModuleRepository import ModuleRepository
from .BaseRepository import BaseRepository

class LessonRepository(BaseRepository):
    def __init__(self):
        self.module_repository = ModuleRepository()
        self.model = Lesson

    def create(self, title, content, module_id, order):
        module = self.module_repository.get_by_id(module_id)
        if not module:
            return "Module does not exist"
        lesson = Lesson(title=title, content=content, module_id=module.id, order=order)
        lesson.save()
        return lesson

    def update(self, id, title, content, module_id, order):
        try:
          lesson = Lesson.objects.get(pk=id)
        except Lesson.DoesNotExist:
            return None

        if title:
            lesson.title = title

        if content:
          lesson.content = content

        if order:
            lesson.order = order

        if module_id:
            module = self.module_repository.get_by_id(module_id)
            if not module:
                return "Module does not exist"
            lesson.module = module

        lesson.save()
        return lesson
