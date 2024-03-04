from abc import ABC
from django.http import HttpRequest, JsonResponse

class Utils(ABC):
    """
    It takes params for patch request and service and calls
    the corresponding update method
    
    Equivalent of this function in view

        def patch(self, request, id):
        enrollment_obj = {
            "course_id": request.data.get("course_id"),
            "student_id": request.data.get("student_id"),
        }

        try:
            enrollment = self.enrollment_service.update(id, **enrollment_obj)
            return JsonResponse(enrollment) if enrollment else JsonResponse(status=404, data={"message": f"Enrollment does not exist"})
        except Exception as e:
            return JsonResponse(status=400, data={"message": f"Error updating Enrollment: {e}"})

    Args:
        request(Request):
            request object to get params from
        id(string|int):
            id of model instance to be updated
        arg_list(list): 
            list of request body inputs to go into model object
        service(Service):
            corresponding service which will have its update method called

    Returns:
        JsonResponse: status 200, 400 or 404 depending of what service returns
    """
    @staticmethod
    def get_patch_data(request: HttpRequest, id: str, arg_list: list, service) -> JsonResponse:
        model_obj = { param: request.data.get(param) for param in arg_list }
        model_name = service.__class__.__name__.split("Service")[0]

        try:
            model = service.update(id, **model_obj)
            # Given id does not exist
            if isinstance(model, str):
                return JsonResponse(status=404, data={"message": model})
            return JsonResponse(model.to_dict()) if model else JsonResponse(status=404, data={"message": f"{model_name} does not exist"})
        except Exception as e:
            return JsonResponse(status=400, data={"message": f"Error updating {model_name.lower()}: {e}"})
