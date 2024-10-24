from django.shortcuts import render
from app1.models import Book,Author
# Create your views here.
def home(request):
    result=Book.objects.all()
    return render(request,'index.html',{'books':result})
def createauthor(request):
    if request.method=="POST":
        name=request.POST.get('author')
        age=request.POST.get('age')
        rating=request.POST.get('rating')
        obj=Author(name=name,age=age,rating=rating)
        obj.save()
    return render(request,'author.html')
def createbook(request):
    if request.method=="POST":
        t=request.POST.get('title')
        p=request.POST.get('price')
        g=request.POST.get('Genre')
        s=request.POST.get('sno')
        if Author.objects.filter(id=s).exists():
            a=Author.objects.get(id=s)
            obj=Book(title=t,price=p,genre=g,author=a)
            obj.save()
    return render(request,'book.html')