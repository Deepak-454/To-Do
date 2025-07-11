# add this to urls.py
from .models import *
urlpatterns=[path('To-Do/',work,name="To-Do"),
    path('remove_task/<id>/',remove_task,name="remove_task")]
