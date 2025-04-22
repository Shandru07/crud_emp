from django import forms
from .models import Employe

class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe            # ✅ 'model' not 'models'
        fields = '__all__'         # ✅ 'fields' not 'feilds'
