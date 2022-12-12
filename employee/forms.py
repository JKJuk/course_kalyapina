from django.forms import ModelForm
from .models import Person, Employee, Position


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['person', 'position', 'NDS', 'salary']


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['last_name', 'first_name', 'middle_name', 'date', 'sex']


class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = ['name_position', 'count_hours_in_week']
