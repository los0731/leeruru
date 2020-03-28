from django.shortcuts import render

# Create your views here.
# ↓↓↓ 추가
say_hi = "안녕 하하핳?"
my_name = "내 이름은 부랑구야."
data = {
    'say_hi': say_hi,
    'my_name': my_name
}


def photos_album(request):
    return render(request, 'app_photos/index.html', data)
