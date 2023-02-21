from django.urls import path,include
from .views import createMsg,getMsg,getMsgById,deleteMsg,updateMsg,getMsgByTeacherId


urlpatterns = [

    path('create',  createMsg.as_view()),
    path('get', getMsg.as_view()),
    path('getByTeacherId/<str:id>', getMsgByTeacherId.as_view()),
    path('get/<str:id>', getMsgById.as_view()),
    path('update/<str:id>', updateMsg.as_view()),
    path('delete/<str:id>', deleteMsg.as_view()),
]

