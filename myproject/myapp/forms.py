from django import forms

class ExecuteForm(forms.Form):
    execute_button = forms.CharField(widget=forms.HiddenInput(), required=False)