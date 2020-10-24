from django.db import models
from administrator.models import Summaries, Vacancies
from ckeditor.fields import RichTextField
from model_utils import Choices
from django.urls import  reverse
from multiselectfield import MultiSelectField

# Create your models here.


class Professions_da(models.Model):
    profession = models.CharField(max_length=100, verbose_name="Профессия")

    def __str__(self):
        return '%s' %(self.profession)

    class Meta:
        verbose_name = '2. Profession Databse'
        verbose_name_plural = '2. Profession Databse'



class Vacaprofessions(models.Model):
    vacprof = models.CharField(max_length=100, verbose_name="Профессия")

    def __str__(self):
        return '%s' %(self.vacprof)

    class Meta:
        verbose_name = '3. Vacancies Profession Databse'
        verbose_name_plural = '3. Vacancies Profession Databse'





class Language_Da(models.Model):
    languages = models.CharField(max_length=100, verbose_name="Профессия")

    def __str__(self):
        return '%s' %(self.languages)

    class Meta:
        verbose_name = 'Language Databse'
        verbose_name_plural = 'Language  Databse'






# Create your models here.
class Student(models.Model):
    user = models.ForeignKey(Summaries, related_name = "student", on_delete = models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    phone_numer = models.CharField(max_length=10, verbose_name="номер телефона")
    city_of_residence = models.CharField(max_length=200, verbose_name="Город проживания")
    date_of_birth = models.CharField(max_length=20, verbose_name="Дата рождения")    
    SEX_CHOICES = (
        ('Мужской', 'Мужской'),
        ('Женский', 'Женский'),

        )
    sex = models.CharField(max_length = 100, verbose_name="Пол" , choices = SEX_CHOICES)
        
    Abxaziya = models.BooleanField(verbose_name='Абхазия')
    Avstraliya = models.BooleanField(verbose_name='Австралия')
    Avstriya = models.BooleanField(verbose_name='Австрия')
    Ozarbayjon = models.BooleanField(verbose_name='Азербайджан')
    Albaniya = models.BooleanField(verbose_name='Албания')
    Jazoir = models.BooleanField(verbose_name='Алжир')
    Angola = models.BooleanField(verbose_name='Ангола')
    Andorra = models.BooleanField(verbose_name='Андорра')
    Argentina = models.BooleanField(verbose_name='Аргентина')
    Armaniston = models.BooleanField(verbose_name='Армения')
    Afgoniston = models.BooleanField(verbose_name='Афганистан')
    Bagama_orollari = models.BooleanField(verbose_name='Багамские Острова ')
    Bangladesh = models.BooleanField(verbose_name='Бангладеш ')
    Barbados = models.BooleanField(verbose_name='Барбадос ')
    Bahrayn = models.BooleanField(verbose_name='Бахрейн ')
    Belorussiya = models.BooleanField(verbose_name='Беларусь ')
    Beliz = models.BooleanField(verbose_name='Белиз ')
    Belgiya = models.BooleanField(verbose_name='Бельгия ')
    Bolgariya = models.BooleanField(verbose_name='Болгария ')
    Boliviya = models.BooleanField(verbose_name='Боливия ')
    Bosniya_Gertsegovina = models.BooleanField(verbose_name='Босния и Герцеговина')
    Braziliya = models.BooleanField(verbose_name='Бразилия')
    Bruney_Darussalom = models.BooleanField(verbose_name='Бруней Даруссалам')
    Burkina_Faso = models.BooleanField(verbose_name='Буркина Фасо')
    Buyuk_Britaniya = models.BooleanField(verbose_name='Великобритания')
    Vengriya = models.BooleanField(verbose_name='Венгрия')
    Venesuela = models.BooleanField(verbose_name='Венесуэла')
    Vetnam = models.BooleanField(verbose_name='Вьетнам')
    Gabon = models.BooleanField(verbose_name='Габон')
    Gvineya = models.BooleanField(verbose_name='Гвинея')
    Germaniya = models.BooleanField(verbose_name='Германия')
    Rossiya = models.BooleanField(verbose_name='Россия')   
    AQSH = models.BooleanField(verbose_name='США')
    Ozbekiston = models.BooleanField(verbose_name='Узбекистан')
    Yaponiya = models.BooleanField(verbose_name='Япония')
    
    
    WORK_CHOICES = (
        ('Есть опыт работы', 'Есть опыт работы'),
        ('Нет опыта работы', 'Нет опыта работы'),

        )
    work = models.CharField(max_length =100, verbose_name="Опыт работы" , choices = WORK_CHOICES)
    career_objective = models.CharField(max_length=200, verbose_name="Желаемая должность")
    salary = models.CharField(max_length=100, verbose_name="Зарплата")
    SAL_CHOICES = (
        ('руб', 'руб'),
        ('USD', 'USD'),
        ('EUR', 'EUR'),

        )
    salaryy = models.CharField(max_length = 100, verbose_name="Зарплата" , choices = SAL_CHOICES)
    DG_CHOICES = (
        ('неокончание выше', 'неокончание выше'),
        ('высшее', 'высшее'),
        ('бакалавр', 'бакалавр'),
        ('магистр', 'Магистр'),
        ('магистр', 'Магистр'),
        ('кандидат наук', 'кандидат наук'),
        ('доктор наук', 'доктор наук'),
        )
    dgree = models.CharField(max_length = 100, verbose_name="Зарплата" , choices = DG_CHOICES)
    LAN_CHOICES = (
        ('английский', 'английский'),
        ('русский', 'русский'),
        ('немецкий', 'немецкий'),
        )
    language = models.CharField(max_length = 100, verbose_name="родной язык" , choices = LAN_CHOICES)
    # professions = models.ManyToManyField(Professions_da)
    # kasblar qo'shish
    opnachala = models.CharField(max_length = 100, verbose_name="Начало работы")
    opndo = models.CharField(max_length = 100, verbose_name="По настоящее время")
    organizatsiya = models.CharField(max_length=200, verbose_name="Организация")
    doljinos = models.CharField(max_length=100, verbose_name="Должность")
    shto_vi_del_na = models.TextField(verbose_name="Обязанности на рабочем месте")
    raskajiti_o_sebya = models.TextField(verbose_name="О себе")
    kluchniy_naviki = models.CharField(max_length=500, verbose_name="ключевые навыки")

    Car = models.BooleanField(verbose_name='Автомобильный бизнес')
    Administrative = models.BooleanField(verbose_name='Административный персонал')
    Accounting_department = models.BooleanField(verbose_name='Бухгалтерия')
    Mining = models.BooleanField(verbose_name='Добыча сырья')
    Other = models.BooleanField(verbose_name='Другое')
    Procurement = models.BooleanField(verbose_name='Закупки')
    Information = models.BooleanField(verbose_name='Информационные технологии, Интернет, Мультимедиа')
    Art = models.BooleanField(verbose_name='Искусство, Развлечения, Масс-медиа')
    Consulting = models.BooleanField(verbose_name='Консультирование')
    Marketing = models.BooleanField(verbose_name='Маркетинг, Реклама, PR')
    The_medicine = models.BooleanField(verbose_name='Медицина, Фармацевтика')
    
    The_science = models.BooleanField(verbose_name='Наука, Образование')
    Sales = models.BooleanField(verbose_name='Продажи')
    Production = models.BooleanField(verbose_name='Производство, Технологии')
    Working = models.BooleanField(verbose_name='Рабочий персонал')
    Insurance = models.BooleanField(verbose_name='Страхование')
    Building = models.BooleanField(verbose_name='Строительство, Архитектура')
    Transport = models.BooleanField(verbose_name='Транспорт, Логистика')
    Tourism = models.BooleanField(verbose_name='Туризм, Гостиницы, Рестораны')
    Control = models.BooleanField(verbose_name='Управление персоналом')
    Finance = models.BooleanField(verbose_name='Финансы, Банки, Инвестиции')
    Lawyers = models.BooleanField(verbose_name='Юристы')
        
    English = models.BooleanField(verbose_name='английский')
    French = models.BooleanField(verbose_name='французский')
    German = models.BooleanField(verbose_name='немецкий')
    Ukrainian = models.BooleanField(verbose_name='украинский')
    Italian = models.BooleanField(verbose_name='итальянский')
    Uzbek = models.BooleanField(verbose_name='узбекский')


    # languagee = models.ManyToManyField(Language_Da)
    # kasblar qo'shish

    class Meta:
        db_table = "students"

    def get_absolute_url(self):
       return reverse('summary_vacancy:res_vac_detail',args=[self.id,])


class Marks(models.Model):
    student = models.ForeignKey(Student, related_name = "marks", on_delete=models.CASCADE)
    class_name = models.CharField(max_length=100)
    english = models.CharField(max_length=100)
    nepali = models.CharField(max_length=100)
    nepalii = models.CharField(max_length=100)


    class Meta:
        db_table = "marks"





class Vacancies_Createes(models.Model):
    user = models.ForeignKey(Vacancies, on_delete = models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    name_vac = models.CharField(max_length=200, verbose_name="Название вакансии")
    sifr = models.CharField(max_length=100, verbose_name="Код вакансии")    

    Abxaziya = models.BooleanField(verbose_name='Абхазия')
    Avstraliya = models.BooleanField(verbose_name='Австралия')
    Avstriya = models.BooleanField(verbose_name='Австрия')
    Ozarbayjon = models.BooleanField(verbose_name='Азербайджан')
    Albaniya = models.BooleanField(verbose_name='Албания')
    Jazoir = models.BooleanField(verbose_name='Алжир')
    Angola = models.BooleanField(verbose_name='Ангола')
    Andorra = models.BooleanField(verbose_name='Андорра')
    Argentina = models.BooleanField(verbose_name='Аргентина')
    Armaniston = models.BooleanField(verbose_name='Армения')
    Afgoniston = models.BooleanField(verbose_name='Афганистан')
    Bagama_orollari = models.BooleanField(verbose_name='Багамские Острова ')
    Bangladesh = models.BooleanField(verbose_name='Бангладеш ')
    Barbados = models.BooleanField(verbose_name='Барбадос ')
    Bahrayn = models.BooleanField(verbose_name='Бахрейн ')
    Belorussiya = models.BooleanField(verbose_name='Беларусь ')
    Beliz = models.BooleanField(verbose_name='Белиз ')
    Belgiya = models.BooleanField(verbose_name='Бельгия ')
    Bolgariya = models.BooleanField(verbose_name='Болгария ')
    Boliviya = models.BooleanField(verbose_name='Боливия ')
    Bosniya_Gertsegovina = models.BooleanField(verbose_name='Босния и Герцеговина')
    Braziliya = models.BooleanField(verbose_name='Бразилия')
    Bruney_Darussalom = models.BooleanField(verbose_name='Бруней Даруссалам')
    Burkina_Faso = models.BooleanField(verbose_name='Буркина Фасо')
    Buyuk_Britaniya = models.BooleanField(verbose_name='Великобритания')
    Vengriya = models.BooleanField(verbose_name='Венгрия')
    Venesuela = models.BooleanField(verbose_name='Венесуэла')
    Vetnam = models.BooleanField(verbose_name='Вьетнам')
    Gabon = models.BooleanField(verbose_name='Габон')
    Gvineya = models.BooleanField(verbose_name='Гвинея')
    Germaniya = models.BooleanField(verbose_name='Германия')
    Rossiya = models.BooleanField(verbose_name='Россия')   
    AQSH = models.BooleanField(verbose_name='США')
    Ozbekiston = models.BooleanField(verbose_name='Узбекистан')
    Yaponiya = models.BooleanField(verbose_name='Япония')
     
    opisaniya = RichTextField(blank=True, null=True)
    kluchniy_naviki = models.CharField(max_length=500, verbose_name="Ключевые навыки")
    
    doxodot = models.CharField(max_length=100, verbose_name="предполагаемый уровень доходов в месяц или за обмен работ от")
    doxoddo = models.CharField(max_length=100, verbose_name="до")
    SAL_CHOICES = (
        ('руб', 'руб'),
        ('USD', 'USD'),
        ('EUR', 'EUR'),

        )
    salaryy = models.CharField(max_length = 3, verbose_name="валюта" , choices = SAL_CHOICES)
    NAL_CHOICES = (
        ('до вычета налогов', 'до вычета налогов'),
        ('на руки', 'на руки'),

        )
    nalog = models.CharField(max_length = 100, verbose_name="налогов" , choices = NAL_CHOICES)
    maestarabota = models.CharField(max_length=200, verbose_name="Вакансия в городе")
    TIPZ_CHOICES = (
        ('полная занятость', 'полная занятость'),
        ('частные занятость', 'частные занятость'),
        ('проектная работа или розовое задание', 'проектная работа или розовое задание'),
        ('волонтерство', 'волонтерство'),
        ('стажировка', 'стажировка'),

        )
    tipza = models.CharField(max_length =100, verbose_name="Тип занятости" , choices = TIPZ_CHOICES)
    
    vozmojno = models.BooleanField(verbose_name='Возможно временное оформление')
    # vozmojno = models.ManyToManyField(to='profession.Vozmojno', verbose_name="Тип занятости")
    
    rejimraboti1 = models.BooleanField(verbose_name='Работа только по сб и вс')
    rejimraboti2 = models.BooleanField(verbose_name='Можно работать сменами по 4–6 часов в день')
    rejimraboti3 = models.BooleanField(verbose_name='Можно начинать работать после 16:00')
    # rejimraboti = models.ManyToManyField(to='profession.Rejimrabota', verbose_name="Режим работы")
    
    OPT_CHOICES = (
        ('Нет опыта', 'Нет опыта'),
        ('От 1 года до 3 лет', 'От 1 года до 3 лет'),
        ('От 3 до 6 лет', 'От 3 до 6 лет'),
        ('Более 6 лет', 'Более 6 лет'),

        )
    optrabota = models.CharField(max_length =100, verbose_name="Опыт работы", choices = OPT_CHOICES)
    GRAF_CHOICES = (
        ('Полный день', 'Полный день'),
        ('Сменный график', 'Сменный график'),
        ('Гибкий график', 'Гибкий график'),
        ('Удаленная работа', 'Удаленная работа'),
        ('Вахтовый метод', 'Вахтовый метод'),

        )
    grafik_rab = models.CharField(max_length =100, verbose_name="График работы",  choices = GRAF_CHOICES)
    
    English = models.BooleanField(verbose_name='английский')
    French = models.BooleanField(verbose_name='французский')
    German = models.BooleanField(verbose_name='немецкий')
    Ukrainian = models.BooleanField(verbose_name='украинский')
    Italian = models.BooleanField(verbose_name='итальянский')
    Uzbek = models.BooleanField(verbose_name='узбекский')


    class Meta:
        verbose_name = '3. Vakansiya'
        verbose_name_plural = '3. Vakansiya'

    def get_absolute_url(self):
       return reverse('summary_vacancy:vac_res_detail',args=[self.id,])
