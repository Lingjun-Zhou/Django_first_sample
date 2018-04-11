from django.shortcuts import render
#业务处理逻辑都在views.py文件里。
# Create your views here.
from django.shortcuts import HttpResponse

from cmdb import  models

#user_list = [
#    {"user":"jack","pwd":"abc"},
#    {"user":"tom","pwd":"ABC"},
#]

#request参数必须有，名字是类似self的默认规则，可以改。它封装了用户请求的所有内容
def index(request):
    # request.POST
    # request.GET
    #return HttpResponse("Hello world")
    if request.method=="POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        #添加到数据库
        models.UserInfo.objects.create(user=username,pwd = password)
        #temp = {"user":username,"pwd":password}
        #user_list.append(temp)
        #print(username,password)
    #从数据库中读取所有数据
    user_list = models.UserInfo.objects.all()
    return render(request,"index.html",{"data":user_list})
#通过上面两个步骤，我们将index这个url指向了views里的index（）函数，它接收用户请求，并返回一个“hello world”字符串。