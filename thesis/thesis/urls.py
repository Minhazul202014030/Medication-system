"""thesis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from thesis import views
from .views import show_medicine_name1

from .views import show_medicine_name2
from .views import show_medicine_name3
from .views import show_medicine_name4
from .views import show_medicine_name5
from .views import show_medicine_name6

from .views import show_medicine_name7
from .views import show_medicine_name8
from .views import show_medicine_name9
from .views import show_medicine_name10
from .views import show_medicine_name11

from .views import show_medicine_name12
from .views import show_medicine_name13
from .views import show_medicine_name14
from .views import show_medicine_name15
from .views import show_medicine_name16

from .views import show_medicine_name17
from .views import show_medicine_name18
from .views import show_medicine_name19
from .views import show_medicine_name20


# from .views import predict_insulin

urlpatterns = [
    path('', views.check_reminders, name='check_reminders'),
    path('admin/', admin.site.urls),
    path('about-us/', views.ABOUTUS),
    path('alert/', views.ALERT),
    path('box/', views.BOX),
    path('index/', views.INDEX),
    path('insulin/', views.INSULIN),
    path('schedule/', views.SCHEDULE),
    path('seeboxname/', views.SEEBOXNAME),
    path('seeschedule/', views.SEESCHEDULE),
    path('test/', views.TEST),
    path('timer/', views.TIMER),
    path('schedule-updated/', views.SCHEDULE_UPDATED),

    path('saveenquiry/', views.saveEnquery,name="saveenquiry"),
    path('savereminder/', views.saveReminder,name="savereminder"),
    path('check_reminders/', views.check_reminders, name='check_reminders'),
    path('show_reminders/', views.show_reminders, name='show_reminders'),

    # path('show_medicine1/', show_medicine_name1, name='show_medicine_name1'),


    path('show_medicine16/', show_medicine_name1, name='show_medicine_name1'),
    path('show_medicine18/', show_medicine_name2, name='show_medicine_name2'),
    path('show_medicine22/', show_medicine_name3, name='show_medicine_name3'),
    path('show_medicine40/', show_medicine_name4, name='show_medicine_name4'),
    path('show_medicine5/', show_medicine_name5, name='show_medicine_name5'),

    path('show_medicine6/', show_medicine_name6, name='show_medicine_name6'),
    path('show_medicine7/', show_medicine_name7, name='show_medicine_name7'),
    path('show_medicine8/', show_medicine_name8, name='show_medicine_name8'),
    path('show_medicine9/', show_medicine_name9, name='show_medicine_name9'),
    path('show_medicine10/', show_medicine_name10, name='show_medicine_name10'),

    path('show_medicine11/', show_medicine_name11, name='show_medicine_name11'),
    path('show_medicine12/', show_medicine_name12, name='show_medicine_name12'),
    path('show_medicine13/', show_medicine_name13, name='show_medicine_name13'),
    path('show_medicine14/', show_medicine_name14, name='show_medicine_name14'),
    path('show_medicine15/', show_medicine_name15, name='show_medicine_name15'),

    path('show_medicine16/', show_medicine_name16, name='show_medicine_name16'),
    path('show_medicine17/', show_medicine_name17, name='show_medicine_name17'),
    path('show_medicine18/', show_medicine_name18, name='show_medicine_name18'),
    path('show_medicine19/', show_medicine_name19, name='show_medicine_name19'),
    path('show_medicine20/', show_medicine_name20, name='show_medicine_name20'),
    
    
    
    
    # path('index2/', views.INDEX2),
]
