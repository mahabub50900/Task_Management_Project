from django import forms 
from . models import MyTask

class TaskForm(forms.ModelForm):
    class Meta:
        model = MyTask
        fields = '__all__'