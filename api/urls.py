from django.urls import path
from . import views


urlpatterns = [
    path('api/pages/', views.PageCreateList.as_view(), name='pages_url'),
    path('api/pages/<int:pk>/links/', views.PageLinksList.as_view(), name='page_links_url'),
    path('api/pages/<int:pk>', views.PageRetrieveUpdateDestroy.as_view(), name='page_url'),
    path('api/links/<int:pk>', views.LinkRetrieveUpdateDestroy.as_view(), name='link_url'),
]
