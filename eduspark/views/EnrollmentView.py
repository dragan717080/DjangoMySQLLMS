from .BaseView import BaseView
from ..repositories.EnrollmentRepository import EnrollmentRepository
from ..HttpUtils import HttpUtils

class EnrollmentView(BaseView):
    def __init__(self, http_method_names):
        self.enrollment_repository = EnrollmentRepository()

    def post(self, request):
        return HttpUtils.get_post_data(
            request,
            id,
            ["course_id", "student_id"], 
            self.enrollment_repository
        )

    def patch(self, request, id):
        return HttpUtils.get_patch_data(
            request,
            id,
            ["course_id", "student_id"],
            self.enrollment_repository
        )
