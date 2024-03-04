from django.http import HttpResponse, JsonResponse
from .BaseView import BaseView
from ..services.AssignmentService import AssignmentService
from ..Utils import Utils

class AssignmentView(BaseView):
    def __init__(self, http_method_names):
        self.assignment_service = AssignmentService()

    def get_all(self):
        return JsonResponse(self.assignment_service.get_all(), safe=False)

    def get_by_id(self, id):
        assignment = self.assignment_service.get_by_id(id)
        return JsonResponse(assignment) if assignment else JsonResponse(status=404, data={"message": f"Assignment does not exist"})

    def post(self, request):
        try:
            assignment_obj = {
                "title": request.data["title"],
                "description": request.data["description"],
                "course_id": request.data["course_id"],
                "due_date": request.data["due_date"],
                "max_points": request.data["max_points"],
            }
        except Exception as e:
            return JsonResponse(status=400, data={"message": f"Missing key: {e}"})

        try:
            assignment = self.assignment_service.create(**assignment_obj)
            return JsonResponse(status=201, data=assignment.to_dict(), safe=False)
        except Exception as e:
            return JsonResponse(status=400, data={"message": f"Error creating Assignment: {e}"})

    def patch(self, request, id):
        assignment_obj = {
            "title": request.data.get("title"),
            "description": request.data.get("description"),
            "course_id": request.data.get("course_id"),
            "due_date": request.data.get("due_date"),
            "max_points": request.data.get("max_points"),
        }

        try:
            assignment = self.assignment_service.update(id, **assignment_obj)
            return JsonResponse(assignment) if assignment else JsonResponse(status=404, data={"message": f"Assignment does not exist"})
        except Exception as e:
            return JsonResponse(status=400, data={"message": f"Error updating assignment: {e}"})

    def delete(self, request, id):
        assignment = self.assignment_service.delete(id)
        if assignment:
            return JsonResponse(status=204, data={"message": f"Deleted assignment with id {id}"})
        else:
            return JsonResponse(status=404, data={"message": f"Assignment does not exist"})
