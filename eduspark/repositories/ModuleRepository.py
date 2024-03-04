from ..models import Module
from .CourseRepository import CourseRepository
from .BaseRepository import BaseRepository

class ModuleRepository(BaseRepository):
    def __init__(self):
        self.course_repository = CourseRepository()
        self.model = Module

    def create(self, title, description, course_id):
        course = self.course_repository.get_by_id(course_id)
        if not course:
            return "Course does not exist"
        module = Module(title=title, description=description, course_id=course.id)
        module.save()
        return module

    def update(self, id, title, description, course_id):
        try:
          module = Module.objects.get(pk=id)
        except Module.DoesNotExist:
            return None
        
        if title:
          module.title = title

        if description:
          module.description = description

        if course_id:
            course = self.course_repository.get_by_id(course_id)
            if not course:
                return "Course does not exist"
            module.course = course

        module.save()
        return module
