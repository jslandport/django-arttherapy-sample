   Art Therapy sample application

   A straightforwards client x appointment x painting's-quantitative-data application, built so that I can learn Django (and Python) with a simple interface for a several-layered database schema.


   Setup:
To run this application you will need to install Python and Django, and create a new Django Project to drop this codebase into.  Here is how I did this:

1) You should have Python and Django installed locally; this should document that process:
  https://docs.djangoproject.com/en/3.0/topics/install/
-I installed Python 3.8.1
-and Django 3.0

2) Then you need to create a Django Project called 'arttherapy' -- the equivalent of a new stand-alone server
-in Windows with Python installed, for example, open the Command Line, change-directory to where Django is installed, then enter:
  django-admin startproject arttherapy
-it's possible I could eliminate this step by including more Django infrastructure in my GitHub repository;
-it doesn't seem like a valuable overhead, and I don't know enough about how Django instantiates itself to know if I would still be missing something / would have to account for different operating systems, etc:
-my goal was to Version Control the code I wrote, not the code necessary to instantiate Django.

3) Once that has set up the instance of the Django server, you can extract my /arttherapy/ GitHub code into the 'django/arttherapy' root folder

4) Then run the Django database migration, to create (and populate where applicable) my application's database tables into Django's database
-in Windows with Python installed, for example, open the Command Line, change-directory to the django/arttherapy root folder, and enter:
  python manage.py migrate

5) Next you run the Django server for this Project;
-in Windows with Python installed, for example, open the Command Line, change-directory to the django/arttherapy root folder, and enter:
  python manage.py runserver

6) Finally you can see the application locally here:
http://127.0.0.1:8000/


   What to do / see:
Start by adding a few Clients, Appointments, and Paintings.  Then check out the Reporting section to see the quantitative number crunching.

Another neat feature is the navigation bar at the top:  based on a few parameters, it derives context, to show you links to 'related' sections, as well as the 'back to' area which functions like a breadcrumb.


   Origin of this application:
For job interview candidates at my last position, we found that asking candidates for Code Samples wasn't providing value.  So I wrote a description of an application (very similar to this application).  The candidate was asked to write the database schema they would use to build that application, then talk about how that database schema would handle reporting, changes to the application, etc.  This is because learning what the customer wants, then coming up with the underlying database design schema behind that application, was the most complex part of the job.  Poor database design would mean the application was built on a faulty foundation, and was likely to doom or damage the final product.


===

>>>
to write better:
>>>

   My takeaways from learning Django:

   What this application is for:
Learning Django by using it to create the kind of intranet applications I'm used to:  simple but tidy interface with database complexity.  I didn't do a "login" because I wanted to get into the complex functionality I normally use rather than the infrastructure/overhead, though obviously this would be an intranet application and thus would have a login functionality.


   Things to refactor:
The Appointment Models might be best with "Date-Time" as part of its __str__(self) summary; however I can't figure out how to timezone-massage the data to the 'default' timezone in the __str__(self) module interface, so I can't use their __str__ display in my Views.  (Maybe it's best practices Not to use __str__ in the application, and reserve it exclusively for database-backend / admin type views, I couldn't find a solid answer to that).

In Views.py, I think it would be a little better if I could normalize the write pages' post()-that-fails-validation sections that re-prepares the form; I guess it's not important (it's 3-8 lines of code) but my instinct is to normalize as much as possible.

