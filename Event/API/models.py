from django.db import models
from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_delete,post_save
from django.dispatch import receiver
from django.db.models import signals
from time import timezone
class co_ordinator(models.Model):
    organizer=models.OneToOneField(User,related_name='organizer',on_delete=models.CASCADE)
    is_approved=models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.organizer.username
     
class Profile(models.Model):
    user=models.OneToOneField(User,related_name='user',on_delete=models.CASCADE)
    bio=models.TextField(max_length=150,default="HII iam a cocordinator ")
    def __str__(self) -> str:
        return self.user.username 

class Domain(models.Model):
    domain_name=models.CharField(max_length=30)  
    def __str__(self) -> str:
        return self.domain_name

class venue(models.Model):
    location=models.CharField(max_length=50)
    max_capacity=models.IntegerField()
    is_available=models.BooleanField(default=True)
    next_avaiability=models.DateTimeField(auto_now_add=True)

class contest(models.Model):
    name=models.CharField(max_length=30)
    co_ord=models.ForeignKey(co_ordinator,related_name="co_ordinator",on_delete=models.CASCADE,null=True)
    contest_description=models.TextField(max_length=200)
    team_size=models.IntegerField()
    price=models.IntegerField()
    entry_price=models.IntegerField()
    participent=models.ManyToManyField(User,related_name="participent")
    domain=models.ForeignKey(Domain,related_name="Domain",on_delete=models.CASCADE,null=True)
    start=models.DateTimeField(auto_now_add=True )
    duration_in_hrs=models.FloatField()
    location=models.ForeignKey(venue,related_name="Venue",null=True,on_delete=models.SET_NULL)
    def __str__(self) -> str:
        return self.name

class Approval(models.Model):
    request_modulues=(('event approval','EVENT approval'),('co-cordiantor authorization','authentication'))
    by=models.ManyToManyField(co_ordinator,related_name='requester')
    requestfor=models.CharField(choices=request_modulues,max_length=30,default='EVENT approval')
    commnets=models.CharField(max_length=150,default="",null=True)
    event=models.ForeignKey(contest,on_delete=models.CASCADE,null=True)

class head_cordinator(models.Model):
    head=models.OneToOneField(User,related_name='head_organizer',on_delete=models.CASCADE)
    requests=models.ManyToManyField(Approval,blank=True,related_name="requests")
    def __str__(self) -> str:
        return self.head.username
    
class Expro(models.Model):
    DOMAIN=models.ManyToManyField(Domain,related_name='DOMAIN',blank=True)

class UserProfile(models.Model):
    user=models.OneToOneField(User,related_name='userProfile',on_delete=models.CASCADE)
    bio=models.TextField(max_length=150,default="hey lets start my EVENT HUNT")
    contest=models.ManyToManyField(contest,related_name='user',blank=True)
    def __str__(self) -> str:
        return self.user.username
