from django.contrib import admin
from complaintapp.models import (
    Complaints,
    Locations,
    Regions,
    Tasks,
    TaskActions,
    User
)

admin.site.register(Regions)
admin.site.register(Locations)
admin.site.register(Complaints)
admin.site.register(Tasks)
admin.site.register(TaskActions)
admin.site.register(User)