from django.db.models.signals import post_save
from django.dispatch import receiver
from complaintapp.models import (
    Complaints,
    Tasks
)

@receiver(post_save, sender=Tasks)
def post_save_update_status(sender, instance, created, *args, **kwargs):
    try:
        if created:
            Complaints.objects.update(pk=instance.complaint.id).update(status="PENDING")
       
    except Exception as e:
        print(f"An exception occured {str(e)}")