from django.http import HttpResponse, JsonResponse
from .BaseView import BaseView
from ..services.LessonService import LessonService
from ..HttpUtils import HttpUtils

class LessonView(BaseView):
    def __init__(self, http_method_names):
        self.lesson_repository = LessonService()

    def post(self, request):
        return HttpUtils.get_post_data(
            request,
            id,
            ["title", "content", "module_id", "order"], 
            self.module_repository
        )

    def patch(self, request, id):
        return HttpUtils.get_patch_data(
            request,
            id,
            ["title", "content", "module_id", "order"], 
            self.module_repository
        )
