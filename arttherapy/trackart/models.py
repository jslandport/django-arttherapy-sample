from django.db import models

# Create your models here.

'''
schema:

NOTE - evidently you don't specify PKid-s, they're just "implicit", and you "implicitly" foreign-key to the table itself.
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
      return self.art_clientlastname +', '+ self.art_clientfirstname
   
class art_appointment(models.Model):
   art_clientid = models.ForeignKey(art_client, on_delete=models.CASCADE)
   art_appointmenttime = models.DateTimeField( blank=False, null=False )
   ## 'summary' of a row, for various admin / display purposes baked into django
   def __str__(self):
      return str(self.art_clientid)+' at '+str(self.art_appointmenttime)
   
class art_painting(models.Model):
   art_appointmentid = models.ForeignKey(art_appointment, on_delete=models.CASCADE)
   createDate = models.DateTimeField( auto_now_add=True )
   ## 'summary' of a row, for various admin / display purposes baked into django
   def __str__(self):
      return 'appointment=' + str(self.art_appointmentid)+'; paintingId ' + str(self.id)


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

## MANY X MANY CONNECTORS:

class art_paintingXpaintcolor(models.Model):
   art_paintingid = models.ForeignKey(art_painting, on_delete=models.CASCADE)
   paintcolorid = models.ForeignKey(paintcolor, on_delete=models.CASCADE)
   createDate = models.DateTimeField( auto_now_add=True )
   def __str__(self):
      return str(self.art_paintingid)+' --> '+str(self.paintcolorid)

class art_paintingXclientmood(models.Model):
   art_paintingid = models.ForeignKey(art_painting, on_delete=models.CASCADE)
   clientmoodid = models.ForeignKey(clientmood, on_delete=models.CASCADE)
   createDate = models.DateTimeField( auto_now_add=True )
   def __str__(self):
      return str(self.art_paintingid)+' --> '+str(self.clientmoodid)

