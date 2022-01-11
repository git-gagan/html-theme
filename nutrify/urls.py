from django.urls import path
from . import views

urlpatterns = [
    path("", views.LoginView.as_view(), name="login"),
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("detail/", views.DetailView.as_view(), name="detail"),
    path("people/", views.PeopleView.as_view(), name="people"),
    path("settings/", views.SettingsView.as_view(), name="settings"),
    path("task-detail/", views.TaskDetailView.as_view(), name="task-detail"),
    path("task/", views.TaskView.as_view(), name="task"),
]