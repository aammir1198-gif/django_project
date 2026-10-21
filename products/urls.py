from django.urls import path

from products.views import Generic_Api

urlpatterns = [

    path('' , Generic_Api.as_view()),

]