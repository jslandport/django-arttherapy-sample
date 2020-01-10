from django import forms

class ArtTherapyForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_therapist = forms.CharField(label='Your Therapist', max_length=100)
    