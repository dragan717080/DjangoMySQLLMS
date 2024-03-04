from django.http import HttpResponse, JsonResponse
from .BaseView import BaseView
from ..services.UserService import UserService
from ..Utils import Utils

class UserView(BaseView):
    def __init__(self, http_method_names):
        self.user_service = UserService()

    def get_all(self):
        return JsonResponse(self.user_service.get_all(), safe=False)

    def get_by_id(self, id):
        user = self.user_service.get_by_id(id)
        return JsonResponse(user) if user else JsonResponse(status=404, data={"message": f"User does not exist"})

    def post(self, request):
        try:
            user_obj = {
                "username": request.data["username"],
                "email": request.data["email"],
                "password_hash": request.data["password_hash"],
                "status": request.data.get("status") if request.data.get("status") else "student",
            }
        except Exception as e:
            return JsonResponse(status=400, data={"message": f"Missing key: {e}"})

        try:
            return JsonResponse(status=201, data=self.user_service.create(**user_obj).to_dict(), safe=False)
        except Exception as e:
            return JsonResponse(status=400, data={"message": f"Error creating user: {e}"})

    def patch(self, request, id):
        return Utils.get_patch_data(request, id, ["username", "email", "password_hash"], self.user_service)

    def delete(self, request, id):
        user = self.user_service.delete(id)
        if user:
            return JsonResponse(status=204, data={"message": f"Deleted user with id {id}"})
        else:
            return JsonResponse(status=404, data={"message": f"User does not exist"})

