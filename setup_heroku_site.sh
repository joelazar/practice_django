heroku run python manage.py migrate --run-syncdb
heroku run python manage.py createsuperuser
heroku run python manage.py loaddata catalog/fixtures/initial_data.json
