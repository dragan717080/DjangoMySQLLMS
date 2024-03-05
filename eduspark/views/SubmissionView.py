from .BaseView import BaseView
from ..repositories.SubmissionRepository import SubmissionRepository
from ..HttpUtils import HttpUtils

class SubmissionView(BaseView):
    def __init__(self, http_method_names):
        self.submission_repository = SubmissionRepository()

    def post(self, request):
        return HttpUtils.get_post_data(
            request,
            id,
            ["title", "description", "course_id", "due_date", "max_points"], 
            self.submission_repository
        )

    def patch(self, request, id):
        return HttpUtils.get_patch_data(
            request,
            id,
            ["title", "description", "course_id", "due_date", "max_points"],
            self.submission_repository
        )

