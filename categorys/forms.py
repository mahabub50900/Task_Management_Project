from django import forms
from . models import MyCategory

class CategoryForm(forms.ModelForm):
    class Meta:
        model = MyCategory
        fields = '__all__'