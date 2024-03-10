from django.shortcuts import render, get_object_or_404
from .models import News
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import News
from .filters import NewsFilter

from .templatetags import custom_filters
def search_news(request):
    news_list = News.objects.all()
    news_filter = NewsFilter(request.GET, queryset=news_list)

    return render(request, 'news/search_news.html', {'filter': news_filter})
def news_list(request):
    news = News.objects.all().order_by('-publication_date')
    return render(request, 'news/news_list.html', {'news': news})

def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    return render(request, 'news/news_detail.html', {'news_item': news_item})

# дополнения от задания  D7.7. Итоговый проект
def news_list(request):
    news_list = News.objects.all()
    paginator = Paginator(news_list, 10)  # Показывать по 10 новостей на странице

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news/news_list.html', {'page_obj': page_obj})