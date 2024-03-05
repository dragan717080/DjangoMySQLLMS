from .BaseView import BaseView
from ..repositories.SubmissionRepository import SubmissionRepository
from ..HttpUtils import HttpUtils

class SubmissionView(BaseView):
    def __init__(self, http_method_names):
        self.model_repository = self.submission_repository = SubmissionRepository()
        super().__init__()

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

