from django.shortcuts import render
from django.http import HttpResponse
from .models import post, postImage, category

# created views
def indexPageView(request) : 
    return render(request, 'portfolio/index.html')

def aboutPageView(request) : 
    return render(request, 'portfolio/about.html')

def portfolioView(request) : 

    data = post.objects.all()
    pics = postImage.objects.all()
    categories = category.objects.all()
    
    breadPosts = data.filter(category="Bread")
    breadPics = pics.filter(myPost__in=breadPosts)[:3]

    savPosts = data.filter(category="Savory Meals")
    savPics = pics.filter(myPost__in=savPosts)[:3]

    dessertPosts = data.filter(category="Desserts")
    dessertPics = pics.filter(myPost__in=dessertPosts)[:3]

    context = {
        "posts" : data,
        "images" : pics,
        "category" : categories,
        "breadPics" : breadPics,
        "savPics" : savPics,
        "dessertPics" : dessertPics
    }

    return render(request, 'portfolio/portfolio.html', context)

def displayPageView(request, portItem) :
     
    data = post.objects.all()
    pics = postImage.objects.all()
    categories = category.objects.all()
    
    context = {
        "portItem" : portItem,
        "posts" : data,
        "images" : pics,
        "category" : categories
    }

    return render(request, 'portfolio/display.html', context)

def contactPageView(request) :
    
    return render(request, 'portfolio/contact.html')