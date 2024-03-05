from django.http import HttpResponse, JsonResponse
from .BaseView import BaseView
from ..repositories.LessonRepository import LessonRepository
from ..HttpUtils import HttpUtils

class LessonView(BaseView):
    def __init__(self, http_method_names):
        self.model_repository = self.lesson_repository = LessonRepository()
        super().__init__()

    def post(self, request):
        return HttpUtils.get_post_data(
            request,
            id,
            ["title", "content", "module_id", "order"], 
            self.lesson_repository
        )

    def patch(self, request, id):
        return HttpUtils.get_patch_data(
            request,
            id,
            ["title", "content", "module_id", "order"], 
            self.lesson_repository
        )
