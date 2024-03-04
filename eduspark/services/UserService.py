from django.http import HttpResponse, JsonResponse
from ..repositories.UserRepository import UserRepository

class UserService():
    def __init__(self):
        self.user_repository = UserRepository()
        
    def get_all(self):
        return [user.to_dict() for user in self.user_repository.get_all()]

    def get_by_id(self, id):
        user = self.user_repository.get_by_id(id)
        return user.to_dict() if user else None

    def create(self, username, email, password_hash, status='student'):
        return self.user_repository.create(username, email, password_hash, status)

    def update(self, id, username, email, password_hash):
        user = self.user_repository.update(id, username, email, password_hash)
        return user if user else None

    def delete(self, id):
        return self.user_repository.delete(id)
