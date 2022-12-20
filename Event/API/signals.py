from .models import User,Profile,head_cordinator,co_ordinator
from django.db.models.signals import post_delete,post_save
from django.dispatch import receiver
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
'''
@receiver(post_save,sender=head_cordinator)
def create_head(sender,instance,created,**kwargs):
    if created:
        head_cordinator.objects.create(head=instance)

'''
