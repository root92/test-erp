from django.conf.urls import url
from django.contrib import admin

from . import views


urlpatterns = [
    url(r'^$', views.payement, name='payement'),
    url(r'^new-payement$', views.new_payement, name='new-payement'),
    url(r'^fees$', views.fees, name='fees'),
    url(r'^new-fee$', views.new_fee, name='new-fee'),
    url(r'^edit-fee/(\d+)/$', views.edit_fee, name='fee-edit'),
    url(r'^delete-fee/([0-9]+)$', views.delete_fee, name='fee-delete'),
]
