# mysite
first project for Django

源地址：https://blog.csdn.net/Sunshine_ZCC/article/details/73918408 
本文面向：有python基础，刚接触web框架的初学者。

　　环境：windows7  　　python3.5.1 　　pycharm专业版 　　Django 1.10版　　pip3

一、Django简介
　　百度百科：开放源代码的Web应用框架，由Python语言编写......
　　重点：一个大而全的框架，啥都替你考虑好了。

1. web框架介绍
　　具体介绍Django之前，必须先介绍WEB框架等概念。
　　web框架： 别人已经设定好的一个web网站模板，你学习它的规则，然后“填空”或“修改”成你自己需要的样子。
　　一般web框架的架构是这样的：
   ![web 框架](mysite/img/1.PNG)
　　其它基于python的web框架，如tornado、flask、webpy都是在这个范围内进行增删裁剪的。例如tornado用的是自己的异步非阻塞“wsgi”，flask则只提供了最精简和基本的框架。Django则是直接使用了WSGI，并实现了大部分功能。
2. MVC/MTV介绍
　　MVC百度百科：全名Model View Controller，是模型(model)－视图(view)－控制器(controller)的缩写，一种软件设计典范，用一种业务逻辑、数据、界面显示分离的方法组织代码，将业务逻辑聚集到一个部件里面，在改进和个性化定制界面及用户交互的同时，不需要重新编写业务逻辑。

　　通俗解释：一种文件的组织和管理形式！不要被缩写吓到了，这其实就是把不同类型的文件放到不同的目录下的一种方法，然后取了个高大上的名字。当然，它带来的好处有很多，比如前后端分离，松耦合等等，就不详细说明了。　　　　　　　
　　模型(model)：定义数据库相关的内容，一般放在models.py文件中。
　　视图(view)：定义HTML等静态网页文件相关，也就是那些html、css、js等前端的东西。
　　控制器(controller)：定义业务逻辑相关，就是你的主要代码。　　
　　MTV: 有些WEB框架觉得MVC的字面意思很别扭，就给它改了一下。view不再是HTML相关，而是主业务逻辑了，相当于控制器。html被放在Templates中，称作模板，于是MVC就变成了MTV。这其实就是一个文字游戏，和MVC本质上是一样的，换了个名字和叫法而已，换汤不换药。

3.Django的MTV模型组织
　　目录分开，就必须有机制将他们在内里进行耦合。在Django中，urls、orm、static、settings等起着重要的作用。一个典型的业务流程是如下图所示：
![web 业务流程](mysite/img/2.PNG)
那么我们学Django学的是什么？

1. 目录结构规范
2. urls路由方式
3. settings配置
4. ORM操作
5. jinja2模板渲染
6.其它
二、Django项目实例
1. 程序安装
　　python3.5、pip3及pycharm专业版自行安装。pycharm不要使用免费版，它不支持Django。
（1）安装Django：
　　这里只介绍较为简单的pip3命令安装方式。
　　win+r，调出cmd，运行命令：pip3 install django，自动安装Pypi提供的最新版本。
  ![安装](mysite/img/3.PNG)
  ![安装](mysite/img/4.PNG)
  ![安装](mysite/img/5.PNG)
  ![安装](mysite/img/6.PNG)
  ![安装](mysite/img/7.PNG)
（2）配置系统环境
成功安装Django后，在下图中的路径可找到django-admin.exe文件，将它加入操作系统环境变量中。这样在以后的调用会比较方便。


 2. 创建django项目
　　在linux等命令行界面下，使用django提供的命令和vim也能进行项目开发。但是，这里推荐使用pycharm这个目前最好的python开发IDE
，它功能强大，界面友好。（下面所有的操作都在pycharm中进行。）
　　点击：file-->new project，出现下面的对话框。
 ![安装](mysite/img/8.PNG)
选择Django栏目，输入项目名称，这里采用国际惯例的mysite。选择python解释器版本，点击create创建。
Django将自动生成下面的目录结构：
 ![安装](mysite/img/9.PNG)
与项目同名的目录中是配置文件，templates目录是html文件存放也就是MTV中的T。manage.py是django项目管理文件。
 ![安装](mysite/img/10.PNG)

3. 创建APP
　　在每个django项目中可以包含多个APP，相当于一个大型项目中的分系统、子模块、功能部件等等，相互之间比较独立，但也有联系。
所有的APP共享项目资源。
　　在pycharm下方的terminal终端中输入命令：
　　python manage.py startapp cmdb
　　这样就创建了一个叫做cmdb的APP，django自动生成“cmdb”文件夹。
  ![创建app](mysite/img/11.PNG)

4. 编写路由
　　路由都在urls文件里，它将浏览器输入的url映射到相应的业务处理逻辑。
　　简单的urls编写方法如下图：
  ![编写路由](mysite/img/13.PNG)
  
5. 编写业务处理逻辑
　　业务处理逻辑都在views.py文件里。
  ![编写业务处理逻辑](mysite/img/12.PNG)
 　通过上面两个步骤，我们将index这个url指向了views里的index（）函数，它接收用户请求，并返回一个“hello world”字符串。

6. 运行web服务
　　现在我们已经可以将web服务运行起来了。
　　命令行的方式是：python manage.py runserver 127.0.0.1:8000
　　但在pycharm中，你可以这么干：
　　在上部工具栏中找到下面图示的图标。
  ![编写业务处理逻辑](mysite/img/14.PNG)
  
  
  
