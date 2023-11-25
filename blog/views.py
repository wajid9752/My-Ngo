from django.shortcuts import render
from .models import *
from .forms import ContactForm,VolunteerForm
from django.http import HttpResponse , JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    
    categories = ['Clean Water', 'Healthy Food', 'Medical Help']
    category_queryset = blog_category.objects.filter(category__in=categories)
    blogs=blog.objects.all()[:3]
    news_blog=blog.objects.filter(category__category = "News")
    events=Event.objects.all()
   
    return render(request , "main/home.html", locals())

#################### CAUSE VIEW ################

def causes_view(request):
    blogs=blog.objects.filter(category__category="causes")
    categorys=blog_category.objects.all()
    return render(request , "cause/causes.html",locals())

def single_cause(request,slug):
    obj=blog.objects.get(slug=slug)
    categorys=blog_category.objects.all()
    return render(request , "cause/single-cause.html",locals())

################# ABOUT US #######################

def about_us(request):
    return render(request , "main/about-us.html")

########################### BLOGS ####################



def blogs_view(request):
    blogs = blog.objects.all().exclude(category__category="causes")
    categorys = blog_category.objects.all()
    blogs_per_page = 3  
    page = request.GET.get('page', 1)
    paginator = Paginator(blogs, blogs_per_page)
    
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    return render(request, "blog/blogs-view.html", {'blogs': blogs, 'categorys': categorys})



def single_blogs(request,slug):
    obj=blog.objects.get(slug=slug)
    categorys=blog_category.objects.all()
    return render(request , "blog/single-blog.html",locals())



##################### EVENT ############################
def single_event(request,pk):
    event=Event.objects.get(id=pk)
    categorys=blog_category.objects.all()
    return render(request , "main/event-detail.html",locals())



def page_view(request):
    return render(request , "main/home.html")


def volunteer_view(request):
    if request.POST:
        form = VolunteerForm(request.POST)
        if form.is_valid():
            getName = form.cleaned_data['name']
            form.save()
            return JsonResponse({'status': 'success', 'message': f'Form submitted successfully {getName}. Will catch you soon '})
        else:
            return JsonResponse({'status': 'error', 'message': str(form.errors)})

    return render(request , "main/volunteer.html")

def contact_view(request):
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            getName = form.cleaned_data['name']
            form.save()
            return JsonResponse({'status': 'success', 'message': f'Form submitted successfully {getName}. Will catch you soon '})
        else:
            return JsonResponse({'status': 'error', 'message': str(form.errors)})

    form = ContactForm()
    return render(request, "main/contact.html", {'form': form})





