from django.urls import path

from .views import GetCreateJournal, UpdateJournal, GetMonthlyJournal, DeleteJournal, GetJournalRatings

urlpatterns = [
    path('create/', GetCreateJournal.as_view()),
    path('all_journals/', GetCreateJournal.as_view()),
    path('<int:pk>/update/', UpdateJournal.as_view()),
    path('<int:pk>/delete/', DeleteJournal.as_view()),
    path('total/<int:month>/', GetMonthlyJournal.as_view()),
    path('ratings/<int:month>/', GetJournalRatings.as_view()),
]