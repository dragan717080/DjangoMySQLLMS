from .BaseView import BaseView
from ..repositories.ModuleRepository import ModuleRepository
from ..HttpUtils import HttpUtils

class ModuleView(BaseView):
    def __init__(self, http_method_names):
        self.model_repository = self.module_repository = ModuleRepository()
        super().__init__()

    def post(self, request):
        return HttpUtils.get_post_data(
            request,
            id,
            ["title", "description", "course_id"], 
            self.module_repository
        )

    def patch(self, request, id):
        return HttpUtils.get_patch_data(
            request,
            id,
            ["title", "description", "course_id"],
            self.module_repository
        )
