from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #from views.home
    path("", views.home, name="home"),
    #from views.apply_job
    path("apply/", views.apply_job, name="apply"),
    path("listing-page/", views.listing_page, name="listing-page"),
    path("edit/<str:pk>/", views.edit_page, name="edit"),
    path("delete/<str:pk>/", views.delete_page, name="delete"),
]
