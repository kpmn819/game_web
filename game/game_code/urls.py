# refers to the views
from django.urls import path

from . import views

urlpatterns = [
    # the type of variable that is passed in will steer it to
    # a particular view ie: <int:id> will take any 8000/integer/ and 
    # send it to index these are called 'path converters' and
    # include int, str, slug, path, uuid
    path('<int:id>', views.index, name='index'),
    path('v1/', views.v1, name='view 1'),
    path('home/', views.home, name='home'),
]