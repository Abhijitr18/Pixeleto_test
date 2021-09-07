from django.urls import path

from . import views

urlpatterns = [
    path('user_api/',views.User_View, name='user_view'),
    # path('user_api/<int:pk>',views.User_View, name='user_view'),

]