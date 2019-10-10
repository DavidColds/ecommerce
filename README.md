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
- The code was developed locally using the Atom Editor.
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
