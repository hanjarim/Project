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
            print(instance.complaint.id)
            complaint_obj = Complaints.objects.get(id=instance.complaint.id)
            complaint_obj.status = "PENDING"
            complaint_obj.save()
       
    except Exception as e:
        print(f"An exception occured {str(e)}")