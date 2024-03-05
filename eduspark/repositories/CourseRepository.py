from ..models import Course, User
from .UserRepository import UserRepository
from .BaseRepository import BaseRepository

class CourseRepository(BaseRepository):
    def __init__(self):
        self.user_repository = UserRepository()
        self.model = Course

    def create(self, title, description, instructor_id, start_date, end_date):
        instructor = self.user_repository.get_by_id(instructor_id)
        if not instructor:
            return "Instructor does not exist"
        if instructor.status != "instructor":
            return "User is not instructor"
        course = Course(title=title, description=description, instructor_id=instructor.id, start_date=start_date, end_date=end_date)
        course.save()
        return course

    def update(self, id, title, description, instructor_id, start_date, end_date):
        try:
            course = Course.objects.get(pk=id)
        except Course.DoesNotExist:
            return "Course does not exist"

        if title:
            course.title = title

        if description:
            course.description = description

        if instructor_id:
            try:
                instructor = User.objects.get(pk=instructor_id)
                if instructor.status != "instructor":
                    return "User is not instructor"
                course.instructor = instructor
            except User.DoesNotExist:
                return "Instructor does not exist"

        if start_date:
            course.start_date = start_date

        if end_date:
            course.end_date = end_date

        course.save()
        return course
