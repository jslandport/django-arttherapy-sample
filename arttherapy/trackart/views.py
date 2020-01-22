 # howdy2 /views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect

## from .forms import ArtTherapyForm
## from trackart import templates
from .models import art_client


# Create your views here.
class HomePageView(TemplateView):
   def get(self, request, **kwargs):
      '''
      qcolor = paintcolor.objects.all().order_by('paintcolortitle')
      '''
      dfeatures = {
         './viewclients': 'Client-centric View',
         './aptmonth':  'Appointment-centric View',
      }
      context = {
         'dfeatures': dfeatures
      }
      return render(request, 'trackart/index.html', context=context)

 
class ClientCentricListView(TemplateView):
   def get(self, request, **kwargs):
      qclient = art_client.objects.all().order_by('art_clientlastname','art_clientfirstname')
      context = {
         'qclient': qclient
      }
      return render(request, 'trackart/clientlist.html', context=context)


class AppointmentCentricListView(TemplateView):
   def get(self, request, **kwargs):
      return render(request, 'trackart/appointmentlist.html') ##, context=context


class ClientOneView(TemplateView):
   def get(self, request, art_client_id):
      qsclient = art_client.objects.all() ##pk=art_client_id
      if len(qsclient) == 1:
         qrow = qsclient[0]
         context = {
            'qoneclient': qrow,
            'id': art_client_id
         }
      else:
         context = {}
      return render(request, 'trackart/clientone.html', context=context)

