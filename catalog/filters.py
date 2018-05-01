import django_filters

from .models import Presentation


class PresentationFilter(django_filters.FilterSet):

    class Meta:
        model = Presentation
        fields = {
            'presentation_id': ['exact'],
            'title': ['contains'],
            'creator': ['contains'],
            }
