from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from .models import User,Useradminpage, Vacancies, Summaries
from django.dispatch import receiver
from django.contrib.auth.models import Group
from summary_vacancy.models import Professions_da, Language_Da, Vacancies_Createes, Student, Marks
from django.views.generic import CreateView, ListView, View
from django.db import transaction
from django.dispatch import receiver
from django.forms import CheckboxSelectMultiple

from multiselectfield import MultiSelectField


class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'email')



# FORM FAQAT ADMINISTRATORLARNI RO'YHATDAN O'TKAZISH UCHUN
class UseradminpageSignUpForm(UserCreationForm):
    last_name = forms.CharField(required=True)
    first_name = forms.CharField(required=True)    
    email = forms.CharField(required=True)
    father_name = forms.CharField(required=True)
    admin_image = forms.ImageField(required=True) 

    
    class Meta(UserCreationForm.Meta):
        model = User 

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        user.is_employee = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save() 

        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        useradminpage = Useradminpage.objects.create(user=user)
        useradminpage.father_name=self.cleaned_data.get('father_name')
        useradminpage.admin_image = self.cleaned_data.get('admin_image') 
        
    
        useradminpage.save()
        return user
   
          



# FORM FAQAT ADMINISTRATORLARNI RO'YHATDAN O'TKAZISH UCHUN
class UservacanciesSignUpForm(UserCreationForm):
    last_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control', 'placeholder': 'фамилия'}
        ))
    first_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control', 'placeholder': 'имя'}
        ))   
    father_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control', 'placeholder': 'отчество'}
        ))
    email = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control', 'placeholder': 'электронная почта'}
        ))
    phone_numer = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control', 'placeholder': 'номер телефона '}
        ))
    name_company = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control', 'placeholder': 'названия компания'}
        ))
    region = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control', 'placeholder': 'регион'}
        ))
    
    class Meta(UserCreationForm.Meta):
        model = User 

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = True
        user.is_staff = True
        
        if commit:
            user.save()
            group = Group.objects.get(name="vacancies")
            user.groups.add(group)

        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        useradminpage = Vacancies.objects.create(user=user)
        useradminpage.father_name=self.cleaned_data.get('father_name')
        useradminpage.phone_numer=self.cleaned_data.get('phone_numer')
        useradminpage.name_company=self.cleaned_data.get('name_company')
        useradminpage.region=self.cleaned_data.get('region')
        useradminpage.save()
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'логин'}) 
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'пароль'}) 
        self.fields['password2'].widget.attrs.update({'class': 'form-control',  'placeholder': 'проверка пароль'}) 
    



        

# FORM FAQAT ADMINISTRATORLARNI RO'YHATDAN O'TKAZISH UCHUN
class UsersummariesSignUpForm(UserCreationForm):
    last_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control', 'placeholder': 'фамилия'}
        ))
    first_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control', 'placeholder': 'имя'}
        ))    
    email = forms.CharField(required=True, widget=forms.TextInput(
        attrs = {'class':'form-control', 'placeholder': 'электронная почта или номер телефона'}
        ))

    
    class Meta(UserCreationForm.Meta):
        model = User 

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = True
        user.is_staff = True

        if commit:
            user.save()
            group = Group.objects.get(name="summaries")
            user.groups.add(group)

        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        useradminpage = Summaries.objects.create(user=user)

        useradminpage.save()
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'логин'}) 
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'пароль'}) 
        self.fields['password2'].widget.attrs.update({'class': 'form-control',  'placeholder': 'проверка пароль'})




class SummariesUpdateForm(forms.ModelForm):

    class Meta:
        model = Summaries
        fields = ('father_name',)


class SummariesssUpdateForm(forms.ModelForm):

    class Meta:
        model = Summaries
        fields = ('summary_image_u',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['summary_image_u'].widget.attrs.update({'class': 'form-control'}) 
 











SEX_CHOICES = (
        ('Мужской', 'Мужской'),
        ('Женский', 'Женский'),

        )
WORK_CHOICES = (
        ('Есть опыт работы', 'Есть опыт работы'),
        ('Нет опыта работы', 'Нет опыта работы'),

        )
DG_CHOICES = (
        ('неокончание выше', 'неокончание выше'),
        ('высшее', 'высшее'),
        ('бакалавр', 'бакалавр'),
        ('магистр', 'Магистр'),
        ('магистр', 'Магистр'),
        ('кандидат наук', 'кандидат наук'),
        ('доктор наук', 'доктор наук'),
        )

SAL_CHOICES = (
        ('руб', 'руб'),
        ('USD', 'USD'),
        ('EUR', 'EUR'),

        )
LAN_CHOICES = (
        ('английский', 'английский'),
        ('русский', 'русский'),
        ('немецкий', 'немецкий'),
        )

class StudentForm(forms.ModelForm):

    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs = {'class':'form-control', 'type':'text', 'placeholder': "Фамилия"}
        ))
    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs = {'class':'form-control', 'type':'text', 'placeholder': "Имя"}
        ))
    phone_numer = forms.CharField(required=False, widget=forms.TextInput(
        attrs = {'class':'form-control', 'type':'number', 'placeholder': "+7"}
        ))
    city_of_residence = forms.CharField(required=False, widget=forms.TextInput(
        attrs = {'class':'form-control', 'type':'text', 'placeholder': "Город проживания"}
        ))
    date_of_birth = forms.CharField(required=False, widget=forms.TextInput(
        attrs = {'class':'form-control', 'type':'date',  'placeholder': "Дата рождения"}
        ))
    sex = forms.ChoiceField(choices=SEX_CHOICES, widget=forms.RadioSelect)
    
    work = forms.ChoiceField(required=False, choices=WORK_CHOICES, widget=forms.RadioSelect)

    career_objective = forms.CharField(required=False, widget=forms.TextInput(
        attrs = {'class':'form-control', 'type':'text',  'placeholder': "Желаемая должность"}
        ))
    salary = forms.CharField(required=False, widget=forms.TextInput(
        attrs = {'class':'form-control col-md-12', 'type':'number',  'placeholder': "Зарплата"}
        ))
    salaryy = forms.ChoiceField(required=False, choices = SAL_CHOICES)
    dgree = forms.ChoiceField(required=False, choices = DG_CHOICES)
    language = forms.ChoiceField(required=False, choices = LAN_CHOICES)   

    # professions = forms.ModelMultipleChoiceField(queryset=Professions_da.objects.all(), widget=forms.CheckboxSelectMultiple(), required=False)
    opnachala = forms.CharField(required=False, widget=forms.TextInput(
        attrs = {'class':'form-control col-md-12', 'type':'date',  'placeholder': "Начало работы"}
        ))
    opndo = forms.CharField(required=False, widget=forms.TextInput(
        attrs = {'class':'form-control col-md-12', 'type':'date',  'placeholder': "По настоящее время"}
        ))
    organizatsiya = forms.CharField(required=False, widget=forms.TextInput(
        attrs = {'class':'form-control col-md-12', 'type':'text',  'placeholder': "Организация"}
        ))
    doljinos = forms.CharField(required=False, widget=forms.TextInput(
        attrs = {'class':'form-control col-md-12', 'type':'text',  'placeholder': "Должность"}
        ))
    shto_vi_del_na = forms.CharField(required=False, widget=forms.Textarea(
        attrs = {'class':'form-control col-md-12', 'type':'text',  'placeholder': "Обязанности на рабочем месте"}
        ))
    raskajiti_o_sebya = forms.CharField(required=False, widget=forms.Textarea(
        attrs = {'class':'form-control col-md-12', 'type':'text',  'placeholder': "О себе"}
        ))
    kluchniy_naviki = forms.CharField(required=False, widget=forms.TextInput(
        attrs = {'class':'form-control col-md-12', 'type':'text',  'placeholder': "Ключевые навыки"}
        ))
    # languagee = forms.ModelMultipleChoiceField(queryset=Language_Da.objects.all(), required=False, widget=forms.CheckboxSelectMultiple())



    class Meta:
        model = Student

        fields = [
            # 'user',
            'last_name',
            'first_name',
            'phone_numer',
            'city_of_residence',
            'date_of_birth',
            'sex',           
            'work',
            'career_objective',
            'salary',
            'salaryy',
            'dgree',
            'language',
            # 'professions',
            'opnachala',
            'opndo',
            'organizatsiya',
            'doljinos',
            'shto_vi_del_na',
            'raskajiti_o_sebya',            
            'kluchniy_naviki',
            'Abxaziya',
            'Avstraliya',
            'Avstriya',
            'Ozarbayjon',
            'Albaniya',
            'Jazoir',
            'Angola', 
            'Andorra',
            'Argentina',
            'Armaniston',
            'Afgoniston',
            'Bagama_orollari',
            'Bangladesh',
            'Barbados',
            'Bahrayn',
            'Belorussiya',
            'Beliz',
            'Belgiya',
            'Bolgariya',
            'Boliviya',
            'Bosniya_Gertsegovina',
            'Braziliya', 
            'Bruney_Darussalom',
            'Burkina_Faso', 
            'Buyuk_Britaniya',
            'Vengriya', 
            'Venesuela',
            'Vetnam',
            'Gabon', 
            'Gvineya',
            'Germaniya',
            'Rossiya',
            'AQSH',
            'Ozbekiston',
            'Yaponiya',
            'English',
            'French',
            'German',
            'Ukrainian',
            'Italian',
            'Uzbek',
            'Car',
            'Administrative',
            'Accounting_department',
            'Mining',
            'Other',
            'Procurement',
            'Information',
            'Art',
            'Consulting',
            'Marketing',
            'The_medicine', 
            'The_science',
            'Sales',
            'Production',
            'Working',
            'Insurance',
            'Building',
            'Transport',
            'Tourism',
            'Control',
            'Finance',
            'Lawyers',
                    
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['user'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['salaryy'].widget.attrs.update({'class': 'form-control col-md-6'}) 
        self.fields['dgree'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['language'].widget.attrs.update({'class': 'form-control'}) 


class MarksForm(forms.ModelForm):
    class_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs = {'class':'form-control col-md-12', 'type':'text',  'placeholder': "Учебное заведение"}
        ))
    english = forms.CharField(required=False, widget=forms.TextInput(
        attrs = {'class':'form-control col-md-12', 'type':'text',  'placeholder': "Факультет"}
        ))
    nepali = forms.CharField(required=False, widget=forms.TextInput(
        attrs = {'class':'form-control col-md-12', 'type':'text',  'placeholder': "Специализация"}
        ))
    nepalii = forms.CharField(required=False, widget=forms.TextInput(
        attrs = {'class':'form-control col-md-12', 'type':'text',  'placeholder': "Год окончания"}
        ))
    class Meta:
        model = Marks

        fields = [
            'class_name',
            'english',
            'nepali',
            'nepalii',
        ]

        widgets = {
            'class_name': forms.TextInput(attrs={'class': 'formset-field'}),
            'english': forms.TextInput(attrs={'class': 'formset-field'}),
            'nepali': forms.TextInput(attrs={'class': 'formset-field'}),
            'nepalii': forms.TextInput(attrs={'class': 'formset-field'})
        }












NAL_CHOICES = (
        ('до вычета налогов', 'до вычета налогов'),
        ('на руки', 'на руки'),

        )

TIPZ_CHOICES = (
        ('полная занятость', 'полная занятость'),
        ('частные занятость', 'частные занятость'),
        ('проектная работа или розовое задание', 'проектная работа или розовое задание'),
        ('волонтерство', 'волонтерство'),
        ('стажировка', 'стажировка'),

        )

RABOTI_CHOICES = (
        ('работа только пн сб', 'работа только пн сб'),
        ('работа только пн сб и вс', 'работа только пн сб и вс'),
        ('можно работать сменами по 4-6 часов в день', 'можно работать сменами по 4-6 часов в день'),

        )
OPT_CHOICES = (
        ('Нет опыта', 'Нет опыта'),
        ('От 1 года до 3 лет', 'От 1 года до 3 лет'),
        ('От 3 до 6 лет', 'От 3 до 6 лет'),
        ('Более 6 лет', 'Более 6 лет'),

        )
GRAF_CHOICES = (
        ('Полный день', 'Полный день'),
        ('Сменный график', 'Сменный график'),
        ('Гибкий график', 'Гибкий график'),
        ('Удаленная работа', 'Удаленная работа'),
        ('Вахтовый метод', 'Вахтовый метод'),

        )


class Vacancies_CreateesForm(forms.ModelForm):
    
    name_vac = forms.CharField(widget=forms.TextInput(
        attrs = {'class':'form-control', 'type':'text', 'placeholder': "название вакансии"}
        ))
    sifr = forms.CharField(widget=forms.TextInput(
        attrs = {'class':'form-control', 'type':'text', 'placeholder': "код вакансии"}
        ))
    kluchniy_naviki = forms.CharField(widget=forms.TextInput(
        attrs = {'class':'form-control', 'type':'text', 'placeholder': "ключевые навыки"}
        ))
    doxodot = forms.CharField(widget=forms.TextInput(
        attrs = {'class':'form-control col-md-12', 'type':'number', 'placeholder': "от"}
        ))
    doxoddo = forms.CharField(widget=forms.TextInput(
        attrs = {'class':'form-control', 'type':'number',  'placeholder': "до"}
        ))
    nalog = forms.ChoiceField(choices=NAL_CHOICES, widget=forms.RadioSelect)

    maestarabota = forms.CharField(widget=forms.TextInput(
        attrs = {'class':'form-control', 'type':'text',  'placeholder': "Вакансия в городе"}
        ))
    tipza = forms.ChoiceField(choices=TIPZ_CHOICES, widget=forms.RadioSelect)

  
    # vozmojno = forms.MultipleChoiceField(choices=Vacancies_Createes.VOZMO_CHOICES,widget=forms.CheckboxSelectMultiple())
    # vozmojno = forms.ModelMultipleChoiceField(queryset=Vozmojno.objects.all(), widget=forms.CheckboxSelectMultiple(), required=False)
    # rejimraboti = forms.ModelMultipleChoiceField(queryset=Rejimrabota.objects.all(), widget=forms.CheckboxSelectMultiple(), required=False)
    

    optrabota = forms.ChoiceField(choices=OPT_CHOICES, widget=forms.RadioSelect)
    grafik_rab = forms.ChoiceField(choices=GRAF_CHOICES, widget=forms.RadioSelect)
    # professionsss = forms.ModelMultipleChoiceField(queryset=Car_business.objects.all(), widget=forms.CheckboxSelectMultiple(), required=False)



    class Meta:
        model = Vacancies_Createes
        fields = ('name_vac', 'sifr', 'opisaniya', 'kluchniy_naviki', 'doxodot', 'doxoddo', 'salaryy', 'nalog', 'maestarabota',
             'tipza', 'vozmojno', 'rejimraboti1', 'rejimraboti2', 'rejimraboti3', 'optrabota', 'grafik_rab', 'Abxaziya', 'Avstraliya', 'Avstriya',
             'Ozarbayjon', 'Albaniya', 'Jazoir', 'Angola', 'Andorra', 'Argentina', 'Armaniston', 'Afgoniston', 'Bagama_orollari', 'Bangladesh',
              'Barbados', 'Bahrayn', 'Belorussiya', 'Beliz', 'Belgiya', 'Bolgariya', 'Boliviya', 'Bosniya_Gertsegovina', 'Braziliya', 
              'Bruney_Darussalom', 'Burkina_Faso', 'Buyuk_Britaniya', 'Vengriya', 'Venesuela', 'Vetnam', 'Gabon', 'Gvineya', 'Germaniya',
               'Rossiya', 'AQSH', 'Ozbekiston', 'Yaponiya', 'English', 'French', 'German', 'Ukrainian', 'Italian', 'Uzbek')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['user'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['salaryy'].widget.attrs.update({'class': 'form-control'}) 
        # self.fields['opisaniya'].widget.attrs.update({'class': 'form-control'}) 
 



