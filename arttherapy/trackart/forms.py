from django import forms
from .models import art_client


### mytuple = [('BF', 'before'), ('DU','during'), ('AF','after')]

class OneClientForm(forms.Form):
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
   
   
   
class OneAppointmentForm(forms.Form):
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

   
   '''
   drawing_completed = forms.NullBooleanField(label='Drawing Completed')
   which_drawing = forms.ChoiceField(
   	choices=mytuple,
   	### this would bake in a class:
   	## widget = forms.Select(attrs={'class': 'abbazabba'})
   	### here's the ability to make the actual widget selected something else:
   	widget=forms.RadioSelect
   )
   ## colors_used = forms.MultipleChoiceField()
   '''
   
   
   '''
   	## here was a top-level clean but i really only cared about one field,
   	## and its errors were always 'generic' errors,
   	## because evidently you have to do a clean_[FIELD]() to get a field-specific error
      def clean(self):
      	cleaned_data = super().clean()
      	if not forms.Form.has_error(field='which_drawing', self=self):
   	    	whichd = cleaned_data.get('which_drawing')
   	    	if whichd != 'AF':
   	    		thismsg = "You\'ll...have to do more after " + whichd
   		    	raise forms.ValidationError(
   		    		thismsg
   		    	)
   '''
   	

   '''
   ### 
   def clean_which_drawing(self):
   	data = self.cleaned_data['which_drawing']
   	if not forms.Form.has_error(field='which_drawing', self=self):
   		if data != 'AF':
   		 	raise forms.ValidationError(
   		    'your choice, ' + data + ', isn\'t the last one, you\'ll need to do more',
   		    code='invalid',
   		 	)
   '''
