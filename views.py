from django.shortcuts import render
from django.http import HttpResponse
from HelloWORLD.models import Test


# hello_world打印
def hello(request):
    # return HttpResponse("Hello world !")
    context = {'hello': 'Hello World!'}
    return render(request, 'HelloWORLD/hello.html', context)


# 操纵数据库
def testdb(request):
    test1 = Test(name='w3cschool.cn')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")
