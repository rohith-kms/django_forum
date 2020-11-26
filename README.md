# django_forum
A simple forum website created in django. Users who are logged in can post and comment on posts. Other users can view posts and comments.

# Users

## Creating users:

You can create a user through the django shell `python manage.py shell`, through the following commands:

```
>>> from django.contrib.auth.models import User
>>> user = User(username='<enter-username-here>',password='<enter-password-here>')
>>> user.save()
```

## Currently added users:

Currently, 2 users exist in the database. You can use them to try out the different features here.

* __username:__ ro; __password:__ roroboat
* __username:__ potato; __password:__ momomomo

