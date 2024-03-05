from .BaseView import BaseView
from ..repositories.CourseRepository import CourseRepository
from ..HttpUtils import HttpUtils

class CourseView(BaseView):
    def __init__(self, http_method_names):
        self.course_repository = CourseRepository()

    def post(self, request):
        return HttpUtils.get_post_data(
            request,
            id,
            ["title", "description", "instructor_id", "start_date", "end_date"], 
            self.course_repository
        )

    def patch(self, request, id):
        return HttpUtils.get_patch_data(
            request,
            id,
            ["title", "description", "instructor_id", "start_date", "end_date"],
            self.course_repository
        )
