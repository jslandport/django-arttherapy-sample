from django import forms
from .models import art_client
from .models import paintcolor
from .models import clientmood


'''
as per dev.to/djangotricks, this kind of approach is how you create an input behavior such that you can get, for example, HTML5's <input type="datetime-local".. into your django forms:
'''
class DateTimeInput_forhtml5(forms.DateTimeInput):
    input_type = "datetime-local"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%dT%H:%M" ## this is the kind of format that datetime-local wants
        super().__init__(**kwargs)


class ClientForm(forms.Form):
   ## d = {"one": 1, "two": 2, "Three":3 }
   art_clientfirstname = forms.CharField(label='First Name', max_length=50)
   art_clientlastname = forms.CharField(label='Last Name', max_length=50)
   art_clientdob = forms.DateField(
      label='Date of Birth',
      input_formats=[
         '%m/%d/%Y'
      ],
      widget=forms.widgets.DateInput(format="%m/%d/%Y")
   )
   
   
   
class AppointmentForm(forms.Form):
   qc = art_client.objects.all().order_by('art_clientlastname','art_clientfirstname')
   art_clientid = forms.ModelChoiceField(queryset=qc, label='Client', empty_label="Pick a Client")
   art_appointmenttime = forms.DateTimeField(
      label='Appointment Date/Time',
      input_formats=[
         '%Y-%m-%dT%H:%M'
      ],
      widget= DateTimeInput_forhtml5(format="%Y-%m-%dT%H:%M") ###forms.widgets.DateTimeInput(format="%m/%d/%Y %I:%M %p")
   )

   
class PaintingForm(forms.Form):
   ## (users should NOT be choosing Appointment when doing a painting, they must already be IN an appointment, which will be handled upstream)
   art_paintingtitle = forms.CharField(label='Painting Title', max_length=200)
   paintcolors = forms.ModelMultipleChoiceField(
      queryset=paintcolor.objects.all(),
      label='Colors Used',
      widget=forms.CheckboxSelectMultiple
   )
   clientmoods = forms.ModelMultipleChoiceField(
      queryset=clientmood.objects.all(),
      label='Client Moods',
      widget=forms.CheckboxSelectMultiple
   )
   
