from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from .models import Report, Seller, Brand, ReportType
from .serializers import (
    ReportSerializer,
    SellerSerializer,
    BrandSerializer,
    ReportTypeSerializer
)


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date', 'seller', 'brand', 'report_type']

    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned purchases to a given user,
    #     by filtering against a `username` query parameter in the URL.
    #     """
    #     queryset = Report.objects.all()
    #     seller_param = self.request.query_params.get('seller')
    #     if seller_param is not None:
    #         queryset = queryset.filter(seller=seller_param)
    #     return queryset

    # class ReportList(generics.ListAPIView):
    #     queryset = Report.objects.all()
    #     serializer_class = ReportSerializer
    #     filter_backends = [DjangoFilterBackend]
    #     filterset_fields = ['date', 'seller', 'brand', 'report_type']


class SellerCreateListViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer 


class BrandCreateListViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer 


class ReportTypeCreateListViewSet(viewsets.ModelViewSet):
    queryset = ReportType.objects.all()
    serializer_class = ReportTypeSerializer
