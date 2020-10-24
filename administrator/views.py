from django.shortcuts import redirect, render
from django.contrib.auth import login, logout,authenticate
from .forms import UseradminpageSignUpForm
from .models import User, Useradminpage, Vacancies
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.generic import CreateView, ListView, View
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user , allowed_users, admin_only
from summary_vacancy.models import Student


@admin_only
def administrator(request):
    a = Student.objects.all()
    return render(request, 'administrator/administrator.html', {'a': a})




class administrator_register(CreateView):
    model = User
    form_class = UseradminpageSignUpForm
    template_name = 'administrator/administrator_register.html'

    
    def form_valid(self, form):
        user = form.save()
        dj_login(self.request, user)
        return redirect('administrator')




class vacancies_database(ListView):
    model = Vacancies
    template_name = 'administrator/vacancies_database.html'
    context_object_name = 'vacancies'

    
    def get_contegxt_data(self, *args, **kwargs):
        context = super().get_contegxt_data(*args, **kwargs)
        print(context)
        return context




def logout_view(request):
    logout(request)
    return redirect('summary_vacancy:login')