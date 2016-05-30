#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^login/$', views.post_login, name='post_login'),
    url(r'^request/$', views.create_request, name='create_request'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^signup/$', views.create_client, name='signup'),
    url(r'^basket/$', views.cart, name='cart'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^catalogs/$', views.catalogs, name='catalogs'),
    url(r'^catalogs/([0-9]{1,2})/$', views.products, name='products'),
    url(r'^catalogs/((?P<category>\d+))/(?P<slug>[\w-]+)/$', views.product, name='product'),
    url(r'^search/$', views.search, name='search'),
] 