from rest_framework import serializers

class CourseListSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    is_popular = serializers.BooleanField()
    is_trending = serializers.BooleanField()
    description = serializers.CharField()
    image = serializers.ImageField()
    price = serializers.DecimalField(max_digits=10,decimal_places=3)
    
