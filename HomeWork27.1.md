* docker run --name db_django -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=test -p 5433:5432 -v ${pwd}/docker/postgres/:/var/lib/postgresql/data postgres
* docker run --name django --network host -it python bash
  * pip install django psycopg2
  * django-admin startproject test
  * cd test
  * apt-get update
  * apt-get install nano
  * nano test/settings.py
     `DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'test',
             'USER': 'postgres',
             'PASSWORD': 'postgres',
             'HOST': '127.0.0.1',
             'PORT': '5433'
         }
     }`	
  * python manage.py migrate
  * ./manage.py runserver
