from django.db.models import Model

class BaseRepository():
    def get_all(self):
        return self.model.objects.all()

    def get_by_id(self, id):
        try:
            return self.model.objects.get(pk=id)
        except self.model.DoesNotExist:
            return None

    def delete(self, id):
        try:
            model_instance = self.model.objects.get(pk=id)
            model_instance.delete()
            return 1
        except self.model.DoesNotExist:
            return None
