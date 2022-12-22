from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import *
from  rest_framework.permissions import IsAdminUser,IsAuthenticated
from .serializers import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from .permission import IsCoordinator,IsHeadCoordinator
from django.contrib.auth.models import Group

#head co-ordinator user view 
class paticipentsList(generics.ListCreateAPIView):
    queryset=User.objects.filter(groups__name="user")
    serializer_class=UserSerializer
    permission_classes=[IsHeadCoordinator]
    def create(self, request, *args, **kwargs):
          serializers=UserSerializer(data=request.data)
          if serializers.is_valid():
            serializers.save()
            print(serializers.data)
            user=User.objects.get(username=request.data['username'])
            grp=Group.objects.get(name="user")
            grp.user_set.add(user)
            return Response(serializers.data,status=status.HTTP_201_CREATED) 
          return Response(status=status.HTTP_400_BAD_REQUEST) 

class paticipentList(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.filter(groups__name="user")
    serializer_class=UserSerializer
    permission_classes=[IsHeadCoordinator]

class ContestViewSet(generics.ListAPIView):
    queryset=contest.objects.all()
    serializer_class=ContestItemSerializer
    def list(self, request):
        queryset = self.get_queryset()
        serializer = ContestItemSerializer(queryset, many=True)
        return Response(serializer.data)
    def get_queryset(self):
        return contest.objects.all()
    
class ContestCreate(generics.CreateAPIView):
    queryset=contest.objects.all()
    serializer_class=ContestItemSerializer
    permission_classes=[IsHeadCoordinator]
    def create(self, request, *args, **kwargs):
       if request.user.groups.filter(name="Coordinator").exists():
          serializers=ContestItemSerializer(data=request.data)
          if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED) 
          return Response(status=status.HTTP_400_BAD_REQUEST) 
       return Response(status=status.HTTP_403_FORBIDDEN) 
class ContestList(generics.RetrieveUpdateDestroyAPIView):
    queryset=contest.objects.all()
    serializer_class=ContestItemSerializer
    permission_classes=[IsHeadCoordinator,IsCoordinator]
    
''' <<<<<                   domain CRUD                       >>>>>   '''
class DomainViewSet(generics.ListCreateAPIView):
    queryset=Domain.objects.all()
    serializer_class=DomainSerializer
    permission_classes=[(IsAuthenticated |IsCoordinator | IsHeadCoordinator)]
    def list(self, request):
        queryset = self.get_queryset()
        serializer = DomainSerializer(queryset, many=True)
        return Response(serializer.data)
        
    def get_queryset(self):
        return Domain.objects.all()
        
    def create(self, request, *args, **kwargs):
        if request.user.groups.filter(name="HEADCORDINATOR").exists():
         serializers=DomainSerializer(data=request.data)
         if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return super().create(request, *args, **kwargs)
        
        
class DomainList(generics.RetrieveUpdateDestroyAPIView):
    queryset=Domain.objects.all()
    serializer_class=DomainSerializer
    permission_classes=[IsHeadCoordinator]


''' <<<<<              Profile    CRUD                       >>>>>   '''
class ProfileViewSet(generics.ListCreateAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    permission_classes=[IsAuthenticated]
    def list(self, request):
        if request.user.groups.filter(name="HEADCORDINATOR").exists():
          queryset = self.get_queryset()
          serializer = ProfileSerializer(queryset, many=True)
          return Response(serializer.data)
        else:
          return Response({"message":"you are not authenticate to this operations"},status=status.HTTP_403_FORBIDDEN)
    def get_queryset(self):
        return Profile.objects.all()
    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)
        return super().perform_create(serializer)

@api_view(["GET","PUT","PATCH","DELETE"])
@permission_classes([IsAuthenticated])
def Profile_list(request,pk):
    try:
        profile=Profile.objects.get(id=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        serializer_item=ProfileSerializer(profile)
        return Response(serializer_item.data,status=status.HTTP_200_OK)
    if request.user.groups.filter(name="HEADCORDINATOR").exists():
        if request.method=="DELETE":
          profile.delete()
          return Response(status=status.HTTP_200_OK)
        return Profile_view(profile,request.method,request.data)      
    if request.user.groups.filter(name="Coordinator").exists():
        return Profile_view(profile,request.method,request.data)      
    return Response({"message":"you are not authenticate to this operations"},status=status.HTTP_403_FORBIDDEN)


''' <<<<<              head   CRUD                       >>>>>   '''
class HeadViewSet(generics.ListCreateAPIView):
    queryset=head_cordinator.objects.all()
    serializer_class=HeadSerializer
    permission_classes=[IsHeadCoordinator]
    def list(self, request):
        queryset = self.get_queryset()
        serializer = HeadSerializer(queryset,many=True)
        return Response(serializer.data)
    def get_queryset(self):
        return head_cordinator.objects.all()
    def create(self, request, *args, **kwargs):
          serializers=UserSerializer(data=request.data)
          if serializers.is_valid():
            serializers.save()
            print(serializers.data)
            user=User.objects.get(username=request.data['username'])
            grp=Group.objects.get(name="HEADCORDINATOR")
            grp.user_set.add(user)
            print(user)
            head_cordinator.objects.create(head=user)
            return Response(serializers.data,status=status.HTTP_201_CREATED) 
          return Response(status=status.HTTP_400_BAD_REQUEST)
    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)
        return super().perform_create(serializer)
        
class HEADList(generics.RetrieveUpdateDestroyAPIView):
    queryset=head_cordinator.objects.all()
    serializer_class=HeadSerializer
    permission_classes=[IsHeadCoordinator]


''' <<<<<             co-ordt   CRUD                       >>>>>   '''

class CoordViewSet(generics.ListCreateAPIView):
    queryset=co_ordinator.objects.all()
    serializer_class=CoOrdSerializer
    permission_classes=[IsHeadCoordinator]
    def list(self, request):
        queryset = self.get_queryset()
        serializer = CoOrdSerializer(queryset, many=True)
        return Response(serializer.data)
    def get_queryset(self):
        return co_ordinator.objects.all()
    def create(self, request, *args, **kwargs):
          serializers=UserSerializer(data=request.data)
          if serializers.is_valid():
            serializers.save()
            user=User.objects.get(username=request.data['username'])
            grp=Group.objects.get(name="Coordinator")
            grp.user_set.add(user)
            co_ordinator.objects.create(organizer=user)
            return Response(serializers.data,status=status.HTTP_201_CREATED) 
          return Response(status=status.HTTP_400_BAD_REQUEST)

class CoordList(generics.RetrieveUpdateDestroyAPIView):
    queryset=co_ordinator.objects.all()
    serializer_class=CoOrdSerializer
    permission_classes=[IsHeadCoordinator]

def Profile_view(profile,method,data):
       if method=="PUT":
           serializer_item=ProfileSerializer(profile,data=data)
           serializer_item.is_valid(raise_exception=True)
           serializer_item.save()
           return Response(serializer_item.data,status.HTTP_201_CREATED)
       elif method=="PATCH":
         serializer_item=ProfileSerializer(profile,partial=True,data=data)
         if serializer_item.is_valid():
            serializer_item.save()
            return Response(serializer_item.data,status=status.HTTP_201_CREATED)
       return Response({"message":"you are not authenticate to this operations"},status=status.HTTP_403_FORBIDDEN) 
    
'''profiler creating after the  user is created'''

class ContestForUser(generics.ListAPIView):
    queryset=contest.objects.all()
    serializer_class=EventforUserSerializer
    def list(self):
        queryset = self.get_queryset()
        serializer = EventforUserSerializer(queryset, many=True)
        return Response(serializer.data)
    def get_queryset(self):
        return contest.objects.all()



@api_view(["GET"])
@permission_classes([])
def contestForUser(request):
    queryset=contest.objects.all()
    serializer_item=EventforUserSerializer(queryset, many=True)
    return Response(serializer_item.data,status=status.HTTP_200_OK)