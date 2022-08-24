from django.contrib import admin
from complaintapp.models import (
    Regions,
    Locations,
    Complaints,
    User
)

admin.site.register(Regions)
admin.site.register(Locations)
admin.site.register(Complaints)
admin.site.register(User)