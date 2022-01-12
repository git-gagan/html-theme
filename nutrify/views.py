from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = "company-login.html"


class SignupView(TemplateView):
    template_name = "company-signup.html"


class DetailView(TemplateView):
    template_name = "company-detail.html"
    extra_context = {'url': 'detail'}


class PeopleView(TemplateView):
    template_name = "company-people.html"
    extra_context = {'url': 'people'}


class SettingsView(TemplateView):
    template_name = "company-settings.html"
    extra_context = {'url': 'settings'}


class TaskDetailView(TemplateView):
    template_name = "company-task-detail.html"
    extra_context = {'url': 'task'}


class TaskView(TemplateView):
    template_name = "company-task.html"
    extra_context = {'url': 'task'}
