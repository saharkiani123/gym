from django.urls import path
from .views import *



app_name = "stadium"

urlpatterns = [

    path('createstudiumset', StudiumSetView.as_view()),
    path('getstudiumset', ListStudiumSetView.as_view()),
    path('getstudiumset/<str:id>', GetOneStudiumSetView.as_view()),
    path('weeklyreservationView', WeeklyReservationView.as_view()),
    path('possibilitiesetview', PossibilitieSetView.as_view()),
    path('sportfieldview', SportFieldView.as_view()),
    path('classtimeview', ClassTimeView.as_view()),
    path('studiumsetpossibilitiefilter', StudiumSetPossibilitieFilter.as_view()),
    path('studiumsetsportsfieldsilter', StudiumSetSportFieldFilter.as_view()),
    path('studiumsetstatefilter', StudiumSetstateFilter.as_view()),
    path('rating', Rating.as_view()),
    path('photos', PhotoListCreateAPIView.as_view()),
    # path('photos', PhotoListCreateAPIView.as_view()),
    
]