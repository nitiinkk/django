## Install and Setup Django
- https://stackoverflow.com/questions/36446599/zsh-command-not-found-django-admin-when-starting-a-django-project
- Getting started : ```django-admin startproject mysite```
- asgi.py and wsgi.py are related to serving our python django application
- ```python3 manage.py runserver``` built in command for starting the preview environment
- ```python3 manage.py startapp app-name``` creates app in the django project, we refer to the convention of apps instead of module.

## Urls & Views
<img src="./img/req-res-flow.png" alt="req-res-cycle">

## Dynamic Path segment & Captured Values
- Dynamic Path segment: So these act as keyword arguments, which Django will use to forward the captured values for these dynamic parameters to the view function that is being executed.
- And in there, we could now check with the IF statement, for example, if month is equal to January.

## Path Converters
```<int:month>``` can be used to call different view based on the type of value passed
- https://docs.djangoproject.com/en/5.1/topics/http/urls/#path-converters

## Templates & Static Files
### Adding and Registering Template
- In settings.py, APP_DIRS = True, so if we register our app officialy in settings.py , it would look for templates folder in our app.
- Under INSTALLED_APPS, add the appName from apps.py
- from django.template.loader import render_to_string
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### template language and variable interpolation
- 