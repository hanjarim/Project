from django.db import models

class Regions(models.Model):
    name =  models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = "regions"
        verbose_name = "Region"
        verbose_name_plural = "Regions"

    def __str__(self):
        return self.name


class Locations(models.Model):
    regionID = models.ForeignKey(Regions, on_delete=models.CASCADE)
    name =  models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "locations"
        verbose_name = "Location"
        verbose_name_plural = "Locations"

    def __str__(self):
        return self.name


class Complaints(models.Model):
    CATEGORY = (
        ('VOICE', 'VOICE'),
        ('DATA', 'DATA'),
    )
    details = models.CharField(max_length=150)
    category = models.CharField(choices=CATEGORY, blank=False, default='VOICE', max_length=100)
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    landmark = models.CharField(max_length=100)
    coordinates = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=100)
    status = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "complaints"
        verbose_name = "Complaint"
        verbose_name_plural = "Complaints"

    def __str__(self):
        return self.details



