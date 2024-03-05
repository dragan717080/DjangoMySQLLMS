from ..models import User
from .BaseRepository import BaseRepository

class UserRepository(BaseRepository):
    def __init__(self):
        self.model = User

    def create(self, username, email, password_hash, status='student'):
        user = User(username=username, email=email, password_hash=password_hash, status=status)
        user.save()
        return user

    def update(self, id, username, email, password_hash, status="student"):
        try:
            user = User.objects.get(pk=id)
        except User.DoesNotExist:
            return None
        
        if username:
            user.username = username

        if email:
            user.email = email

        if password_hash:
            user.password_hash = password_hash

        if status in [User.ROLE_STUDENT, User.ROLE_INSTRUCTOR]:
            user.status = status
        else:
            return f"Undefined status {status}"

        user.save()
        return user

    def get_all_students(self):
        return User.objects.filter(status="student")
    
    def get_all_instructors(self):
        return User.objects.filter(status="instructor")
