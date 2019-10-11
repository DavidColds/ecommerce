[![Build Status](https://travis-ci.org/DavidColds/ecommerce.svg?branch=master)](https://travis-ci.org/DavidColds/ecommerce)

<h6>Drughi David</h6>

<h1> Full Stack Framework Milestone </h1>

<a href="https://winebordeaux.herokuapp.com/" target="_blank"> Click here to view the website </a>

## Purpose

The website for the Bordeaux vineyard located in the region of southwest France. Bordeaux is centered on the city of Bordeaux, on the Garonne River.

And I manage to do that with the help of the technologies I learnt on my coding journey to demonstrate how a SQL (Structured Query Language) based
database can be utilised efficiently and effectively to create scalable apps on the web. The aim of this project is to showcase my skill set learnt
throughout the course.
Throughout this project I will make use of Python a high-end programming language along with Django a Python framework.

## UX

This platform has been built to be fully responsive so it works perfectly on any device and screen size.
Some of the initial Wireframes for both desktop and mobile versions can be found here.
In the website you can buy, send emails, comment, review, search.
Within my app I have created a cart to accommodate the process of buying. Within this app the user has the ability to manage their purchases within
the cart. By this the user can remove items from their cart if no wanted.
I've implemented a password reset functionality to my app, this allows
registered users the ability to recovery their account and reset their passwords and a Email functionality.
The app was designed so it aid the modern style of usability across all
types of devices and screen sizes.

## User stories and Features overview

##### The Home page the user should be able to:

-   Have a easy navigation trough the page,
-   From the navigation bar the user should go the main pages,
-   The 'Explore' button will direct the user to the wines page,

-   As a user I want to navigate from the footer of the page everywhere I need, luckily
    the footer does that, from the footer can the user navigate wherever the pleases.

##### The Wines page the user should be able to:

-   As a user I want to able to se all the wines, prices and a search bar. The Wines
    page provide just that and ever a direct add to cart button.
-   As a user I want to read in detail about a wine and even read some reviews from
    other users. The pages provides just that, as the user clinks on the bottle it
    will be redirected to the product detail page, there the user can read about
    the product and reviews from others. The user is able to leave a comment and review.

##### The Cart page the user should be able to:

-   As a user who wishes to purchase, I want to have a smooths and easy time doing that,
    and the pages provides just that. As soon the user clicks on the add to cart, the
    product will be added to the cart. From the cart, the user can proceed to the paying stage.
    The user must be an official member of the vineyard( that means to have an account but ),
    otherwise he will be redirected to the register page, there he will make an account and then the user,
    will be able to finish the purchase.
-   As a user I want to see what I'm buying before proceeding, and yes, the page
    provides just that. The cart page shows exactly what the user wishes to purchase,
    the price and the quantity.
-   The user will then click on the " checkout " button and whom will be redirected
    to the checkout page, there the user will be able to write in the requirements and the order will be placed.
-   As a user who just purchase a product I want to receive some kind of confirmation,
    as soon the order is being placed, the user will receive a " Thank You page".

##### The About page the user should be able to:

-   As a user, I want to read some information about the vineyard, those informations
    can be found at the About page. At the About page the user can read about the vineyard
    and then to chose to go to Grapes or Wines page.

##### The Contact page the user should be able to:

-   As a user I want to contact the vineyard, that can be found at the Contact page.
    The user has access to: address, directions, email and phone number.
-   As a user I might want to visit and se the vineyard myself, with just a phone call,
    the user can arrange a meeting within  the opening hours.
-   The user can find a simple email form where he can email the vineyard.
-   As user on the phone I want a link with directions. The page provides a quick
    google maps area where the user can get directions and redirected to google maps.

##### The My Account page the user should be able to:

-   As a user I want a simple form where I can register an account.
    With a simple click and some few informations the website provides just that.
    Same goes for the login page.

##### The Grapes page the user should be able to:

-   As a user I would want to know what kind of grapes the vineyard produces,
    the grapes page can be found at the bottom of the Home page, above the footer.
-   On the Grapes page the user can read about every sort of grape that grows
    at the vineyard.

## Technologies

-   [HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML)
-   [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
-   [Bootstrap](https://getbootstrap.com/)
-   [JavaScript](https://developer.mozilla.org/bm/docs/Web/JavaScript)
-   [Django](https://www.djangoproject.com/)
-   [Github](https://github.com/)
-   [Heroku](https://www.heroku.com/)
-   [AWS](https://aws.amazon.com/products/databases/)
-   [Stripe](https://stripe.com/en-se)
-   [Travis](https://travis-ci.org/)

## Deployment

-   The code was developed locally using the Atom Editor and GitBash.
-   Code was then pushed to GitHub.
-   Static files and user uploads where then configured to be hosted by AWS S3 buckets.
-   Travis was then used for continuous integration.
-   Code was then deployed on Heroku.

GitHub Repo [here](https://github.com/DavidColds/ecommerce)

Getting my application ready for deployment consisted of the following: -
1. Removing all my hard-coded environment variables to project my keys and secrets. These were placed in the .bashrc for development and entered into Heroku's Config Vars for production.
2. Ensuring the applications requirements.txt is up-to-date with all the latest packages installed for my app being noted on this file.
	**The command to update requirements**
		```
		pip3 freeze > requirements.txt
		```
3. Set up the Procfile - *A Procfile is required by Heroku in order to tell the service worker what command to run for my application to start.*
4. Push all static files to S3 Bucket `python3 manage.py collectstatic`
5. Enter all my ENV vars into Heroku's config vars (A list of all my config var is listed below in expanding on my project section)
6. Push all my latest production ready code to GitHub ready for deployment via Heroku's GitHub function where you can deploy from GitHub the production ready app.

**Upon successful deployment Heroku will give you the URL that is hosted your app**

*Upon unsuccessful deployment Heroku will log the cause of the error and this is view able in the 'view log' section on the Heroku website. Here you will find a detailed report of what has cause your application not to be deployed successfully. *

### Heroku Config Var's
| Key | Value |
 --- | ---
AWS_ACCESS_KEY_ID| `<your_access_key_id>`
AWS_SECRET_ACCESS_KEY| `<your_secret_key>`
DATABASE_URL| `<your_data_base_url>`
DEFAULT_FROM_EMAIL| `<your_from_email>`
DISABLE_COLLECTSTATIC| `1`
EMAIL_HOST | `<your_email_host>`
EMAIL_HOST_PASSWORD| `<your-email-password>`
EMAIL_HOST_USER| `<your-email-address>`
SECRET_KEY| `<a_secret_key>`
SERVER_EMAIL| `<your_email_address>`
STRIPE_PUBLISHABLE| `<your_stripe_key>`
STRIPE_SECRET| `<your_stripe_secret>`

## Expanding on my Project
To get set up with a copy of my project you can do these multiple ways.

**Via GitHub** -  
1. You can manually download locally to your machine and then upload to your preferred IDE.
2. Install the projects requirements.txt using `pip3 install -r requirements.txt`
3. You will need to update a few project settings before we can run the app. Open settings folder and in local.py
	1. `ADD ALLOWED HOST`
	2.  `SET UP EMAIL CONFIG`
	3. `SET UP STRIPE API KEY/SECRET`
4. Once the above steps are complete you can try run the application using `python3 manage.py runserver $IP:$PORT`

*Please note* step 4 may be different depending on the operating system you are running, please refer to the documentation for more details on running the Django server on different OS's

**Via the CLI** -
1. Clone my repo via Git using the following command `https://github.com/DavidColds/ecommerce.git`
2. Install the projects requirements.txt using `pip3 install -r requirements.txt`
3. You will need to update a few project settings before we can run the app. Open settings folder and in local.py
	1. `ADD ALLOWED HOST`
	2.  `SET UP EMAIL CONFIG`
	3. `SET UP STRIPE API KEY/SECRET`
4. Once the above steps are complete you can try run the application using `python3 manage.py runserver $IP:$PORT`

## Testing

This project has been tested in many different ways: .
    \- I used chrome developer tools to check for errors, responsiveness and test if something was wrong with my html, css or javascript files.
    \- I used Django error page that appeared when my code had any errors, I also use print command at time with specific messages to understand if, for example, data was been aplied.
    \- As well, I used Django built-in test functionality to create automated, custom test. This had allow me to create multiple tests for my views, models, forms...
    \- I also used Travis CI by connecting it trough my Github repo.
    \- I asked friends to test my application and to give me feedback.
    \- Finally I went through lots of manual tests to understand and make sure the functionality of the website was on point.

#### Some of Manual Tests done:

\-Clicking on logo icon in navigation takes user to homepage
 Successful

\-The platform has been tested on all modern desktop and mobile browsers to ensure cross compatibility and functionalities.
  Successful

\-The platform has been tested to be fully responsive and that is correctly displayed across all of type devices.
  Successful

\-The platform has been tested to ensure that all of the user stories were functional without errors.
  Successful

\-The platform has been tested to make sure all urls work properly
  Successful

\-The platform has been tested to ensure all text-area and inputs are perfectly functioning and sending/receiving the right data.</td>
  Successful

\-All links and buttons tested to make sure they all works as they should.
  Successful

\-The user can come back to the previous window from everywhere, no rabbit holes.
  Successful

\-Data from database is been accessible at all times.
  Successful

\-Purchase process until the purchase its done works perfectly.
 Purchasing test card (4242 4242 4242 4242) random CVC and day and month expiration dates
  Successful

\-Changing password trough email works perfectly.
  Successful

\-Contact email trough Contact page works.
  Successful

\-Being able to rate and review a product works perfectly.
  Successful

## Credits

Big thanks to :
[Corey Schafer](https://www.youtube.com/user/schafer5)
[Traversy Media](https://www.youtube.com/user/TechGuyWeb)

My mentor: Anthony Ngene and slack students.

For the media and inspiration :
[unsplash](https://unsplash.com/)
[logo](https://www.freepik.com/free-vector/wine-grapes_794408.htm)
[inspiration](https://kingfamilyvineyards.com/)
[Aos](https://michalsnik.github.io/aos/)
[Colorlib](https://colorlib.com/wp/templates/)
