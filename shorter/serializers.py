import uuid

from shorter.models import Url

from rest_framework import serializers
from rest_framework.generics import DestroyAPIView


class UrlSerializer(serializers.ModelSerializer, DestroyAPIView):

    class Meta:
        model = Url
        fields = ('url', 'short_id')
        read_only_fields = ('short_id', )

    def create(self, validated_data):
        return Url.objects.create(
            url=validated_data.get('url'),
            short_id=uuid.uuid4().hex.capitalize()[0:6],
            creator_ip=self.context['request'].META['REMOTE_ADDR']
        )
