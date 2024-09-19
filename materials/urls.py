from django.urls import path
from rest_framework.routers import SimpleRouter

from materials.views import CourseViewSet, LessonListApiView, LessonCreateApiView, LessonDestroyApiView, LessonUpdateApiView, LessonRetrieveApiView
from materials.apps import MaterialsConfig

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lesson/", LessonListApiView.as_view(), name="lesson_list"),
    path("lesson/<int:pk>/", LessonRetrieveApiView.as_view(), name="lesson_retrieve"),
    path("lesson/create/", LessonCreateApiView.as_view(), name="lesson_create"),
    path("lesson/<int:pk>/delete/", LessonDestroyApiView.as_view(), name="lesson_destroy"),
    path("lesson/<int:pk>/update/", LessonUpdateApiView.as_view(), name="lesson_update"),
]

urlpatterns += router.urls

