from django.contrib import admin
from .models import Professions_da
from django_summernote.admin import SummernoteModelAdmin
from .models import Student, Marks, Language_Da, Vacaprofessions, Professions_da 



from import_export.admin import ImportExportModelAdmin
from .models import Vacancies_Createes, Student

@admin.register(Vacancies_Createes)
class Vacancies_CreateesAdmin(ImportExportModelAdmin):
	list_display = ('user', 'name_vac', 'sifr', 'opisaniya', 'kluchniy_naviki', 'doxodot', 'doxoddo', 'salaryy', 'nalog', 'maestarabota', 'vozmojno', 'tipza', 'rejimraboti1', 'rejimraboti2', 'rejimraboti3', 'optrabota')


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
	list_display = ('user', 'last_name', 'first_name', 'phone_numer', 'city_of_residence', 'date_of_birth', 'sex', 'work', 'career_objective', 'salary', 'salaryy', 'dgree', 'language', 'opnachala', 'opndo', 'organizatsiya', 'doljinos', 'shto_vi_del_na', 'raskajiti_o_sebya', 'kluchniy_naviki')


@admin.register(Professions_da)
class Professions_daAdmin(ImportExportModelAdmin):
	list_display = ('profession', )





# admin.site.register(Student)
admin.site.register(Marks)
admin.site.register(Language_Da)
admin.site.register(Vacaprofessions)



# admin.site.register(Vacancies_Createes)



