from django.db import models


'''
this was an attempt to standardize __str__(self) date-formatting;
HOWEVER after extensive research I haven't been able to get __str__(self) to be able to stamp Datetimes into TIME-ZONE-AWARE times, so I won't be using it on the Template front-end, instead I'll just display the fields AND times to the template front-end, where it AUTOMATICALLY time-zone-corrects.
'''
myjustdate = "%m/%d/%Y"
myfulltime = myjustdate+" %I:%M:%S %p"



'''
schema:
'''
## CORE TABLES:

class art_client(models.Model):
   art_clientfirstname = models.CharField(max_length=50)
   art_clientlastname = models.CharField(max_length=50)
   art_clientdob = models.DateField(blank=False,null=False)
   createDate = models.DateTimeField( auto_now_add=True )
   lastupdated = models.DateTimeField( auto_now=True )
   ## 'summary' of a row, for various admin / display purposes baked into django
   def __str__(self):
      return self.art_clientfirstname +' '+ self.art_clientlastname
   
class art_appointment(models.Model):
   art_clientid = models.ForeignKey(art_client, on_delete=models.CASCADE)
   art_appointmenttime = models.DateTimeField( blank=False, null=False )
   ## 'summary' of a row, for various admin / display purposes baked into django
   def __str__(self):
      return self.art_clientid.__str__() + ' at '+ self.art_appointmenttime.strftime(myfulltime)

## LOOKUP TABLES:

class paintcolor(models.Model):
   paintcolortitle = models.CharField(max_length=100)
   createDate = models.DateTimeField( auto_now_add=True )
   ## this __str__ is the 'how do i describe a row in this table?' function
   def __str__(self):
      return self.paintcolortitle

class clientmood(models.Model):
   clientmoodtitle = models.CharField(max_length=100)
   createDate = models.DateTimeField( auto_now_add=True )
   ## 'summary' of a row, for various admin / display purposes baked into django
   def __str__(self):
      return self.clientmoodtitle



## table x lookup
   
class art_painting(models.Model):
   art_appointmentid = models.ForeignKey(art_appointment, on_delete=models.CASCADE)
   art_paintingtitle = models.CharField(max_length=200, default='(Untitled)')
   createDate = models.DateTimeField( auto_now_add=True )
   lastupdated = models.DateTimeField( auto_now=True )
   paintcolors = models.ManyToManyField(paintcolor)
   clientmoods = models.ManyToManyField(clientmood)
   ## 'summary' of a row, for various admin / display purposes baked into django
   def __str__(self):
      return self.art_paintingtitle + ' by ' + self.art_appointmentid.art_clientid.art_clientfirstname + ' ' + self.art_appointmentid.art_clientid.art_clientlastname ### ', created ' + self.createDate.strftime(myfulltime)
      
