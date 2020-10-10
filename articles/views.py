from django.shortcuts import render, redirect
from .models import Article,Contact
from django.contrib import messages
def home(request):
    articles  = Article.objects.all().order_by('date')
    return render (request, 'articles/article_list.html', {'articles':articles})
def about(request):
    return render(request, 'about.html')
def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        sub = request.POST['sub']
        message = request.POST['message']
        ins = Contact(name=name, email=email, phone=phone, sub=sub, message=message)
        ins.save()
        messages.success(request, f'Thanks. We Receive Your Message SUCCESSFULLY. You\'ll reply soon.')
        return redirect('contact')
    return render(request, 'contact.html',)
def article_details(request, slug):
    article = Article.objects.filter(slug=slug).first()
    context = {'article':article}
    return render (request, 'articles/article_details.html', context)
