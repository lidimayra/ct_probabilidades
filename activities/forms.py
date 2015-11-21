from django import forms

class form_n(forms.Form):
    n = forms.IntegerField()

class form_fac(forms.Form):
    fac = forms.IntegerField()

class form_fr(forms.Form):
    fr = forms.FloatField()

class form_facr(forms.Form):
    facr = forms.FloatField()