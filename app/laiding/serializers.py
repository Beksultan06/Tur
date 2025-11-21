# serializers.py
from rest_framework import serializers
from .models import (
    Settings, Values, Image, Direction, DirectionImage,
    PartnerImage, Reviews, Blog, Feedback, Services, Statistic
)

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = [
            "id",
            "logo",
            "title",
            "description",
            "image_back",
            "title_about",
            "text1",
            "text2",
            "image_about",
            "logo_about",
            "image_about_blok",
            "image_about_blok2",
            "description_about",
            "description_about2",
            "values",
            "title_missions",
            "description_missions",
            "title_directions",
            "title_development",
            "description_development",
            "title_parrners",
            'description_parrners',
            "title_reviews",
            "title_blog",
            "description_blog",
            "title_end",
            "image_end",
            "title_feedback",
            "description_feedback",
            "title_contact",
            "phone_number",
            "email",
            "address",
            "text",
            "end_text",
            'inta',
            'watchap',
            'telegram',
            'title_statistic'
        ]

class ValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Values
        fields = ["id", "title", "image"]


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["id", "image"]


class DirectionImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectionImage
        fields = ["id", "direction", "image"]



class DirectionSerializer(serializers.ModelSerializer):
    direction_images = DirectionImageSerializer(
        source="direction", 
        many=True,
        read_only=True
    )

    class Meta:
        model = Direction
        fields = ["id", "title", "description", "direction_images"]


class PartnerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerImage
        fields = ["id", "image"]


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ["id", "name", "date", "description", "star"]


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["id", "title", "description"]


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ["id", "name", "email", "phone", "message"]

class ServicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['id', 'title', 'description']
        

class StatisticSerializers(serializers.ModelSerializer):
    class Meta:
        model = Statistic  
        fields = ['id', 'types', 'statistic']