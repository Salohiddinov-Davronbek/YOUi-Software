from django.shortcuts import redirect, render
from django.contrib.auth import login, logout,authenticate
from administrator.forms import UseradminpageSignUpForm,UsersummariesSignUpForm,  SummariesssUpdateForm, UserChangeForm, SummariesUpdateForm, UservacanciesSignUpForm, UsersummariesSignUpForm,  Vacancies_CreateesForm
from administrator.models import User, Useradminpage, Vacancies, Summaries
from .models import Vacancies_Createes
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.generic import CreateView, ListView, View
from django.contrib.auth import authenticate, login as dj_login
from django.http import HttpResponse 
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import login,logout,authenticate


from django.contrib.auth import authenticate, login as dj_login
# Create your views here.
from django.forms import modelformset_factory
from django.db import transaction, IntegrityError
from multiselectfield import MultiSelectField


from .models import Student, Marks, Professions_da
from administrator.forms import MarksForm, StudentForm

from django.shortcuts import render,get_object_or_404
from django.db.models import Q

from django.shortcuts import render
import json






# class Vacancies_CreateesListView(ListView):
#     model = Vacancies_Createes
#     template_name = 'summary_vacancy/vac_search.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["qs_json"] = json.dumps(list(Vacancies_Createes.objects.values()))
#         return context




def vac_search(request,vacancies_createes_slug=None):
    vacancies_createes = None
    vacancies_createess = Vacancies_Createes.objects.all()
    if vacancies_createes_slug:
        vacancies_createess = get_object_or_404(Vacancies_Createes,slug=vacancies_createes_slug)
    return render(request, 'summary_vacancy/vac_search.html', {'vacancies_createess':vacancies_createess,
                                              'vacancies_createes':vacancies_createes,
                                               })





   # user = Summaries.objects.get(id=id)
   #  contact.user.add(user) 


def create_resume(request):
    context = {}    
    MarksFormset = modelformset_factory(Marks, form=MarksForm)  
    form = StudentForm(request.POST or None)
    formset = MarksFormset(request.POST or None, queryset= Marks.objects.none(), prefix='marks')
    if request.method == "POST":
        if form.is_valid() and formset.is_valid():
            try:  
                
                with transaction.atomic():
                    student = form.save(commit=False)
                    student.user = request.user.summaries
                    student.save()
                    form.save_m2m()

                    for mark in formset:
                        data = mark.save(commit=False)
                        data.student = student
                        data.save()
            except IntegrityError:
                print("Error Encountered")

            return redirect('summary_vacancy:meine_biografiess')


    context['formset'] = formset
    context['form'] = form
    return render(request, 'summary_vacancy/create_resume.html', context)





def company_vacancy_create(request):    
    if request.method == 'POST':        
        form = Vacancies_CreateesForm(request.POST)
        if form.is_valid():
            try:
                instance = form.save(commit=False)
                instance.user = request.user.vacancies
                instance.save()
                picked = form.cleaned_data.get('vozmojno')

                form.save()
                return redirect('summary_vacancy:vacancies_biografies')
            except:
                pass
    else:
        b = Vacancies.objects.filter(user=request.user)
        form = Vacancies_CreateesForm()
        context = {'form' : form, 'b': b}
        return render(request, 'summary_vacancy/company_vacancy_create.html', context)





















def home(request):
	return render(request, 'summary_vacancy/home.html')



def res_search(request,student_slug=None):
    student = None
    students = Student.objects.all()
    if student_slug:
        students = get_object_or_404(Student,slug=student_slug)
    return render(request, 'summary_vacancy/res_search.html', {'students':students,
                                              'student':student,
                                               })

# def story_list(request,category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     story = Story.objects.all()
#     if category_slug:
#         category = get_object_or_404(Category,slug=category_slug)
#         story = story.filter(category=category)
#     return render(request, 'story_list.html', {'categories':categories,
#                                               'category':category,
#                                               'story':story,
#                                               })


def res_vac_detail(request,id):
    students=get_object_or_404(Student,id=id)
    return render(request,'summary_vacancy/res_vac_detail.html',{'students':students})




def vac_res_detail(request,id):
    userr=get_object_or_404(Vacancies_Createes,id=id)
    return render(request,'summary_vacancy/vac_res_detail.html',{'userr':userr})



# VACANCIES ************************************
class vacancies_create(CreateView):
    model = User
    form_class = UservacanciesSignUpForm
    template_name = 'summary_vacancy/vacancies_create.html'

    
    def form_valid(self, form):
        user = form.save()
        dj_login(self.request, user)
        return redirect('summary_vacancy:login')


def vacancies_profile(request):
    b = Vacancies.objects.filter(user=request.user)
    return render(request, 'summary_vacancy/vacancies_profile.html', {'b': b})


def vacancies_profile_dataile(request):
    b = Vacancies.objects.filter(user=request.user)
    return render(request, 'summary_vacancy/vacancies_profile_dataile.html', {'b': b})
# VACANCIES ////////////////////////////////////////////////////



def my_vacansies(request):
    return render(request, 'summary_vacancy/my_vacansies.html')
    pass


def vacancies_biografies(request):
    b = Vacancies.objects.filter(user=request.user)
    au = Vacancies_Createes.objects.filter(user__user=request.user)
    return render(request, 'summary_vacancy/vacancies_biografies.html', {'b': b, 'au': au})

























def user_profile(request):
    a = Summaries.objects.filter(user=request.user)
    return render(request, 'summary_vacancy/user_profile.html', {'a': a})



# Summaries ****************************************
class summary_create(CreateView):
    model = User
    form_class = UsersummariesSignUpForm
    template_name = 'summary_vacancy/summary_create.html'

    
    def form_valid(self, form):
        user = form.save()
        dj_login(self.request, user)
        return redirect('summary_vacancy:login')


def summary_vacancies_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            dj_login(request, user)
            return redirect('administrator')

        else:
            messages.info(request, 'Wrong username or password.')
            
    context = {}
    return render(request, 'summary_vacancy/summary_vacancies_login.html',context)




def summary_profile(request):
    a = Summaries.objects.filter(user=request.user)
    b = Vacancies_Createes.objects.all()
    return render(request, 'summary_vacancy/summary_profile.html', {'a': a, 'b': b})





def vac_search(request,vacancies_createes_slug=None):
    vacancies_createes = None
    vacancies_createess = Vacancies_Createes.objects.all()
    if vacancies_createes_slug:
        vacancies_createess = get_object_or_404(Vacancies_Createes,slug=vacancies_createes_slug)
    return render(request, 'summary_vacancy/vac_search.html', {'vacancies_createess':vacancies_createess,
                                              'vacancies_createes':vacancies_createes,
                                               })

# Summaries //////////////////////////////////////////


def summary_profile_dataile(request):
    a = Summaries.objects.filter(user=request.user)
    return render(request, 'summary_vacancy/summary_profile_dataile.html', {'a': a})
    pass


# def book_update(request, pk, template_name='summary_vacancy/create_complete_resume.html'):
#     summaries = get_object_or_404(Summaries, pk=pk)
#     form = SummariesUpdateForm(request.POST or None, instance=summaries)
#     if form.is_valid():
#         form.save()
#         return redirect('s_profile')
#     return render(request, template_name, {'form':form})


# def book_update(request, pk, template_name='summary_vacancy/create_complete_resume.html'):
#     summaries = get_object_or_404(Summaries, pk=pk)
#     form = SummariesUpdateForm(request.POST or None, instance=summaries)
#     if form.is_valid():
#         form.save()
#         return redirect('s_profile')
#     return render(request, template_name, {'form':form})



def book_update(request, pk):
    if request.method == 'POST':
        user_form = UserChangeForm(request.POST, instance=request.user)
        profile_form = SummariesUpdateForm(request.POST, instance=request.user.summaries)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'You account has been updated!')
            return redirect('summary_vacancy:s_details')
    else:
        # category = Category.objects.all()
        a = Summaries.objects.filter(user=request.user)
        user_form = UserChangeForm(instance=request.user)
        profile_form = SummariesUpdateForm(instance=request.user.summaries)
        context = {

            # 'category': category,
            'a': a,
            'user_form': user_form,
            'profile_form': profile_form
        }        
        return render(request, 'summary_vacancy/summary_profile_dataile_update.html',context)







def summary_image_uplo(request, pk):
    if request.method == 'POST':
        
        profile_form = SummariesssUpdateForm(request.POST, request.FILES, instance=request.user.summaries)
        if profile_form.is_valid():
          
            profile_form.save()
            messages.success(request, 'You account has been updated!')
            return redirect('summary_vacancy:s_details')
    else:
        # category = Category.objects.all()
        a = Summaries.objects.filter(user=request.user)
        
        profile_form = SummariesssUpdateForm(instance=request.user.summaries)
        context = {

            # 'category': category,
            'a': a,          
            'profile_form': profile_form
        }        
        return render(request, 'summary_vacancy/summary_image_uplo.html',context)






def meine_biografies(request):
    a = Summaries.objects.filter(user=request.user)
    b = Student.objects.filter(user__user=request.user)
    c = Marks.objects.filter(student__user__user=request.user)
    return render(request, 'summary_vacancy/meine_biografies.html', {'a': a, 'b': b, 'c': c})





def resume_deldf(request, pk, template_name='summary_vacancy/resume_del.html'):
    studentss= get_object_or_404(Student, pk=pk)    
    if request.method=='POST':
        studentss.delete()
        return redirect('summary_vacancy:meine_biografiess')
    return render(request, template_name, {'object':studentss})




# def create_resume(request):    
#     if request.method == 'POST':        
#         form = Summary_CreateesForm(request.POST, request.FILES)
#         if form.is_valid():
#             # newdoc = Summary_CreateesForm(docfile=request.FILES['docfile'])
#             # newdoc.save()
#             try:
#                 form.save()
#                 return redirect('meine_biografies')
#             except:
#                 pass
#     else:
#         a = Summaries.objects.filter(user=request.user)
#         form = Summary_CreateesForm()
#         context = {'form' : form, 'a': a}
#         return render(request, 'summary_vacancy/create_resume.html', context)



# def create_resume(request):
#     context = {}
#     form = EducationForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('summary_vacancy:meine_biografiess')

#             except:
#                 pass
#     else:

#         form = EducationForm()
#         # context['formset'] = formset
#         context['form'] = form
#         return render(request, 'summary_vacancy/create_resume.html', context)



# def create_resume(request):
#     context = {}
#     EducationFormset = modelformset_factory(Education, form=EducationForm)  
#     form = Summary_CreateesForm(request.POST or None)
#     formset = EducationFormset(request.POST or None, queryset= Education.objects.none(), prefix='education')
#     if request.method == "POST":
#         if form.is_valid() and formset.is_valid():
#             try:
#                 with transaction.atomic():
#                     summary_createes = form.save(commit=False)
#                     summary_createes.save()

#                     for mark in formset:
#                         data = mark.save(commit=False)
#                         data.summary_createes = summary_createes
#                         data.save()
#             except IntegrityError:
#                 print("Error Encountered")

#             return redirect('summary_vacancy:meine_biografiess')


#     context['formset'] = formset
#     context['form'] = form
#     return render(request, 'summary_vacancy/create_resume.html', context)



