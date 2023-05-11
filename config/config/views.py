from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article
import random

def home_view(request):
    random_int = random.randint(1, 3)
    article_obj = Article.objects.get(id=random_int)
    article_queryset = Article.objects.all()
    context = {
        "object_list": article_queryset,
        "title": article_obj.title,
        "content": article_obj.content,
        "id": article_obj.id
    }

    HTML_STRING = render_to_string("home_view.html", context=context)   
    return HttpResponse(HTML_STRING)