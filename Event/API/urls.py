from django.urls import path,include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns=[
             path('contest-list',views.ContestViewSet.as_view()),
             path('contest-list/<int:pk>',views.ContestList.as_view()),
             
             path('contest-lists',views.contestForUser),
             path('contest',views.ContestCreate.as_view()),
             
             path('domain-list',views.DomainViewSet.as_view()),
             path('domain-list/<int:pk>',views.DomainList.as_view()),

             path('domain-contest/<int:pk>',views.DOMAIN_CONTEST),

             path('profile-list',views.ProfileViewSet.as_view()),
             path('profile-user/<int:pk>',views.Profile_list),
             
             path('head-list',views.HeadViewSet.as_view()),
             path('head-list/<int:pk>',views.HEADList.as_view()),

             path('co-ordlist',views.CoordViewSet.as_view()),
             path('co-ord/<int:pk>',views.CoordList.as_view()),
             
             #participents in overall events 
             path('user',views.paticipentsList.as_view()),
             path('user/<int:pk>',views.paticipentList.as_view()),
             path('Profile',views.contestent),
    

             path('api-token-auth/',obtain_auth_token),
             ]
