from django.db.models import Model, CharField, TextField, \
    DateField, DateTimeField, JSONField, UUIDField, \
    IntegerField, ForeignKey, CASCADE, UniqueConstraint
from uuid import uuid4

class BaseModel(Model):
    id = UUIDField(
        primary_key = True, 
        default = uuid4, 
        editable = False
    )

    class Meta:
        abstract = True

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

class User(BaseModel):
    username = CharField(max_length = 20, unique=True)
    email = CharField(max_length = 30, unique=True)
    password_hash = TextField()
    ROLE_STUDENT = 'student'
    ROLE_INSTRUCTOR = 'instructor'
    ROLE_CHOICES = [
        (ROLE_STUDENT, 'Student'),
        (ROLE_INSTRUCTOR, 'Instructor'),
    ]

    status = CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=ROLE_STUDENT
    )

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password_hash': self.password_hash,
            'status': self.status,
        }

class Course(BaseModel):
    title = CharField(max_length = 150)
    description = TextField()
    start_date = DateField()
    end_date = DateField()

    instructor = ForeignKey(User, on_delete=CASCADE)

    class Meta:
        db_table = 'courses'

    def __str__(self):
        return self.title

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'instructor': self.instructor.username,
            'start_date': self.start_date,
            'end_date': self.end_date,
        }

class Enrollment(BaseModel):
    course = ForeignKey(Course, on_delete=CASCADE)
    student = ForeignKey(User, on_delete=CASCADE)

    class Meta:
        db_table = 'enrollments'

        # Ensure unique combination of student and course
        constraints = [
            UniqueConstraint(fields=['student', 'course'], name='unique_enrollment')
        ]

    def __str__(self):
        return f"Course {self.id}"
    
    def to_dict(self):
        return {
            "student": self.student.username,
            "course": self.course.title,
            "enrollment_date": self.created_at
        }

class Module(BaseModel):
    title = CharField(max_length = 150)
    description = TextField()

    course = ForeignKey(Course, on_delete=CASCADE)

    class Meta:
        db_table = 'modules'
        # Ensure unique combination of student and course
        constraints = [
            UniqueConstraint(fields=['title', 'course'], name='unique_module')
        ]

    def __str__(self):
        return self.title

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,  
            'course_id': self.course.id
        }

class Lesson(BaseModel):
    title = CharField(max_length = 150)
    content = TextField()
    order = IntegerField()

    module = ForeignKey(Module, on_delete=CASCADE)

    class Meta:
        db_table = 'lessons'

    def __str__(self):
        return self.title
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,  
            'module_id': self.module.id,
            'order': self.order,
        }

class Assignment(BaseModel):
    title = CharField(max_length = 150)
    description = TextField()
    due_date = DateField()
    max_points = IntegerField()

    course = ForeignKey(Course, on_delete=CASCADE)

    class Meta:
        db_table = 'assignments'

    def __str__(self):
        return self.title

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'course_id': self.course.id,
            'due_date': self.due_date,
            'max_points': self.max_points
        }

class Submission(BaseModel):
    submission_date = DateField()
    points_awarded = IntegerField()

    assignment = ForeignKey(Assignment, on_delete=CASCADE)
    student = ForeignKey(User, on_delete=CASCADE)

    class Meta:
        db_table = 'submissions'

    def __str__(self):
        return f"Assignment {self.id}"

    def to_dict(self):
        return {
            'id': self.id,
            'assignment': self.assignment.title,
            'student': self.student.username,
            'submission_date': self.submission_date,
            'points_awarded': self.points_awarded,
        }
