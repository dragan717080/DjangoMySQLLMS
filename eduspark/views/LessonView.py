from django.http import HttpResponse, JsonResponse
from .BaseView import BaseView
from ..services.LessonService import LessonService
from ..Utils import Utils

class LessonView(BaseView):
    def __init__(self, http_method_names):
        self.lesson_service = LessonService()

    def get_all(self):
        return JsonResponse(self.lesson_service.get_all(), safe=False)

    def get_by_id(self, id):
        Lesson = self.lesson_service.get_by_id(id)
        return JsonResponse(Lesson) if Lesson else JsonResponse(status=404, data={"message": f"Lesson does not exist"})

    def post(self, request):
        try:
            lesson_obj = {
                "title": request.data["title"],
                "content": request.data["content"],
                "module_id": request.data["module_id"],
                "order": request.data["order"],
            }
        except Exception as e:
            return JsonResponse(status=400, data={"message": f"Missing key: {e}"})

        try:
            lesson = self.lesson_service.create(**lesson_obj)
            return JsonResponse(status=201, data=lesson.to_dict(), safe=False)
        except Exception as e:
            return JsonResponse(status=400, data={"message": f"Error creating lesson: {e}"})

    def patch(self, request, id):
        lesson_obj = {
            "title": request.data.get("title"),
            "content": request.data.get("content"),
            "module_id": request.data.get("module_id"),
            "order": request.data.get("order"),
        }

        try:
            lesson = self.lesson_service.update(id, **lesson_obj)
            return JsonResponse(lesson) if lesson else JsonResponse(status=404, data={"message": f"Lesson does not exist"})
        except Exception as e:
            return JsonResponse(status=400, data={"message": f"Error updating lesson: {e}"})

    def delete(self, request, id):
        Lesson = self.lesson_service.delete(id)
        if Lesson:
            return JsonResponse(status=204, data={"message": f"Deleted lesson with id {id}"})
        else:
            return JsonResponse(status=404, data={"message": f"Lesson does not exist"})
