from django.urls import path
from . import views

urlpatterns = [  
    path('message', views.MessageView.as_view()),
    path('message/new', views.add_message),
    path('message/list', views.message_list),
    path('conversation/list', views.conversation_list)
]