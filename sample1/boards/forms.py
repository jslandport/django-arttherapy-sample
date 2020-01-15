from django import forms

mytuple = [('BF', 'before'), ('DU','during'), ('AF','after')]

class ArtTherapyForm(forms.Form):
   ## d = {"one": 1, "two": 2, "Three":3 }
   
   your_name = forms.CharField(label='Your name', max_length=100)
   your_therapist = forms.CharField(label='Your Therapist', max_length=100)
   visit_number = forms.IntegerField(label='Visit Number', min_value=0, max_value=100)
   visit_date = forms.DateField(
      label='Visit Date',
      input_formats=[
         '%m/%d/%Y',
         '%m/%d/%y',
         '%m-%d-%y'
       ]
   )
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
   	
   ### 
   def clean_which_drawing(self):
   	data = self.cleaned_data['which_drawing']
   	if not forms.Form.has_error(field='which_drawing', self=self):
   		if data != 'AF':
   		 	raise forms.ValidationError(
   		    'your choice, ' + data + ', isn\'t the last one, you\'ll need to do more',
   		    code='invalid',
   		 	)
   
