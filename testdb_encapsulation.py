# 该模块是对django函数的一种封装，旨在提供更为高级的数据处理功能
from django.http import HttpResponse
from .models import Test

# 函数：网数据库添加字段
# 函数参数就是字段名称，这样容易一一对应
# 这里就一个字段 name
def add_test(request, name):
    test = Test(name=name)
    test.save()
    return HttpResponse("<p>数据添加成功！</p>")


# 删除单个数据
def delete_test(request):
    # 方式一
    test1 = Test.objects.get(id=1)
    test1.delete()
    return HttpResponse("<p>删除成功</p>")

    '''
    # 方式二
    Test.objects.filter(id=1).delete()
    return HttpResponse("<p>删除成功</p>")
    '''


# 删除所有数据
def deleteall_test(request):
    Test.objects.all().delete()
    return HttpResponse("<p>全部删除成功</p>")


# 根据id，更新数据
def update_test(request, id):
    test = Test.objects.get(id=id)
    test.name = 'w3cschoolW3Cschool教程'
    test.save()
    return HttpResponse("<p>修改成功</p>")

    '''
    # 更新的另一种方式
    Test.objects.filter(id=1).update(name='w3cschoolW3Cschool教程')
    return HttpResponse("<p>修改成功</p>")
    '''


# 更新某一字段的所有数据
def updateall_test(request):
    Test.objects.all().update(name='w3cschoolW3Cschool教程')
    return HttpResponse("<p>修改成功</p>")


# 查询函数
def find_test(reuqest):
    pass
