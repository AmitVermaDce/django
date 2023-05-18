from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Article
from articles.forms import ArticleForm
from django.http import Http404

# Create your views here.

def article_search_view(request):
    query_dict = request.GET
    try:
        query = int(query_dict.get("query"))
    except:
        query = None
    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context = {
        "object": article_obj
    }
    return render(request, "articles/search.html", context=context)


def article_detail_view(request, slug=None):
    article_obj = None
    if slug is not None:
        article_obj = Article.objects.get(slug=slug)
        try:
            article_obj = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            raise Http404
        except:
            raise Http404
    context = {
        "object": article_obj
    }
    return render(request, "articles/detail.html", context=context)



@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        'form': form
    }

    if form.is_valid():
        article_obj = form.save()
        context['form'] = ArticleForm()
    return render(request, 'articles/create.html', context)

