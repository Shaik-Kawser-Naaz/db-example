from django.urls import path
from app1 import views
urlpatterns=[
    path('',views.home,name="homepage"),
    path('createauthor',views.createauthor,name="author"),
    path('createbook',views.createbook,name="book")
]