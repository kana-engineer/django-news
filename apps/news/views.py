from django.shortcuts import render, redirect, get_object_or_404
from .models import Newss

# Create your views here.
def news(request):
    news = Newss.objects.all().order_by('-created_ad')
    return render(request, 'news/news.html', {'news': news})

def add_news(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        text = request.POST.get("text")
        Newss.objects.create(title=title, text=text)
        return redirect('news')
    return render(request, 'news/add_news.html')

def delete_news(request, id=id):
    news = get_object_or_404(Newss, id=id)
    if request.method == 'POST':
        news.delete()
        return redirect('news')
    return redirect('news')
