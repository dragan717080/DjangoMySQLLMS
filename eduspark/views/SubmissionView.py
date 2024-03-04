from django.http import HttpResponse, JsonResponse
from .BaseView import BaseView
from ..services.SubmissionService import SubmissionService
from ..Utils import Utils

class SubmissionView(BaseView):
    def __init__(self, http_method_names):
        self.submission_service = SubmissionService()

    def get_all(self):
        return JsonResponse(self.submission_service.get_all(), safe=False)

    def get_by_id(self, id):
        submission = self.submission_service.get_by_id(id)
        return JsonResponse(submission) if submission else JsonResponse(status=404, data={"message": f"Submission does not exist"})

    def post(self, request):
        try:
            submission_obj = {
                "title": request.data["title"],
                "description": request.data["description"],
                "course_id": request.data["course_id"],
                "due_date": request.data["due_date"],
                "max_points": request.data["max_points"],
            }
        except Exception as e:
            return JsonResponse(status=400, data={"message": f"Missing key: {e}"})

        try:
            submission = self.submission_service.create(**submission_obj)
            return JsonResponse(status=201, data=submission.to_dict(), safe=False)
        except Exception as e:
            return JsonResponse(status=400, data={"message": f"Error creating submission: {e}"})

    def patch(self, request, id):
        return Utils.get_patch_data(request, id, ["title", "description", "course_id", "due_date", "max_points"], self.submission_service)

    def delete(self, request, id):
        submission = self.submission_service.delete(id)
        if submission:
            return JsonResponse(status=204, data={"message": f"Deleted submission with id {id}"})
        else:
            return JsonResponse(status=404, data={"message": f"Submission does not exist"})
