from django.urls import include, path
from .views import *

app_name ="blog"

urlpatterns = [
    
    path("" , home , name="home") ,
    path("about-us/" , about_us , name="about-us") ,
    path("single-event/<int:pk>/" , single_event , name="single-event") ,

    path("causes/" , causes_view , name="causes-view") ,
    path("cause/<str:slug>/" , single_cause , name="single-cause") ,

    path("page/" , page_view , name="page-view") ,
    path("volunteer/" , volunteer_view , name="volunteer") ,
    path("contact/" , contact_view , name="contact") ,
    
    path("blogs/" , blogs_view , name="blogs-view") ,
    path("<str:slug>/" , single_blogs , name="single-blog") ,
]