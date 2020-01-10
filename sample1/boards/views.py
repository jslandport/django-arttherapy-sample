 # howdy/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect

from .forms import ArtTherapyForm

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)
    def post(self, request, **kwargs):
        return render(request, 'indexpost.html', context=None)


class AboutPageView(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'about.html', context=None)

class FinkPageView(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'Fink.html', context=None)

class artTherapyPageView(TemplateView):
	def get(self, request, **kwargs):  # get_name(request):
		# if this is a POST request we need to process the form data
		form = ArtTherapyForm(initial={'your_name':'Dan?','your_therapist':'Steve Jones'})
		return render(request, 'arty.html', {'form': form})

	def post(self, request, **kwargs):
		# create a form instance and populate it with data from the request:
		form = ArtTherapyForm(request.POST)
		# check whether it's valid:
		if 1==0 and form.is_valid():
			# process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			return HttpResponseRedirect('/thanks/')
		else:
			print( form.changed_data )  ## this shows up in the SERVER (commandline)..
			return render(request, 'arty.html', {'form': form})
	

class thanksPageView(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'thanks.html', context=None)
