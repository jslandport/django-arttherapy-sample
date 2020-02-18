 # howdy2 /views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect

from .forms import ClientForm
from .forms import AppointmentForm
from .forms import PaintingForm
## from trackart import templates
from .models import art_client
from .models import art_appointment
from .models import art_painting
from .models import paintcolor
from .models import clientmood

from .navhelper import getnavdictfromparamsdict

## for 'default new Appointment to the current datetime'
import datetime


#############################
##
##    BASICS
##



# Create your views here.
class HomePageView(TemplateView):
   def get(self, request, **kwargs):
      dfeatures = {
         './viewclients': 'All Clients',
         './viewappointments':  'All Appointments',
         './viewpaintings':  'All Paintings',
      }
      context = {
         'dfeatures': dfeatures
      }
      return render(request, 'trackart/index.html', context=context)


#####    X-CENTRIC VIEWS
 
class ClientCentricListView(TemplateView):
   def get(self, request, **kwargs):
      qclient = art_client.objects.all().order_by('art_clientlastname','art_clientfirstname')
      context = {
         'qclient': qclient
      }
      return render(request, 'trackart/clientlist.html', context=context)


class AppointmentCentricListView(TemplateView):
   def get(self, request, **kwargs):
      qsappointment = art_appointment.objects.all().order_by('-art_appointmenttime')
      context = {
         'qsappointment': qsappointment
      }
      print(qsappointment)
      return render(request, 'trackart/appointmentlist.html', context=context)


class PaintingCentricListView(TemplateView):
   def get(self, request, **kwargs):
      qpainting = art_painting.objects.all().order_by('-createDate')
      context = {
         'qpainting': qpainting
      }
      return render(request, 'trackart/paintinglist.html', context=context)


class NotFound(TemplateView):
   def get(self, request, whatnotfound, idnotfound):
      dnavlinks = getnavdictfromparamsdict(
         dparams = { 'art_' + whatnotfound + 'id': 0 },
         cururl = request.path_info
      )
      context = {
         'whatnotfound': whatnotfound,
         'idnotfound': idnotfound,
         'dnavlinks': dnavlinks
      }
      return render(request, 'trackart/notfound.html', context=context)
      


######   CLIENT

class ClientView(TemplateView):
   def get(self, request, art_clientid):
      qsclient = art_client.objects.filter(pk=art_clientid)
      dnavlinks = getnavdictfromparamsdict(
         dparams = { 'art_clientid': art_clientid },
         cururl = request.path_info
      )
      ##{ '/viewclients': 'Client-Centric View' }
      if len(qsclient) == 1:
         qrow = qsclient[0]
         qsapt = art_appointment.objects.filter(art_clientid = art_clientid).order_by('-art_appointmenttime')
         context = {
            'qoneclient': qrow,
            'qsappointment': qsapt,
            'pkid': art_clientid,
            'dnavlinks': dnavlinks
         }
         return render(request, 'trackart/clientone.html', context=context)
      else:
         return HttpResponseRedirect('/notfound/client/' + str(art_clientid));


class ClientNotFound(TemplateView):
   def get(self, request):
      return render(request, 'trackart/clientnotfound.html')
      


#############################
##
##    CLIENT - WRITE
##


class ClientNew(TemplateView):
   def get(self, request):
      form = ClientForm()
      dnavlinks = getnavdictfromparamsdict(
         dparams = { 'art_clientid': 0 },
         cururl = request.path_info
      )
      context = {
         'form': form,
         'dnavlinks': dnavlinks
      }
      return render(request, 'trackart/clientwrite.html', context=context)

   def post(self, request):
      thisform = ClientForm(request.POST)
      dnavlinks = getnavdictfromparamsdict(
         dparams = { 'art_clientid': 0 },
         cururl = request.path_info
      )
      if thisform.is_valid():
         ## process:
         qc = art_client.objects.create(
            art_clientfirstname = thisform.cleaned_data.get("art_clientfirstname"),
            art_clientlastname = thisform.cleaned_data.get("art_clientlastname"),
            art_clientdob = thisform.cleaned_data.get("art_clientdob")
         )
         qc.save()
         ## go back to client:
         return HttpResponseRedirect('/client/' + str(qc.id));
      else:
         ## send them back to the form:
         ##   >> TO REFACTOR >>  WHY DO I HAVE TO REPLICATE THIS IN THE 'GET' AND POST?
         form = ClientForm(request.POST)
         context = {
            'form': thisform,
            'dnavlinks': dnavlinks
         }
         return render(request, 'trackart/clientwrite.html', context=context)


###
###

class ClientWrite(TemplateView):
   def get(self, request, art_clientid):
      qsclient = art_client.objects.filter(pk=art_clientid)
      if len(qsclient) == 1:
         qrow = qsclient[0]
         thisdata = {
            'art_clientfirstname': qrow.art_clientfirstname,
            'art_clientlastname': qrow.art_clientlastname,
            'art_clientdob': qrow.art_clientdob
         }
         thisform = ClientForm(thisdata)
         dnavlinks = getnavdictfromparamsdict(
            dparams = { 'art_clientid': art_clientid },
            cururl = request.path_info
         )
         thiscontext = {
            'qoneclient': qrow,
            'pkid': art_clientid,
            'form': thisform,
            'dnavlinks': dnavlinks
         }
         return render(request, 'trackart/clientwrite.html', context=thiscontext)
      else:
         return HttpResponseRedirect('/notfound/client/' + str(art_clientid));
      
   def post(self, request, art_clientid):
      thisform = ClientForm(request.POST)
      if thisform.is_valid():
         ## process;
         qc = art_client.objects.get(id=art_clientid)
         qc.art_clientfirstname = thisform.cleaned_data.get("art_clientfirstname")
         qc.art_clientlastname = thisform.cleaned_data.get("art_clientlastname")
         qc.art_clientdob = thisform.cleaned_data.get("art_clientdob")
         ## this commits that AND changes LastUpdated:
         qc.save()
         return HttpResponseRedirect('/client/' + str(art_clientid));
      else:
         ##   >> TO REFACTOR >>  WHY DO I HAVE TO REPLICATE THIS IN THE 'GET' AND POST?
         thisdata = {
            'art_clientfirstname': thisform.cleaned_data.get("art_clientfirstname"),
            'art_clientlastname': thisform.cleaned_data.get("art_clientlastname"),
            'art_clientdob': thisform.cleaned_data.get("art_clientdob")
         }
         thisform = ClientForm(thisdata)
         dnavlinks = getnavdictfromparamsdict(
            dparams = { 'art_clientid': art_clientid },
            cururl = request.path_info
         )
         thiscontext = {
            'pkid': art_clientid,
            'form': thisform,
            'dnavlinks': dnavlinks
         }
         return render(request, 'trackart/clientwrite.html', context=thiscontext)
         

####
class ClientDelete(TemplateView):
   def get(self, request, art_clientid):
      art_client.objects.filter(id=art_clientid).delete()
      return HttpResponseRedirect('/viewclients')
   

##
## /client write
##



######   APPOINTMENTS


class AppointmentView(TemplateView):
   def get(self, request, art_appointmentid):
      qsappointment = art_appointment.objects.filter(pk=art_appointmentid)
      if len(qsappointment) == 1:
         qrow = qsappointment[0]
         qspainting = art_painting.objects.filter(art_appointmentid = art_appointmentid).order_by('-createDate')
         dnavlinks = getnavdictfromparamsdict(
            {  'art_appointmentid': art_appointmentid,
               'art_clientid': qrow.art_clientid.id
            },
            request.path_info
         )
         context = {
            'qoneappointment': qrow,
            'qspainting': qspainting,
            'pkid': art_appointmentid,
            'dnavlinks': dnavlinks
         }
         return render(request, 'trackart/appointmentone.html', context=context)
      else:
         return HttpResponseRedirect('/notfound/appointment/' + str(art_appointmentid));


#############################
##
##    APPOINTMENTS - WRITE
##

class AppointmentNew(TemplateView):
   def get(self, request):
      thisdata = {
         'art_appointmenttime': datetime.datetime.now().strftime("%Y-%m-%dT%H:%M")
      }
      if 'art_clientid' in request.GET.keys():
         thisdata['art_clientid'] = request.GET['art_clientid']
      thisform = AppointmentForm(thisdata)
      dnavlinks = getnavdictfromparamsdict(
         {  'art_appointmentid': 0  },
         request.path_info
      )
      context = {
         'form': thisform,
         'dnavlinks': dnavlinks
      }
      return render(request, 'trackart/appointmentwrite.html', context=context)

   def post(self, request):
      thisform = AppointmentForm(request.POST)
      if thisform.is_valid():
         ## process:
         print(thisform.cleaned_data.get('art_appointmenttime'))
         qa = art_appointment.objects.create(
            art_clientid = thisform.cleaned_data.get("art_clientid"),
            art_appointmenttime = thisform.cleaned_data.get("art_appointmenttime")
         )
         qa.save()
         ## go to Appointment:
         return HttpResponseRedirect('/appointment/' + str(qa.id));
      else:
         ## send them back to the form:
         ##   >> TO REFACTOR >>  WHY DO I HAVE TO REPLICATE THIS IN THE 'GET' AND POST?
         form = AppointmentForm(request.POST)
         dnavlinks = getnavdictfromparamsdict(
            {  'art_appointmentid': 0 },
            request.path_info
         )
         context = {
            'form': thisform,
            'dnavlinks': dnavlinks
         }
         return render(request, 'trackart/appointmentwrite.html', context=context)


###

class AppointmentWrite(TemplateView):
   def get(self, request, art_appointmentid):
      qsappointment = art_appointment.objects.filter(pk=art_appointmentid)
      if len(qsappointment) == 1:
         qrow = qsappointment[0]
         thisdata = {
            'art_clientid': qrow.art_clientid.pk,
            'art_appointmenttime': qrow.art_appointmenttime
         }
         thisform = AppointmentForm(thisdata)
         dnavlinks = getnavdictfromparamsdict(
            {  'art_appointmentid': art_appointmentid,
               'art_clientid': qrow.art_clientid.id
            },
            request.path_info
         )
         thiscontext = {
            'qoneappointment': qrow,
            'pkid': art_appointmentid,
            'form': thisform,
            'dnavlinks': dnavlinks
         }
         return render(request, 'trackart/appointmentwrite.html', context=thiscontext)
      else:
         return HttpResponseRedirect('/notfound/appointment/' + str(art_appointmentid));
         
               
   def post(self, request, art_appointmentid):
      thisform = AppointmentForm(request.POST)
      if thisform.is_valid():
         ## process;
         qa = art_appointment.objects.get(id=art_appointmentid)
         qa.art_clientid = thisform.cleaned_data.get("art_clientid")
         qa.art_appointmenttime = thisform.cleaned_data.get("art_appointmenttime")
         ## this commits that AND changes LastUpdated:
         qa.save()
         return HttpResponseRedirect('/appointment/' + str(art_appointmentid));
      else:
         ##   >> TO REFACTOR >>  WHY DO I HAVE TO REPLICATE THIS IN THE 'GET' AND POST?
         thisdata = {
            'art_clientid': thisform.cleaned_data.get("art_clientid"),
            'art_appointmenttime': thisform.cleaned_data.get("art_appointmenttime")
         }
         thisform = AppointmentForm(thisdata)
         dnavlinks = getnavdictfromparamsdict(
            {  'art_appointmentid': art_appointmentid },
            request.path_info
         )
         thiscontext = {
            'pkid': art_appointmentid,
            'form': thisform,
            'dnavlinks': dnavlinks
         }
         return render(request, 'trackart/appointmentwrite.html', context=thiscontext)


##

class AppointmentDelete(TemplateView):
   def get(self, request, art_appointmentid):
      art_appointment.objects.filter(id=art_appointmentid).delete()
      return HttpResponseRedirect('/viewappointments')



##
## /appointments write
##




######   PAINTINGS

class PaintingView(TemplateView):
   def get(self, request, art_appointmentid, art_paintingid):
      qspainting = art_painting.objects.filter(pk=art_paintingid, art_appointmentid=art_appointmentid)
      if len(qspainting) == 1:
         qrow = qspainting[0]
         dnavlinks = getnavdictfromparamsdict(
            {  'art_paintingid': qrow.pk,
               'art_appointmentid': qrow.art_appointmentid.id,
               'art_clientid': qrow.art_appointmentid.art_clientid.id
            },
            request.path_info
         )
         context = {
            'qpainting': qrow,
            'pkid': art_paintingid,
            'dnavlinks': dnavlinks
         }
         return render(request, 'trackart/paintingone.html', context=context)
      else:
         return HttpResponseRedirect('/notfound/painting/' + str(art_paintingid));

#############################
##
##    PAINTING - WRITE
##

class PaintingNew(TemplateView):
   def get(self, request, art_appointmentid):
      thisform = PaintingForm()
      dnavlinks = getnavdictfromparamsdict(
         {  'art_paintingid': 0,
            'art_appointmentid': art_appointmentid,
            'art_clientid': art_appointment.objects.get(pk = art_appointmentid).art_clientid.id
         },
         request.path_info
      )
      context = {
         'form': thisform,
         'art_appointmentid': art_appointmentid,
         'dnavlinks': dnavlinks
      }
      return render(request, 'trackart/paintingwrite.html', context=context)

   def post(self, request, art_appointmentid):
      thisform = PaintingForm(request.POST)
      if thisform.is_valid():
         ## process:
         ## 1) write the painting:
         qpaint = art_painting.objects.create(
            art_appointmentid = art_appointment.objects.get(pk = art_appointmentid),
            art_paintingtitle = thisform.cleaned_data.get('art_paintingtitle')
         )
         qpaint.save()
         qpaint.paintcolors.set( thisform.cleaned_data.get('paintcolors') )
         qpaint.clientmoods.set( thisform.cleaned_data.get('clientmoods') )

         ## go to Painting:
         return HttpResponseRedirect('/appointment/' + str(art_appointmentid) + '/painting/' + str(qpaint.id));
      else:
         ## send them back to the form:
         ##   >> TO REFACTOR >>  WHY DO I HAVE TO REPLICATE THIS IN THE 'GET' AND POST?
         form = PaintingForm(request.POST)
         dnavlinks = getnavdictfromparamsdict(
            {  'art_paintingid': 0,
               'art_appointmentid': art_appointmentid,
               'art_clientid': art_appointment.objects.get(pk = art_appointmentid).art_clientid.id
            },
            request.path_info
         )
         context = {
            'form': thisform,
            'art_appointmentid': art_appointmentid,
            'dnavlinks': dnavlinks
         }
         return render(request, 'trackart/paintingwrite.html', context=context)


###

class PaintingWrite(TemplateView):
   def get(self, request, art_appointmentid, art_paintingid):
      qpaint = art_painting.objects.filter(pk=art_paintingid, art_appointmentid=art_appointmentid)
      if len(qpaint) == 1:
         qrow = qpaint[0]
         thisform = PaintingForm(
            initial={
               'art_paintingtitle': qrow.art_paintingtitle,
               'paintcolors': qrow.paintcolors.all(),
               'clientmoods': qrow.clientmoods.all()
            }
         )
         dnavlinks = getnavdictfromparamsdict(
            {  'art_paintingid': art_paintingid,
               'art_appointmentid': art_appointmentid,
               'art_clientid': qrow.art_appointmentid.art_clientid.id
            },
            request.path_info
         )
         thiscontext = {
            'qonepainting': qrow,
            'pkid': art_paintingid,
            'art_appointmentid': art_appointmentid,
            'form': thisform,
            'dnavlinks': dnavlinks
         }
         return render(request, 'trackart/paintingwrite.html', context=thiscontext)
      else:
         return HttpResponseRedirect('/notfound/painting/' + str(art_paintingid));
      
   def post(self, request, art_appointmentid, art_paintingid):
      thisform = PaintingForm(request.POST)
      if thisform.is_valid():
         ## process:
         ## 1:  (Update the core table)
         qp = art_painting.objects.get(id=art_paintingid)
         qp.art_paintingtitle = thisform.cleaned_data.get("art_paintingtitle")
         ## this commits that AND changes LastUpdated:
         qp.save()
         ## 2:  update the Set:
         art_painting.objects.filter(id=art_paintingid)[0].paintcolors.set( thisform.cleaned_data.get('paintcolors') )
         art_painting.objects.filter(id=art_paintingid)[0].clientmoods.set( thisform.cleaned_data.get('clientmoods') )
         ## redirect
         return HttpResponseRedirect('/appointment/' + str(art_appointmentid) + '/painting/' + str(art_paintingid));
      else:
         ##   >> TO REFACTOR >>  WHY DO I HAVE TO REPLICATE THIS IN THE 'GET' AND POST?
         form = PaintingForm(request.POST)
         dnavlinks = getnavdictfromparamsdict(
            {  'art_paintingid': art_paintingid,
               'art_appointmentid': art_appointmentid,
               'art_clientid': art_appointment.objects.get(pk = art_appointmentid).art_clientid.id
            },
            request.path_info
         )
         context = {
            'form': thisform,
            'art_appointmentid': art_appointmentid,
            'dnavlinks': dnavlinks
         }
         return render(request, 'trackart/paintingwrite.html', context=context)


##

class PaintingDelete(TemplateView):
   def get(self, request, art_appointmentid, art_paintingid):
      art_painting.objects.filter(id=art_paintingid).delete()
      return HttpResponseRedirect('/appointment/' + str(art_appointmentid))

