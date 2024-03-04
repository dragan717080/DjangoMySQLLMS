from django.http import HttpResponse, JsonResponse
from .BaseView import BaseView
from ..services.EnrollmentService import EnrollmentService
from ..Utils import Utils

class EnrollmentView(BaseView):
    def __init__(self, http_method_names):
        self.enrollment_service = EnrollmentService()

    def get_all(self):
        return JsonResponse(self.enrollment_service.get_all(), safe=False)

    def get_by_id(self, id):
        enrollment = self.enrollment_service.get_by_id(id)
        return JsonResponse(enrollment) if enrollment else JsonResponse(status=404, data={"message": f"Enrollment does not exist"})

    def post(self, request):
        try:
            enrollment_obj = {
                "course_id": request.data["course_id"],
                "student_id": request.data["student_id"],
            }
        except Exception as e:
            return JsonResponse(status=400, data={"message": f"Missing key: {e}"})

        try:
            enrollment = self.enrollment_service.create(**enrollment_obj)
            if isinstance(enrollment, str):
                return JsonResponse(status=404, data={"message": enrollment})
            return JsonResponse(status=201, data=enrollment.to_dict(), safe=False)
        except Exception as e:
            return JsonResponse(status=400, data={"message": f"Error creating enrollment: {e}"})

    def patch(self, request, id):
        return Utils.get_patch_data(request, id, ["course_id", "student_id"], self.enrollment_service)

    def delete(self, request, id):
        enrollment = self.enrollment_service.delete(id)
        if enrollment:
            return JsonResponse(status=204, data={"message": f"Deleted enrollment with id {id}"})
        else:
            return JsonResponse(status=404, data={"message": f"Enrollment does not exist"})
