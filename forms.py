from django import forms
from salesactivity.models import Branches
class BranchesForm(forms.ModelForm):
    class Meta:
        model=Branches
        fields="__all__"
