# Art Therapy sample application
	
__A client x appointment x painting's-quantitative-data application, built so that I can learn Django (and Python) with a simple interface for a several-layered database schema.__


##  Setup:
Before you can run this application, you will need to install Python and Django, download my code from GitHub, perform 2 command line statements to set up and populate the database, then 1 command line statement to run the Django server.  Here is how I did this:

1. I installed Python and Django locally; this should explain how to do this:
	* [Installing Django](https://docs.djangoproject.com/en/3.0/topics/install/)
	* For example:  I installed Python 3.8.1,
	* and Django 3.0
	* on a Windows 7 machine
1. Download this GitHub code base
1. Then run the Django database migration, to create (and populate where applicable) my application's database tables into Django's built-in database:
	* for example, in Windows with Python installed, open the Command Line, change-directory to the 'arttherapy\arttherapy' folder with its manage.py file, and enter:
	*  `python manage.py makemigrations trackart`
	* then enter:
	*  `python manage.py migrate`
	* this will create the database tables, and populate the 'lookup' tables, so you have all the database you need for the application's CRUD functionality.
1. Next you run the Django server for this Project;
	* for example, in Windows with Python installed, for example, open the Command Line, change-directory to the 'arttherapy\arttherapy' folder with its manage.py file, and enter:
	*  `python manage.py runserver`
1. Then you can see the application running locally at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


###	 What to do / see:
Start by adding a few Clients, Appointments, and Paintings.  Then go back to the TrackArt homepage and check out the Reporting section to see the quantitative number crunching.

Another neat feature is the navigation bar at the top:  based on a few parameters, it derives context, to show you links to 'related' sections, as well as the 'back to' area which functions like a breadcrumb.


===

##  What this application is for:

This was so I could learn Django by using it to create the kind of intranet applications I'm used to:  simple but tidy interface, with database complexity.  I didn't create login-s because I wanted to get into the complex database functionality I normally work with, rather than the write-once infrastructure/overhead of a login; however this application is intended as part of an intranet, and you would want login functionality for this application.


###  Origin of this application:

For job interview candidates at my last position, we found that asking candidates for Code Samples wasn't providing value.  In response to this, I wrote a description of an application (very similar to this application), and the candidate was asked to describe the database schema they would use to build that application and describe how that database schema would handle a few specific reports, its future flexibility for changes to the application, etc.  I focused on database schema because coming up with the underlying database schema to support customer's application was the most complex part of the job.  Poor database design means the application was built on a faulty foundation, resulting in applications with out-of-control development timelines and/or bloated or hard to maintain code.


###  Things I'd like to refactor, given more time:

My goal was to build a Django application which achieved the current level of functionality, but there were a few things I thought about along the way.  These aren't as high a priority as the next things I want to learn, but I might return to them in the future:

The Appointment Model's `__str__(self)` summary should probably include it's Appointment Time, a datetime field.  However I couldn't figure out how to timezone-massage the data to the project's 'default' timezone in the `__str__(self)` module interface, so I couldn't use their `__str__(self)` display in my Views.  It's also possible that it's Django best practices to not use `__str__(self)` for customer-facing displays, and to instead reserve it for database-backend / admin type views -- I couldn't find a solid answer to that in the time I wanted to spend on it.

In Views.py, I was disappointed by my inability to normalize the Add/Edit pages' post()-that-fails-validation sections.  I would prefer that their "re-preparing the form" part was able to re-use the same code that the get() section uses.  I guess it's not important (it's 3-8 lines of code) but my instinct is to normalize as much as possible.

Another learning opportunity could be to break the TrackArt Application into one Application per Module -- TrackArtClient, TrackArtAppointment, TrackArtPainting -- as it would help make smaller applications, smaller View.py files, and help me learn how Django communicates between Applications.  However, this is only valuable if Applications are meant to be small modular pieces that you can split into 3-5 different endpoints each, and if the overhead of reaching from Application to Application on a regular basis is low; I would have to do further reading about Django to see if this is the case.
