from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.Home),
    path("add/",views.Add),
    path("edit/<int:id>",views.Edit),
    path("delete/<int:id>",views.delete)

]
