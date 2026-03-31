from django import forms
from .models import Employee

#A form created based on model is called ModelForm
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'#['name','desg']