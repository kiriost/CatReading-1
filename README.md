# 猫阅读网站


## **开发环境以及开发工具说明**
Ubuntu
16.04 64位
服务器系统名
官网：www.ubuntu.com.cn下载ubuntu镜像，制作启动盘，按步骤装系统。

pip
9.01
python包管理工具
sudo  apt-get install python-pip 
Nginx
1.10.0
网页服务器
控制终端输入：sudo apt-get install nginx
Uwsgi
2.0.14
Web服务器
控制终端输入：sudo pip insatll uwsgi==2.0.14
Python
2.7.12
后端开发语言
官网：
www.python.org下载python2.7.13版本，配置环境变量。
Djanngo
1.9.0
Python Web框架
控制终端输入：sudo pip insatll django==1.9.0
MySQL
5.7.16
后端数据库
控制终端输入：sudo apt-get install mysql-server


开发工具
描述
pycharm community edition
python开发IDE
Navicat for MySQL
MySQL数据库可视化管理工具


## **项目目录** 
.
├── CatReading
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── README.md			// 说明文件
├── static			// 静态文件目录
│   └── src
│       ├── css			// css文件目录
│       ├── img			// 图片文件目录
│       └── js			// js文件目录
│           ├── app
│           └── lib
└── template			// 网页模板目录
    └── src
        ├── admin		// 管理界面目录
        └── reading		// 读书界面目录
            ├── account
            └── index.html	// 阅读首页目录




