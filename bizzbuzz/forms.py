from django import forms
from bizzbuzz.models import Preferences

class PrefForm(forms.Form):
    class Meta:
        model = Preferences
        fields = ('apple', 'google', 'facebook', 'microsoft')
    # username = forms.CharField()
    # apple = forms.CharField(widget = forms.CheckboxInput(attrs={'checked': True}))
    # google = forms.CharField(widget = forms.CheckboxInput(attrs={'checked': True}))
    # facebook = forms.CharField(widget = forms.CheckboxInput(attrs={'checked': True}))
    # microsoft = forms.CharField(widget = forms.CheckboxInput(attrs={'checked': True}))