from ..models import Assignment
from .CourseRepository import CourseRepository
from .BaseRepository import BaseRepository

class AssignmentRepository(BaseRepository):
    def __init__(self):
        self.course_repository = CourseRepository()
        self.model = Assignment

    def create(self, title, description, course_id, due_date, max_points):
        course = self.course_repository.get_by_id(course_id)
        if not course:
            return "Course does not exist"
        assignment = Assignment(title=title, description=description, course_id=course.id, due_date=due_date, max_points=max_points)
        assignment.save()
        return assignment

    def update(self, id, title, description, course_id, due_date, max_points):
        try:
          assignment = Assignment.objects.get(pk=id)
        except Assignment.DoesNotExist:
            return None

        if title:
            assignment.title = title

        if description:
            assignment.description = description

        if due_date:
            assignment.due_date = due_date

        if max_points:
            assignment.max_points = max_points

        if course_id:
            course = self.course_repository.get_by_id(course_id)
            if not course:
                return "Course does not exist"
            assignment.course = course

        assignment.save()
        return assignment
