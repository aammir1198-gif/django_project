from django.urls import path

from products.views import CreatAndShow

urlpatterns = [

    path('' , CreatAndShow.as_view()),

]