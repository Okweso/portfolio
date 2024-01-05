from django.contrib import admin
from .models import my_details, Project, Icon, Doc

class my_detailsAdmin(admin.ModelAdmin):
    list_display = ("greeting1", "greeting2", "my_name", "my_image")

class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "photo", "describe")

# Register your models here.
admin.site.register(my_details, my_detailsAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Icon)
admin.site.register(Doc)