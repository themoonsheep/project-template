from django import forms


class SimpleForm(forms.Form):
    is_clear = forms.BooleanField(label="Is this document clear?", required=False)
