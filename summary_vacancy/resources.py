from import_export import resources
from .models import Vacancies_Createes, Student, Professions_da


class Vacancies_CreateesResource(resources.ModelResource):

    class Meta:
        model = Vacancies_Createes
        fields = '__all__'
 


class Student(resources.ModelResource):

    class Meta:
        model = Student
        fields = '__all__'



class Professions_da(resources.ModelResource):

    class Meta:
        model = Professions_da
        fields = '__all__'

