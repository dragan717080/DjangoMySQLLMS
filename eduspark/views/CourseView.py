from django.http import HttpResponse, JsonResponse
from .BaseView import BaseView
from ..services.CourseService import CourseService
from ..Utils import Utils

class CourseView(BaseView):
    def __init__(self, http_method_names):
        self.course_service = CourseService()

    def get_all(self):
        return JsonResponse(self.course_service.get_all(), safe=False)

    def get_by_id(self, id):
        course = self.course_service.get_by_id(id)
        return JsonResponse(course) if course else JsonResponse(status=404, data={"message": f"Course does not exist"})

    def post(self, request):
        try:
            course_obj = {
                "title": request.data["title"],
                "description": request.data["description"],
                "instructor_id": request.data["instructor_id"],
                "start_date": request.data["start_date"],
                "end_date": request.data["end_date"],
            }
        except Exception as e:
            return JsonResponse(status=400, data={"message": f"Missing key: {e}"})

        try:
            return JsonResponse(status=201, data=self.course_service.create(**course_obj).to_dict(), safe=False)
        except Exception as e:
            return JsonResponse(status=400, data={"message": f"Error creating course: {e}"})

    def patch(self, request, id):
        return Utils.get_patch_data(request, id, ["title", "description", "instructor_id", "start_date", "end_date"], self.course_service)

    def delete(self, request, id):
        course = self.course_service.delete(id)
        if course:
            return JsonResponse(status=204, data={"message": f"Deleted course with id {id}"})
        else:
            return JsonResponse(status=404, data={"message": f"Course does not exist"})
