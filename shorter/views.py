from shorter.models import Url, Visit
from shorter.serializers import UrlSerializer

from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, DestroyAPIView


class RedirectUrlView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        url = get_object_or_404(Url, short_id=kwargs['short_id'])
        Visit.objects.create(url=url, visitor_ip=self.request.META['REMOTE_ADDR'])
        return url.url


class UrlCreateAPIView(CreateAPIView):
    lookup_field = 'url'
    serializer_class = UrlSerializer


class UrlDeleteAPIView(DestroyAPIView):
    lookup_field = 'short_id'
    serializer_class = UrlSerializer

    def get_queryset(self, *args, **kwargs):
        return Url.objects.filter(creator_ip=self.request.META['REMOTE_ADDR'])


class IpStatsAPIView(APIView):

    def get(self, request):
        stats = []
        urls = Url.objects.filter(creator_ip=request.META['REMOTE_ADDR'])

        for url in urls:
            stats.append({
                'url': url.url,
                'short_id': url.short_id,
                'views': Visit.objects.filter(url=url).count()
            })

        return Response(stats)


class UrlStatsAPIView(APIView):

    def get(self, request, short_id):
        url = get_object_or_404(Url, short_id=short_id, creator_ip=request.META['REMOTE_ADDR'])
        visits = []

        for visit in Visit.objects.filter(url=url):
            visits.append({
                'visitor_ip': visit.visitor_ip,
                'visit_time': visit.visit_time
            })

        return Response(visits)
