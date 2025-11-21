from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import (
    Settings, Values, Image, Direction, DirectionImage,
    PartnerImage, Reviews, Blog, Feedback, Services, Statistic
)
from .serializers import (
    SettingsSerializer, ValuesSerializer, ImageSerializer, DirectionSerializer,
    DirectionImageSerializer, PartnerImageSerializer, ReviewsSerializer,
    BlogSerializer, FeedbackSerializer, ServicesSerializers, StatisticSerializers
)

class SettingsViewSet(viewsets.ModelViewSet):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ServiseAPI(viewsets.GenericViewSet,
                mixins.ListModelMixin ):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializers

class ValuesViewSet(viewsets.ModelViewSet):
    queryset = Values.objects.all()
    serializer_class = ValuesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class DirectionViewSet(viewsets.ModelViewSet):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class DirectionImageViewSet(viewsets.ModelViewSet):
    queryset = DirectionImage.objects.all()
    serializer_class = DirectionImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class PartnerImageViewSet(viewsets.ModelViewSet):
    queryset = PartnerImage.objects.all()
    serializer_class = PartnerImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

class StatisticViewSet(viewsets.GenericViewSet,
                       mixins.ListModelMixin):
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializers