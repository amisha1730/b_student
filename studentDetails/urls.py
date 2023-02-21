from django.urls import path,include
from .views import createStudentDetail,getStudentDetail,getStudentDetailById,deleteStudentDetail,updateStudentDetail


urlpatterns = [

    path('create',  createStudentDetail.as_view()),
    path('get', getStudentDetail.as_view()),
    path('get/<str:id>', getStudentDetailById.as_view()),
    path('update/<str:id>', updateStudentDetail.as_view()),
    path('delete/<str:id>', deleteStudentDetail.as_view()),
]

