[![Build Status](https://travis-ci.org/DavidColds/ecommerce.svg?branch=master)](https://travis-ci.org/DavidColds/ecommerce)

<h6>Drughi David</h6>

<h1> Full Stack Framework Milestone </h1>

<a href="" target=" blank"> Click here to view the website </a>

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

## Features overview

## User stories

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

### For local deployment

-   Clone the project:
    `git clone https://github.com/DavidColds/ecommerce.git`
-   Arrange contents so that the cloned document is in the root of the environment.
-   Following need to be installed

`pip install django=1.11` The framework used.

`pip  install Pillow` A python package that allows images to be uploaded.

`pip  install django-forms-bootstrap` To render our forms with bootstrap styling.

-   Create AWS account. Configure an S3 bucket for public access as a place to store user uploads and static files.

`pip  install django-storages` To set up media and static transfer on S3

`python3 manage.py collectstatic` To send all media and static directories to S3

`pip  install psycopg2`
`pip  install dj-database-url==0.5.0` To handle postgres database.

-   Create a new app on Heroku and link to your local repo.
-   Create a requirements.txt and Procfile.

`pip freeze > requirements.txt` To tell Heroku what packages are required to run this program.

`echo web: python app.py > Procfile` To tell Heroku what type of application this is.

-   Push to github
-   Create a new app on Heroku.
-   Add postgres database as a resource.

Set up environment variables on Heroku for:

-   STRIPE_PUBLISHABLE
-   STRIPE_SECRET
-   EMAIL_ADDRESS
-   EMAIL_PASSWORD
-   AWS_ACCESS_KEY_ID
-   AWS_SECRET_ACCESS_KEY

-   Link up GitHub
-   Run deploy.

## Testing

This project has been tested in many different ways: .
    \- I used chrome developer tools to check for errors, responsiveness and test if something was wrong with my html, css or javascript files.
    \- I used Django error page that appeared when my code had any errors, I also use print command at time with specific messages to understand if, for example, data was been aplied.
    \- As well, I used Django built-in test functionality to create automated, custom test. This had allow me to create multiple tests for my views, models, forms...
    \- I also used Travis CI by connecting it trough my Github repo.
    \- I asked friends to test my application and to give me feedback.
    \- Finally I went through lots of manual tests to understand and make sure the functionality of the website was on point.

    #### Some of Manual Tests done

          Manual Testing

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
