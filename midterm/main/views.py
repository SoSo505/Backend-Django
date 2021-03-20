# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets, status, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from auth_.models import MainUser
from main.models import BookJournalBase, Book, Journal
from rest_framework.response import Response
from django.shortcuts import render



from main.serializers import BookJournalBaseSerializer, BookSerializer, JournalSerializer


class BookViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def book(self, request):
        books = BookJournalBase.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)





class JournalViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def journal(self, request):
        journals = Journal.objects.all()
        serializer = JournalSerializer(journals, many=True)
        return Response(serializer.data)


   
