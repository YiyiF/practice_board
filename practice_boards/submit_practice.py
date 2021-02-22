from django.shortcuts import render
from django.views.decorators import csrf


# 接收POST请求数据
def practice_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "practice_upload.html", ctx)
