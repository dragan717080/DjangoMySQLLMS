from django.urls import path
from .views.UserView import UserView
from .views.CourseView import CourseView
from .views.EnrollmentView import EnrollmentView
from .views.ModuleView import ModuleView
from .views.LessonView import LessonView
from .views.AssignmentView import AssignmentView
from .views.SubmissionView import SubmissionView

urlpatterns = [
    path('users', UserView.as_view(http_method_names=['get', 'post']), name='user_base'),
    path('users/<str:id>', UserView.as_view(http_method_names=['get', 'patch', 'delete']), name='user_with_id'),
    path('courses', CourseView.as_view(http_method_names=['get', 'post']), name='course_base'),
    path('courses/<str:id>', CourseView.as_view(http_method_names=['get', 'patch', 'delete']), name='course_with_id'),
    path('enrollments', EnrollmentView.as_view(http_method_names=['get', 'post']), name='enrollment_base'),
    path('enrollments/<str:id>', EnrollmentView.as_view(http_method_names=['get', 'patch', 'delete']), name='enrollment_with_id'),
    path('modules', ModuleView.as_view(http_method_names=['get', 'post']), name='module_base'),
    path('modules/<str:id>', ModuleView.as_view(http_method_names=['get', 'patch', 'delete']), name='module_with_id'),
    path('lessons', LessonView.as_view(http_method_names=['get', 'post']), name='lesson_base'),
    path('lessons/<str:id>', LessonView.as_view(http_method_names=['get', 'patch', 'delete']), name='lesson_with_id'),
    path('assignments', AssignmentView.as_view(http_method_names=['get', 'post']), name='assignment_base'),
    path('assignments/<str:id>', AssignmentView.as_view(http_method_names=['get', 'patch', 'delete']), name='assignment_with_id'),
    path('submissions', SubmissionView.as_view(http_method_names=['get', 'post']), name='submission_base'),
    path('submissions/<str:id>', SubmissionView.as_view(http_method_names=['get', 'patch', 'delete']), name='submission_with_id'),
]
