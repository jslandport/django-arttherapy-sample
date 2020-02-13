from django import forms
from .models import art_client
from .models import paintcolor
from .models import clientmood


### mytuple = [('BF', 'before'), ('DU','during'), ('AF','after')]

class ClientForm(forms.Form):
   ## d = {"one": 1, "two": 2, "Three":3 }
   art_clientfirstname = forms.CharField(label='First Name', max_length=50)
   art_clientlastname = forms.CharField(label='Last Name', max_length=50)
   art_clientdob = forms.DateField(
      label='Date of Birth',
      input_formats=[
         '%m/%d/%Y',
         '%m-%d-%Y'
      ],
      widget=forms.widgets.DateInput(format="%m/%d/%Y")
   )
   
   
   
class AppointmentForm(forms.Form):
   qc = art_client.objects.all().order_by('art_clientlastname','art_clientfirstname')
   art_clientid = forms.ModelChoiceField(queryset=qc, label='Client', empty_label="Pick a Client")
   art_appointmenttime = forms.DateTimeField(
      label='Appointment Date/Time',
      input_formats=[
         '%m/%d/%Y %H:%M',
         '%m-%d-%Y %H:%M'
      ],
      widget=forms.widgets.DateInput(format="%m/%d/%Y %H:%M")
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
   
