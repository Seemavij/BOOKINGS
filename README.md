* Resturant Bookings:
 >The idea behind this project is to create a site for a restaurant that can manage reservations. On deployment all the restaurant details, including contact details, openings hours, booking details, and categories have already been set up, however this can be edited as the admin wants thus making the content changeable. Much of the content is auto generated on the pages, and the admin can set up their preferred criteria.

* The development 
> for this project is to create an application that meets a real-life need, which is the need for restaurant owners to digitalise the process of taking orders, sorting tables, and avoiding double bookings. Much of it should be automatic, including emails.

* project - main
> reservations - contains the booking and table models as well as the booking and profile form. Contains all the views related to booking, both for admin and users. Also contains all the booking logic in a separate file booking.py.
homepage - simply contains the view for the index page and the 404 view code.
contact - contains the view codes for the contact pages as well as the forms
menu - contains the view for the menu page as well as the two models; Category and Meals.
restaurant - contains two models: OpeningHours and BookingDetailsDjango Apps:

* CRUDS:
> Create - Users and admin can create objects in the Booking model via the booking form + booking view code on the booking page. Admin can additionally create objects via the admin panel.

> Reading - Users can find their past (previous bookings page) and future booking (upcoming bookings page) object on their site and see the booking details (booking details page). Admin can see all bookings in admin panel, or filtered bookings on the pending bookings page, accepted bookings page, and the updated bookings page.

> Updating - Users can update their future bookings on the upcoming bookings page using the UpdateView class. It is limited in that they can only alter the comment. However, admin is able to alter every aspect of the booking objects, done in the admin panel, pending bookings, updated bookings, and accepted bookings, and can alter bookings from any time.

> Deletion -Users can delete their future bookings on the upcoming bookings page. Admin can delete bookings via the pending bookings, updated bookings, accepted bookings, and can delete all bookings from any time.

Email
* Additional Information mentions:
> New postgres: https://www.elephantsql.com/ Not Heroku anymore: Gitpod had new dependencies. I Followed the instructions: * find -name "deps.txt" - no results, which meant that I had the older version * ran pip3 freeze > unins.txt && pip3 uninstall -y -r unins.txt && rm unins.txt * pip3 install django gunicorn * pip3 install dj_database_url psycopg2 * pip3 install dj3-cloudinary-storage * pip3 install django-allauth * pip3 freeze --local > requirements.txt * saved, commited, and pushed * pip3 install Pillow * pip3 freeze --local > requirements.txt From here onwards, whenever I (re)started my workspace, I needed to do two things:

> First:
pip3 freeze > unins.txt && pip3 uninstall -y -r unins.txt && rm unins.txt
Second:
> pip3 install -r requirements.txt
command used for copying authentication templates to directory. Once copied we can make changes to the styling, and the content cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates