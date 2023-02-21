from django.urls import path,include
from .views import createPayment,getPayment,getPaymentById,deletePayment,updatePayment


urlpatterns = [

    path('create',  createPayment.as_view()),
    path('get', getPayment.as_view()),
    path('get/<str:id>', getPaymentById.as_view()),
    path('update/<str:id>', updatePayment.as_view()),
    path('delete/<str:id>', deletePayment.as_view()),
]