from .BaseView import BaseView
from ..repositories.AssignmentRepository import AssignmentRepository
from ..HttpUtils import HttpUtils

class AssignmentView(BaseView):
    def __init__(self, http_method_names):
        self.model_repository = self.assignment_repository = AssignmentRepository()
        super().__init__()

    def post(self, request):
        return HttpUtils.get_post_data(
            request,
            id,
            ["title", "description", "course_id", "due_date", "max_points"], 
            self.assignment_repository
        )

    def patch(self, request, id):
        return HttpUtils.get_patch_data(
            request,
            id,
            ["title", "description", "course_id", "due_date", "max_points"], 
            self.assignment_repository
        )
