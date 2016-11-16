from django.utils.deprecation import MiddlewareMixin


class LoginFormMiddleware(MiddlewareMixin):
    def process_request(self, request):
        from django.contrib.auth.forms import AuthenticationForm
        if request.method == 'POST' and \
                'account' in request.POST and \
                        request.POST['account'] == 'Login':
            form = AuthenticationForm(data=request.POST, prefix="login")
            if form.is_valid():
                from django.contrib.auth import login
                login(request, form.get_user())
            request.method = 'GET'
        else:
            form = AuthenticationForm(request, prefix="login")

        form.fields['username'].widget.attrs.update({
            'placeholder': 'Username',
            'class': 'form-control'
        })
        form.fields['password'].widget.attrs.update({
            'placeholder': 'Password',
            'class': 'form-control'
        })
        request.login_form = form