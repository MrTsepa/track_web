from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', ]


class RegisterView(FormView):
    form_class = MyUserCreationForm
    # success_url = resolve_url("core:login") #  why not working
    success_url = "/login/"
    template_name = "core/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)
