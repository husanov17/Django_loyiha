from django.urls import path
from .views import ProductApiView, TeacherApiView, StudentApiView, CourseApiView

urlpatterns = [
    path('product/', ProductApiView.as_view(), name='product_api'),
    path('teacher/', TeacherApiView.as_view(), name='teacher_api'),
    path('student/', StudentApiView.as_view(), name='student_api'),
    path('course/', CourseApiView.as_view(), name='course_api'),
]
