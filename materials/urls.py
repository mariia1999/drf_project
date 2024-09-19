from django.urls import path
from rest_framework.routers import SimpleRouter

from materials.views import CourseViewSet, LessonListApiView, LessonCreateApiView, LessonDestroyApiView, LessonUpdateApiView, LessonRetrieveApiView
from materials.apps import MaterialsConfig

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lesson/", LessonListApiView.as_view(), name="lesson_list"),
    path("course/<int:pk>/", LessonRetrieveApiView.as_view(), name="course_retrieve"),
    path("course/create/", LessonCreateApiView.as_view(), name="course_create"),
    path("course/<int:pk>/delete/", LessonDestroyApiView.as_view(), name="course_destroy"),
    path("course/<int:pk>/update/", LessonUpdateApiView.as_view(), name="course_update"),
]

urlpatterns += router.urls

