# mysite
first project for Django
本文面向：有python基础，刚接触web框架的初学者。

　　环境：windows7  　　python3.5.1 　　pycharm专业版 　　Django 1.10版　　pip3

一、Django简介
　　百度百科：开放源代码的Web应用框架，由Python语言编写......

　　重点：一个大而全的框架，啥都替你考虑好了。

1. web框架介绍
　　具体介绍Django之前，必须先介绍WEB框架等概念。

　　web框架： 别人已经设定好的一个web网站模板，你学习它的规则，然后“填空”或“修改”成你自己需要的样子。

　　一般web框架的架构是这样的：

   ![web 框架](/tree/master/img/1.png)

 

　　其它基于python的web框架，如tornado、flask、webpy都是在这个范围内进行增删裁剪的。例如tornado用的是自己的异步非阻塞“wsgi”，flask则只提供了最精简和基本的框架。Django则是直接使用了WSGI，并实现了大部分功能。
