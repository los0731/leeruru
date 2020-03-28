from django.shortcuts import render
import os
import random

# Create your views here.
# ↓↓↓ 추가
img_0 = "img_ruru_0.jpg"
my_name = "내 이름은 부랑구야."
list_imgs_src = []

current_path = os.getcwd()
imgs_path = 'app_photos/static/imgs'

list_imgs = os.listdir(imgs_path)
# # print(list_imgs)


for i in list_imgs:
    tag = '{}{}'.format('/static/imgs/', i)
    list_imgs_src.append(tag)
    print(tag)



data = {
    # 'list_img': list_imgs,
    'list_imgs_src': list_imgs_src,
    'img_0': img_0,
}


def photos_album(request):
    return render(request, 'app_photos/index.html', data)
