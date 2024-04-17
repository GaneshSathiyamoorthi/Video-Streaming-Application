from rest_framework import serializers
from videoapp.models import Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'name', 'description', 'url', 'user', 'created_at']
