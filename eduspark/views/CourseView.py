from .BaseView import BaseView
from ..repositories.CourseRepository import CourseRepository
from ..HttpUtils import HttpUtils

class CourseView(BaseView):
    def __init__(self, http_method_names):
        self.model_repository = self.course_repository = CourseRepository()
        super().__init__()

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
