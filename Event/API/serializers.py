from rest_framework import serializers
from .models import *
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
   class Meta:
     model=contest 
     fields=['id','name','co_ord','coord','domain','team_size','price','entry_price','participent','domain','start','end']

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
    

    






















class HeadItemSerializer(serializers.ModelSerializer):
    model=head_cordinator
    head=UserSerializer
    request=ApprovalSerializer
    fields=['id','head','request']
