from rest_framework.views import APIView
from django.http import JsonResponse

class BaseView(APIView):
    http_method_names = ['get', 'post', 'patch', 'delete']

    def __init__(self):
        self.model_name = self.model_repository.__class__.__name__.split("Repository")[0]

    def get(self, request, id=None):
        return self.get_by_id(id) if id else self.get_all()

    def get_all(self):
        # Return type is list but JsonResponse expects dict, so we must set param safe to False
        return JsonResponse([model.to_dict() for model in self.model_repository.get_all()], safe=False)

    def get_by_id(self, id):
        model = self.model_repository.get_by_id(id)
        return JsonResponse(model.to_dict()) if model is not None  else JsonResponse(status=404, data={"message": f"{self.model_name} does not exist"})

    def delete(self, request, id):
        model = self.model_repository.delete(id)
        if model:
            return JsonResponse(status=204, data={"message": f"Deleted {self.model_name.lower()} with id {id}"})
        else:
            return JsonResponse(status=404, data={"message": f"{self.model_name} does not exist"})
