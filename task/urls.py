from django.urls import path

from . import views
app_name = "task"
urlpatterns = [
    path("", views.todo,name="todo"),  # Add this line to include the hello view
   
]