from rest_framework import serializers
from .models import *
from time import timezone
from datetime import datetime
class DomainSerializer(serializers.ModelSerializer):
   class Meta: 
     model=Domain
     fields='__all__'
class UserSerializer(serializers.ModelSerializer):
   class Meta:
     model=User
     fields=['id','username','email']

class CoOrdSerializer(serializers.ModelSerializer):
    organizer=UserSerializer(read_only=True)
    class Meta:
      model=co_ordinator
      fields=['id','organizer','is_approved']

class ContestItemSerializer(serializers.ModelSerializer):
   coord=CoOrdSerializer(read_only=True)
   domain=DomainSerializer(read_only=True)
   participent=UserSerializer(many=True,read_only=True)

   start=serializers.DateTimeField(read_only=True)
   class Meta:
     model=contest 
     fields=['id','name','coord','team_size','price','entry_price','participent','domain','duration_in_hrs','start']
class ApprovalSerializer(serializers.ModelSerializer):
  by=UserSerializer(many=True,read_only=True)
  event=ContestItemSerializer(read_only=True)
  class Meta:
    model=Approval 
    fields=['id','requestfor','commnets','by','event']

class VenueSerializers(serializers.ModelSerializer):
  class Meta:
    model=venue
    fields=['location','max_capacity','is_available','next_avaiability']

class HeadSerializer(serializers.ModelSerializer):
  head=UserSerializer(read_only=True)
  request=ApprovalSerializer(read_only=True,many=True)
  class Meta:
    model=head_cordinator
    fields=['id','head','request']
 
class ProfileSerializer(serializers.ModelSerializer):
  user=UserSerializer(read_only=True)
  class Meta:
    model=Profile
    fields=['id','user','bio']
    

class EventforUserSerializer(serializers.ModelSerializer):
   coord=CoOrdSerializer(read_only=True)
   domain=DomainSerializer(read_only=True)
   team_size=serializers.IntegerField(min_value=1)
   start=serializers.DateTimeField()
   def validate(self, attrs):
     d1=attrs['start']
     if d1.date()>datetime.now():
       raise serializers.ValidationError
   class Meta:
     model=contest 
     fields='__all__'
     '''['id','name','coord','domain','team_size','price','entry_price','start']'''

class ProfileUserSerializer(serializers.ModelSerializer):
  user=UserSerializer(read_only=True)
  contests=ContestItemSerializer(read_only=True)
  class Meta:
     model=UserProfile
     fields=['user','bio','contests']

class HeadItemSerializer(serializers.ModelSerializer):
    model=head_cordinator
    head=UserSerializer
    class Meta:
     request=ApprovalSerializer
     fields=['id','head','request']
