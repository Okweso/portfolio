from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.home, name="home"),
    path("home/<name>", views.Paul, name="Paul"),
    path("about/", views.about, name="about"),
    path("project/", views.project, name="project"),
    path("contact/", views.contact, name="contact"),
    path("Paul/", views.Paul, name="Paul"),
    #path("uploads/", views.home, name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
