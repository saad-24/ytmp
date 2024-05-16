from django.shortcuts import render
import requests
import json
from django.http import JsonResponse
from .models import *
# Create your views here.


def home(request):
    header = Logo.objects.first()
    trending_songs = Trending.objects.all()
    horizontal_adsense = Horizontal_Adsense.objects.first()
    vertical_adsense = Vertical_Adsense.objects.first()
    return render(request, 'home.html', {'header':header, 'trending_songs':trending_songs, 'horizontal_adsense':horizontal_adsense, 'vertical_adsense':vertical_adsense})


def converter(request):
    if request.method == 'POST' or request.method == 'GET':
        if request.method == 'POST':
            video_url = request.POST.get('url')
        elif request.method == 'GET':
            video_url = request.GET.get('url')

        if video_url:
            url = "https://youtube-mp3-downloader2.p.rapidapi.com/ytmp3/ytmp3/"

            querystring = {"url": video_url}

            headers = {
                "X-RapidAPI-Key": "179ba634e1msh1a4493c700cd480p175adfjsne064125f1d62",
                "X-RapidAPI-Host": "youtube-mp3-downloader2.p.rapidapi.com"
            }

            response = requests.get(url, headers=headers, params=querystring)
            data = response.json()

            if response.status_code == 200:
                download_link = data.get('dlink')
                return JsonResponse({'success': True, 'download_link': download_link})
            else:
                return JsonResponse({'success': False, 'error': 'Failed to convert the video.'})
        else:
            return JsonResponse({'success': False, 'error': 'No URL provided.'})

    return JsonResponse({'error': 'Unsupported method.'}, status=405)

# def blogs(request):
#     header = Logo.objects.first()
#     trending_songs = Trending.objects.all()
#     horizontal_adsense = Horizontal_Adsense.objects.first()
#     vertical_adsense = Vertical_Adsense.objects.first()
#     return render(request, 'blogs.html', {'header':header, 'trending_songs':trending_songs, 'horizontal_adsense':horizontal_adsense, 'vertical_adsense':vertical_adsense})

def contact(request):
    header = Logo.objects.first()
    trending_songs = Trending.objects.all()
    horizontal_adsense = Horizontal_Adsense.objects.first()
    vertical_adsense = Vertical_Adsense.objects.first()
    return render(request, 'contact.html', {'header':header, 'trending_songs':trending_songs, 'horizontal_adsense':horizontal_adsense, 'vertical_adsense':vertical_adsense})

def privacy(request):
    header = Logo.objects.first()
    trending_songs = Trending.objects.all()
    horizontal_adsense = Horizontal_Adsense.objects.first()
    vertical_adsense = Vertical_Adsense.objects.first()
    privacy = Privacy.objects.first()
    return render(request, 'privacy.html', {'header':header, 'trending_songs':trending_songs, 'horizontal_adsense':horizontal_adsense, 'vertical_adsense':vertical_adsense, 'privacy':privacy})

def terms(request):
    header = Logo.objects.first()
    trending_songs = Trending.objects.all()
    horizontal_adsense = Horizontal_Adsense.objects.first()
    vertical_adsense = Vertical_Adsense.objects.first()
    terms = Terms.objects.first()
    return render(request, 'terms.html', {'header':header, 'trending_songs':trending_songs, 'horizontal_adsense':horizontal_adsense, 'vertical_adsense':vertical_adsense, 'terms':terms})

def blogs(request):
    header = Logo.objects.first()
    trending_songs = Trending.objects.all()
    horizontal_adsense = Horizontal_Adsense.objects.first()
    vertical_adsense = Vertical_Adsense.objects.first()
    blogs = Blogs.objects.all()
    return render(request, 'blogs.html', {'header':header, 'trending_songs':trending_songs, 'horizontal_adsense':horizontal_adsense, 'vertical_adsense':vertical_adsense, 'blogs':blogs})

def blog_detail(request, blog_id):
    header = Logo.objects.first()
    trending_songs = Trending.objects.all()
    horizontal_adsense = Horizontal_Adsense.objects.first()
    vertical_adsense = Vertical_Adsense.objects.first()
    blog = Blogs.objects.get(id=blog_id)
    # Your view logic here
    # return render(request, 'blog_single.html', {'blog': blog})
    return render(request, 'blog_single.html', {'header':header, 'trending_songs':trending_songs, 'horizontal_adsense':horizontal_adsense, 'vertical_adsense':vertical_adsense, 'blog':blog})