from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Useradminpage, Vacancies, Summaries


class UserAdminn(UserAdmin):
	list_display = ("id","username", "last_name", "first_name", "password", "date_joined", "last_login", "is_superuser", "is_active", "is_staff")
	readonly_fields = ("date_joined", "last_login")

	filter_horizontal=()
	list_filter = ()
	fieldsets = ()

admin.site.register(User, UserAdminn)
# ************************************************************************
# ************************************************************************

class UseradminpageAdmin(admin.ModelAdmin):
	list_display = ("user", "father_name", "admin_image")
	# readonly_fields = ("date_joined", "last_login")

	filter_horizontal=()
	list_filter = ()
	fieldsets = ()

admin.site.register(Useradminpage, UseradminpageAdmin)
# ************************************************************************
# ************************************************************************



class VacanciesAdmin(admin.ModelAdmin):
	list_display = ("user", "father_name")
	# readonly_fields = ("date_joined", "last_login")

	filter_horizontal=()
	list_filter = ()
	fieldsets = ()

admin.site.register(Vacancies, VacanciesAdmin)
# ************************************************************************
# ************************************************************************


class SummariesAdmin(admin.ModelAdmin):
	list_display = ("user", "father_name")
	# readonly_fields = ("date_joined", "last_login")

	filter_horizontal=()
	list_filter = ()
	fieldsets = ()

admin.site.register(Summaries, SummariesAdmin)
# ************************************************************************
# ************************************************************************




# admin.site.register(User)
# admin.site.register(Useradminpage)
# admin.site.register(Vacancies)
# admin.site.register(Summaries)



