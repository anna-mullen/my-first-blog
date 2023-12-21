from django.urls import path
from . import views

urlpatterns = [
    # path('', views.post_list, name='post_list'), Why this was throwing the error "no patterns or circular import", IDK, seems like the same line to me...
    path('', views.post_list, name='post_list'),
]