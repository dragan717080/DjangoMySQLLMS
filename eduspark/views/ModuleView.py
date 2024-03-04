from django.http import HttpResponse, JsonResponse
from .BaseView import BaseView
from ..services.ModuleService import ModuleService
from ..Utils import Utils

class ModuleView(BaseView):
    def __init__(self, http_method_names):
        self.module_service = ModuleService()

    def get_all(self):
        return JsonResponse(self.module_service.get_all(), safe=False)

    def get_by_id(self, id):
        module = self.module_service.get_by_id(id)
        return JsonResponse(module) if module else JsonResponse(status=404, data={"message": f"module does not exist"})

    def post(self, request):
        try:
            module_obj = {
                "title": request.data["title"],
                "description": request.data["description"],
                "course_id": request.data["course_id"],
            }
        except Exception as e:
            return JsonResponse(status=400, data={"message": f"Missing key: {e}"})

        try:
            module = self.module_service.create(**module_obj)
            return JsonResponse(status=201, data=module.to_dict(), safe=False)
        except Exception as e:
            return JsonResponse(status=400, data={"message": f"Error creating module: {e}"})

    def patch(self, request, id):
        return Utils.get_patch_data(request, id, ["title", "description", "course_id"], self.module_service)

    def delete(self, request, id):
        module = self.module_service.delete(id)
        if module:
            return JsonResponse(status=204, data={"message": f"Deleted module with id {id}"})
        else:
            return JsonResponse(status=404, data={"message": f"Module does not exist"})
