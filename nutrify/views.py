from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = "company-login.html"

class SignupView(TemplateView):
    template_name = "company-signup.html"

class DetailView(TemplateView):
    template_name = "company-detail.html"

class PeopleView(TemplateView):
    template_name = "company-people.html"

class SettingsView(TemplateView):
    template_name = "company-settings.html"

class TaskDetailView(TemplateView):
    template_name = "company-task-detail.html"

class TaskView(TemplateView):
    template_name = "company-task.html"