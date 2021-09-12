# How to Setup

### Step 1 - Create and activate virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

### Step 2 - Install all the dependencies

```
pip3 install -r requirements.txt
```

### Step 3 - Setup MYSQL Credentials

First create a database in mysql and add the credentials to DATABASE in settings.py

```
'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_name',
        'USER': 'db_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
```

### Step 4 - Migrate the changes to database

```
python3 manage.py migrate
```

### Step 5 - Create a superuser/admin for accessing admin panel

```
python3 manage.py createsuperuser
```

Please enter information as per instruction

### Step 6 - Now let's start the server

```
python3 manage.py runserver
```

### Step 7 - Now visit localhost:8000

1. For web application [Click Here](http://localhost:8000)
2. For admin panel [Click Here](http://localhost:8000/admin)
