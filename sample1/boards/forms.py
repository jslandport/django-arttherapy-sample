from django import forms

mytuple = [('1', 'before'), ('2','during'), ('3','after')]

class ArtTherapyForm(forms.Form):
	 ## d = {"one": 1, "two": 2, "Three":3 }
	
    your_name = forms.CharField(label='Your name', max_length=100)
    your_therapist = forms.CharField(label='Your Therapist', max_length=100)
    visit_number = forms.IntegerField(label='Visit Number', min_value=0, max_value=100)
    drawing_completed = forms.NullBooleanField(label='Drawing Completed')
    which_drawing = forms.ChoiceField(
    	choices=mytuple,
    	### this would bake in a class:
    	## widget = forms.Select(attrs={'class': 'abbazabba'})
    	### here's the ability to make the actual widget selected something else:
    	widget=forms.RadioSelect
    )
    ## colors_used = forms.MultipleChoiceField()
    
