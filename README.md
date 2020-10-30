# Recipe Repository

I started this project as a way to keep track of all my recipes from various sites in one location. I've learned quite a bit about Django in the process and working on learning some front end to make it look nicer.

![alt text](https://raw.githubusercontent.com/kshintaku/recipe-repo/main/ss.png "Screen Shot")

## Features

- Keep track of all your recipes in a single site.
- Search all recipes featuring desired ingredients.

## Requirements

- Python 3
- Django
- Heroku (optional for deployment)

## Build Instructions

1. Clone the repository
2. Run `pip install requirements.txt`.
3. Run `$ python manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())'` to generate your own Django key.
4. Copy generated key to `.env` and replace placeholder key in the first line `DJANGO_KEY=<KEY>`.
5. Run `python manage.py migrate` to create database.
6. Create an admin account with `python manage.py createsuperuser` and fill in prompts.
7. Start the app with `python manage.py runserver`.

## How to deploy to Heroku

1. Create an account on Heroku.
2. Run through installation and setup at <https://devcenter.heroku.com/articles/getting-started-with-python>.
3. Create a new Heroku app with `heroku create`
4. Log into Heroku and navigate to your new app and go to Settings and in inside Config vars create `DJANGO_KEY` and paste the key you generated during the build; the same as in the `.env` file.
5. While in the app, go to Deploy tab and select your prefered deployment method.
6. Then click the more button next to open app and run console. Enter `python manage.py migrate` to create your deployed database.
7. You will also need to create a new admin user so be sure to run `python manage.py createsuperuser` via the console as well.

### Recipe Format

Look at `sample.json` for an example of recipe format. I suggest condensing it before pasting into database field.
