''' create venv (python -m venv: Name) ''' 
from networkx import cartesian_product


Windows: python -m venv venv  (C:\python_310\python.exe -m venv Y:\Vitali\Python\13F_Database\venv)
Ubuntu:  python3 -m venv venv

''' activate venv ''' 
Windows: venv\Scripts\activate
Ubuntu: . venv/bin/activate

pip install -r requirements.txt
python manage.py runserver
Break --> Strg C

''' getbootstrap '''
https://getbootstrap.com/

----------------------------------------------------- Git Start --------------------------------------------------------
git config --global user.email "vitali.ulrich@mailbox.org"
git config --global user.name "Timeless-Energy"

git log  --graph --all --oneline
git checkout

----------------------------------------------------- Git End --------------------------------------------------------



----------------------------------------------------- Django 4.2 Start -------------------------------------------------
# 1
# wsgi.py (synchron) - standard
Web Server, Gateway Interface (Apache, Nginx, Gunicorn,..)
# asgi.py (asynchron)y
Asynchronous Server, Gateway Interface (Daphne, Hypercorn,..)

# 2
# create DJANGO Project: app
https://www.djangoproject.com/download/
pip install Django==4.2.13
django-admin startproject app
python manage.py runserver

# 3
# create Django app: main
python manage.py startapp main
python manage.py startapp goods

# 4
# activate django default database
python manage.py migrate

# 5
# goods/models.py
python manage.py makemigrations
python manage.py migrate

# 6
# admin passwort
python manage.py createsuperuser

# 7
# goods/admin.py
    from goods.models import Categories
    admin.site.register(Categories)

# 8
# goods/models.py
    class Meta:
        db_table = 'category'
        verbose_name = 'categorie'
        verbose_name_plural = 'categories'

# 9
# goods/models.py
    class Products(models.Model):
pip install Pillow
python manage.py makemigrations
python manage.py migrate 

# 10
# database
pip install ipython
python manage.py shell
'from goods.models import Categories'
'Categories.objects'
'Categories.objects.create(name='Küche', slug='Kitchen')'
'quit()'

# 11
# requirements.txt
pip freeze > requirements.txt
pip install -r requirements.txt

# 12
# PostgreSQL
python manage.py dumpdata goods.Categories > fixtures/goods/categories.json
python manage.py dumpdata goods.Products > fixtures/goods/products.json

# 13
# pgAdmin4
# SQL Shell(psql)
create user name: home
create databases: home
https://docs.djangoproject.com/en/5.0/ref/databases/#postgresql-notes
pip install psycopg2

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'home',
        'USER': 'home',
        'PASSWORD': 'Django#7777',
        'HOST': 'localhost',  # 127.0.0.1
        'PORT': '5432',  # Django Port: 8000

        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',        
    }
}
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata fixtures/goods/categories.json
python manage.py loaddata fixtures/goods/products.json

# 14
# Users
python manage.py startapp users

# 15
# form
<form action="{% url "user:login" %}" method="post">
    {% csrf_token %} 
    {% for item in form %}
        <div class="mb-3">
            <label for="{{ item.id_for_label }}" class="form-label">{{ item.label }}</label>
            {{ item }}
    </div>                       
    {% endfor %}    
    <button type="submit" class="btn btn-dark btn-block">Войти</button> 
</form>

# 16
python manage.py startapp carts
python manage.py makemigrations
python manage.py migrate

# 16
python manage.py startapp orders
python manage.py makemigrations
python manage.py migrate





----------------------------------------------------- Django 4.2 End -------------------------------------------------
''' DJANGO-ADMIN ''' 
django-admin check                       # Checks the entire django project for potential problems
django-admin changepassword <username>   # Allows changing a user’s password. It prompts you to enter a new password twice for the given user.
django-admin clearsessions               # Can be run as a cron job or directly to clean out expired sessions.
django-admin collectstatic               # Helps to collect all the static files in the one mentioned directory
django-admin createsuperuser             # Creates a superuser account (a user who has all permissions).
django-admin compilemessages             # Compiles .po files to .mo files for use with builtin gettext support
django-admin createcachetable            # Creates the tables needed to use the SQL cache backend.
django-admin dbshell                     # Runs the command-line client for specified database, or the default database if none is provided.
django-admin diffsettings                # Displays differences between the current settings.py and Django's default settings.
django-admin dumpdata                    # Output the contents of the database as a fixture of the given format (using each model's default manager unless --all is specified).
django-admin flush                       # Removes ALL DATA from the database, including data added during migrations. Does not achieve a "fresh install" state.
django-admin inspectdb                   # Introspects the database tables in the given database and outputs a Django model module.
django-admin loaddata                    # Installs the named fixture(s) in the database.
django-admin makemessages                # Runs over the entire source tree of the current directory and pulls out all strings marked for translation. It creates (or updates) a message file in the conf/locale (in the django tree) or locale (for projects and applications) directory. You must run this command with one of either the --locale, --exclude, or --all options.
django-admin help                        # display usage information and a list of the commands provided by each application
django-admin makemigrations              # create new migrations to the database based on the changes detected in the models
django-admin migrate                     # synchronize the database state with your current state project models and migrations
django-admin remove_stale_contenttypes   # Deletes stale content types (from deleted models) in your database.y.
django-admin runserver <port>            # start the development webserver at 127.0.0.1 with the port <port> default 8000
django-admin sendtestemail               # Sends a test email to the email addresses specified as arguments.
django-admin shell                       # Runs a Python interactive interpreter. Tries to use IPython or bpython, if one of them is available. Any standard input is executed as code.
django-admin showmigrations              # Shows all available migrations for the current project.
django-admin sqlflush                    # Returns a list of the SQL statements required to return all tables in the database to the state they were in just after they were installed.
django-admin sqlmigrate                  # Prints the SQL statements for the named migration.
django-admin sqlsequencereset            # Prints the SQL statements for resetting sequences for the given app name(s).
django-admin squashmigrations            # Squashes an existing set of migrations (from first until specified) into a single new one.
django-admin startapp <Appname>          # create a new django application with the specified name
django-admin startproject <ProjectName>  # create a new project directory structure
django-admin testserver                  # Runs a development server with data from the given fixture(s).
django-admin version                     # display the current django version


----------------------------------------------------- Django 3.2 PRF_DE_Tools-mit-Django Start -------------------------------------------------
# create DJANGO app: webtools, compressormodel
python manage.py startapp webtools
python manage.py startapp compressormodel

# migration --> models.py
python manage.py makemigrations
python manage.py migrate

# multiple databases
**router.py**
**models.py**
**admin.py**
python manage.py makemigrations compressormodel
python manage.py migrate --database=db1compressor

# admin
python manage.py createsuperuser
----------------------------------------------------- Django 3.2 PRF_DE_Tools-mit-Django End -------------------------------------------------



