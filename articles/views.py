from django.shortcuts import render, HttpResponse
from .models import Article

def home(request):
    return render(request, 'index.html')



def about(request):
    return render(request, 'about.html')




def contact(request):
    return render(request, 'contact.html')


def article_list(request):
    articles  = Article.objects.all().order_by('date')
    return render (request, 'articles/article_list.html', {'articles':articles})


def article_details(request, slug):
    article = Article.objects.filter(slug=slug).first()
    context = {'article':article}
    return render (request, 'articles/article_details.html', context)


