# coding=utf-8
"""simplecmdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from hostinfo import views

admin.autodiscover()
urlpatterns = [
    url(r'^admin/',admin.site.urls), #django后台管理登入url
    url(r'^api/gethost\.json$',views.gethosts()),#nagios客户端访问API接口地址
    url(r'^api/clooect$', views.collect()),#客户端访问API进行上传数据的API
]


