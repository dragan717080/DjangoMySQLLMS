from rest_framework.views import APIView

class BaseView(APIView):
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get(self, request, id=None):
        return self.get_by_id(id) if id else self.get_all()
