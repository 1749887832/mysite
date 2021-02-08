"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import app.bascketball.Nba as NB
import app.views as av
import jkyporttest.Logic.Test_ordercase as test
import jkyporttest.views as ja

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', av.Login_modular.l_modular),
    path('nba/', NB.NBA.get_msg),
    path('nba_msg/', NB.NBA.get_schedule),
    path('lakes/', NB.NBA.get_lakes),
    path('lakes_context/', NB.NBA.get_context),
    path('order/', test.Test_Order.start_order_test),
    path('open/', ja.open),
    path('create/', ja.create),
    path('ceshi/',ja.ceshi)
]
