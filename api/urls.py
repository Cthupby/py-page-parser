from django.urls import path
from . import views


urlpatterns = [
    path('api/pages/', views.PageList.as_view()),
    path('api/pages/<int:pk>', views.PageRetrieveUpdateDestroy.as_view()),
    path('api/links/', views.LinkList.as_view()),
    path('api/links/<int:pk>', views.LinkRetrieveUpdateDestroy.as_view()),
]
