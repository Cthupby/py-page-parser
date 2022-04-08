from django.urls import path
from . import views


urlpatterns = [
    path('links/', views.LinkList.as_view()),
    path('pages/', views.PageList.as_view()),
]
