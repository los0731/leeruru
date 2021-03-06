from django.shortcuts import render
import os
import random

# Create your views here.
# ↓↓↓ 추가

# 로컬을 위한 경로.
imgs_path = '/Users/frank.io/Documents/workplace/django_4th/app_photos/static/imgs'
# pythonanywhere용 절대 경로.
imgs_path = '/home/leeruru/leeruru/app_photos/static/imgs'

list_imgs_src = []
list_imgs = os.listdir(imgs_path)


for idx, val in enumerate(list_imgs):
    tag = '/static/imgs/{}'.format(val)
    list_imgs_src.append(tag)

random.shuffle(list_imgs_src)

page_1 = list_imgs_src[0:199]
page_2 = list_imgs_src[200:399]
page_3 = list_imgs_src[400:599]
page_4 = list_imgs_src[600:799]
page_5 = list_imgs_src[800:999]
page_6 = list_imgs_src[1000:1199]
page_7 = list_imgs_src[1200:1399]
page_8 = list_imgs_src[1400:]

data = {
    'list_imgs_src': list_imgs_src,
    'page_1': page_1,
    'page_2': page_2,
    'page_3': page_3,
    'page_4': page_4,
    'page_5': page_5,
    'page_6': page_6,
    'page_7': page_7,
    'page_8': page_8,
}


def photos_album(request):
    return render(request, 'app_photos/index.html', data)


def page_1(request):
    return render(request, 'app_photos/index.html', data)


def page_2(request):
    return render(request, 'app_photos/2.html', data)


def page_3(request):
    return render(request, 'app_photos/3.html', data)


def page_4(request):
    return render(request, 'app_photos/4.html', data)


def page_5(request):
    return render(request, 'app_photos/5.html', data)


def page_6(request):
    return render(request, 'app_photos/6.html', data)


def page_7(request):
    return render(request, 'app_photos/7.html', data)


def page_8(request):
    return render(request, 'app_photos/8.html', data)


def page_memories(request):
    return render(request, 'app_photos/memories.html', data)
