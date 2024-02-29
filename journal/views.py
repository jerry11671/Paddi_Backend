from django.shortcuts import render

from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import permissions

from .serializers import JournalSerializer
from .models import Journal
from .utils import get_days_in_month
from datetime import datetime
from django.db.models import Count


class GetCreateJournal(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        journal_qs = Journal.objects.filter(journal_user=self.request.user.id)
        serializer = JournalSerializer(journal_qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        request.data['journal_user'] = self.request.user.id
        if request.data['feeling'] == 'overjoyed' or request.data['feeling'] == 'happy' or request.data['feeling'] == 'neutral':
            request.data['rating'] = 'positive'
        else:
            request.data['rating'] = 'negative'
        serializer = JournalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateJournal(GenericAPIView):
    def put(self, request, pk):
        user_obj = self.request.user.id
        data = request.data
        data['journal_user'] = user_obj
        qs = Journal.objects.get(pk=pk, journal_user=user_obj)
        serializer =JournalSerializer(qs, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DeleteJournal(GenericAPIView):
    def delete(self, request, pk):
        user_obj = self.request.user.id
        qs = Journal.objects.filter(journal_user=user_obj, pk=pk)
        qs.delete()
        return Response("Journal Deleted", status=status.HTTP_204_NO_CONTENT)  


  
class GetMonthlyJournal(GenericAPIView):
    def get(self, request, month):
        try:
            month=int(month)
        except ValueError:
            return Response({'error': 'Invalid Month!!'})
        
        if month > 12:
            return Response("This is not a valid month!!")
        
        user_obj = self.request.user.id
        monthly_journals = Journal.objects.filter(journal_user=user_obj, created_at__month=month)


        serializer = JournalSerializer(monthly_journals, many=True)
        total_journals = monthly_journals.count()

        return Response({'data': serializer.data,
            'Total_Journal': total_journals}, status=status.HTTP_200_OK)



class GetJournalRatings(GenericAPIView):
    def get(self, request, month):
        journal_user = self.request.user.id
        journals = Journal.objects.filter(journal_user=journal_user, created_at__month=month).annotate(day=Count('created_at__day')).values('day', 'journal_rating')

        # To organize the data by day
        for journal in journals:
            journal_ratings = {}
            day = journal['day']
            rating = journal['journal_rating']
            journal_ratings.setdefault(day, []).append(rating)

        return Response(journal_ratings)
            









    
        
        
            
