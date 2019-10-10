[![Build Status](https://travis-ci.org/DavidColds/ecommerce.svg?branch=master)](https://travis-ci.org/DavidColds/ecommerce)

<h6>Drughi David</h6>

<h1> Full Stack Framework Milestone </h1>

<a href="" target=" blank"> Click here to view the website </a>

## Purpose

## UX

## Features overview

### User stories

## Technologies

## Deployment
- The code was developed locally using the Atom Editor and GitBash.
- Code was then pushed to GitHub.
- Static files and user uploads where then configured to be hosted by AWS S3 buckets.
- Travis was then used for continuous integration.
- Code was then deployed on Heroku.


GitHub Repo [here](https://github.com/DavidColds/ecommerce)

### For local deployment
- Clone the project:
` git clone https://github.com/DavidColds/ecommerce.git`
- Arrange contents so that the cloned document is in the root of the environment.
- Following need to be installed

`pip install django=1.11` The framework used.

`pip  install Pillow` A python package that allows images to be uploaded.

`pip  install django-forms-bootstrap` To render our forms with bootstrap styling.

- Create AWS account. Configure an S3 bucket for public access as a place to store user uploads and static files.

`pip  install django-storages` To set up media and static transfer on S3

`python3 manage.py collectstatic` To send all media and static directories to S3

`pip  install psycopg2`
`pip  install dj-database-url==0.5.0` To handle postgres database.

- Create a new app on Heroku and link to your local repo.
- Create a requirements.txt and Procfile.

`pip freeze > requirements.txt` To tell Heroku what packages are required to run this program.

`echo web: python app.py > Procfile` To tell Heroku what type of application this is.

- Push to github
- Create a new app on Heroku.
- Add postgres database as a resource.

Set up environment variables on Heroku for:
- STRIPE_PUBLISHABLE
- STRIPE_SECRET
- EMAIL_ADDRESS
- EMAIL_PASSWORD
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY

- Link up GitHub
- Run deploy.

## Testing
<p>
This project has been tested in many different ways: .
    - I used chrome developer tools to check for errors, responsiveness and test if something was wrong with my html, css or javascript files.
    - I used Django error page that appeared when my code had any errors, I also use print command at time with specific messages to understand if, for example, data was been aplied.
    - As well, I used Django built-in test functionality to create automated, custom test. This had allow me to create multiple tests for my views, models, forms...
    - I also used Travis CI by connecting it trough my Github repo.
    - I asked friends to test my application and to give me feedback.
    - Finally I went through lots of manual tests to understand and make sure the functionality of the website was on point.


    #### Some of Manual Tests done

          Manual Testing

-Clicking on logo icon in navigation takes user to homepage
 Successful

-The platform has been tested on all modern desktop and mobile browsers to ensure cross compatibility and functionalities.
  Successful

-The platform has been tested to be fully responsive and that is correctly displayed across all of type devices.
  Successful


-The platform has been tested to ensure that all of the user stories were functional without errors.
  Successful

-The platform has been tested to make sure all urls work properly
  Successful

-The platform has been tested to ensure all text-area and inputs are perfectly functioning and sending/receiving the right data.</td>
  Successful

-All links and buttons tested to make sure they all works as they should.
  Successful

-The user can come back to the previous window from everywhere, no rabbit holes.
  Successful

-Data from database is been accessible at all times.
  Successful

-Purchase process until the purchase its done works perfectly.
  Successful

-Changing password trough email works perfectly.
  Successful

-Contact email trough Contact page works.
  Successful

-Being able to rate and review a product works perfectly.
  Successful
