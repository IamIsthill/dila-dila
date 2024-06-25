from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from .forms import UserCreationForm
from .models import User
from django.contrib import messages

# Create your views here.
def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
            context = {'name': request.POST.get('name', ''), 'email': request.POST.get('email', '')}
            return render(request, 'users/register.html', context)
    else:
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'users/register.html', context)
    
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password. Please try again.')
    return render(request, 'users/login.html')
 

def logout_view(request):
  logout(request)
  return redirect('landing')


from django.contrib.auth.forms import SetPasswordForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth import get_user_model
from django.http import Http404

User = get_user_model()

class PasswordResetConfirmView(FormView):
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')
    form_class = SetPasswordForm
    token_generator = default_token_generator

    def get_user(self, uidb64):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        return user

    def dispatch(self, request, *args, **kwargs):
        self.user = self.get_user(kwargs['uidb64'])
        if self.user is not None and self.token_generator.check_token(self.user, kwargs['token']):
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("Invalid token or user does not exist")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


    

