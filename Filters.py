# Страница /news/search для поиска новостей
import django_filters
from .models import News

class NewsFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author_name = django_filters.CharFilter(lookup_expr='icontains', field_name='author__name')  # предполагается что у вас есть связь с моделью Author через поле author
    published_date = django_filters.DateFilter(field_name='published_date', lookup_expr='gt', widget=django_filters.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = News
        fields = ['title', 'author_name', 'published_date']
