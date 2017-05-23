# -*- coding: utf-8 -*-
"""CatReading URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from books import views
from account import views
from admin import views
from reward import views
from comment import views
from statistics import views
import books
import account
import admin
import reward
import comment
import statistics

urlpatterns = [
    # 首页
    url(r'^$', books.views.indexPage, name='index'),
    # 书库页
    url(r'^library/', books.views.libraryPage, name='library'),
    # 排行页
    url(r'^rank/', books.views.rankPage, name='rank'),

    # 详情页
    url(r'^bookDetails/', books.views.bookDetailsPage, name='bookDetails'),
    url(r'^catalogue/[0-9]+/$', books.views.cataloguePage, name='catalogue'),
    url(r'^bookCommentInfo/[0-9]+/$', books.views.bookCommentPage, name='bookCommentPage'),
    url(r'^bookRewardInfo/[0-9]+/$', books.views.bookRewardPage, name='bookRewardPage'),

    # 详情页
    url(r'^books/[0-9]+/$', books.views.bookDetailsPage,  name='bookDetails'),
    url(r'^books/[0-9]+/chapters/[0-9]+/$', books.views.readingPage, name='Reading'),

    # 登陆页
    url(r'^login/$', account.views.loginPage, name='login'),

    # 个人中心
    url(r'^center/$', account.views.userCenterPage, name='centered'),
    url(r'^userHistoryComment/$', account.views.userHistoryCommentPage, name='userHistoryComment'),

    # 注册页
    url(r'^oneRegister/', account.views.oneRegisterPage, name='firstRegister'),
    url(r'^twoRegister/', account.views.twoRegisterPage, name='twoRegister'),
    url(r'^threeRegister/$', account.views.threeRegisterPage, name='threeRegister'),

    # 找回密码页面
    url(r'^oneFind/$', account.views.oneFindPage, name='oneFind'),
    url(r'^twoFind/$', account.views.twoFindPage, name='twoFind'),
    url(r'^threeFind/$', account.views.threeFindPage, name='threeFind'),
    url(r'^fourFind/$', account.views.fourFindPage, name='fourFind'),
                                                                
    url(r'^createBook/$', admin.views.createBookPage, name='createbook'),
    url(r'^bookManager/$', admin.views.BookManagerPage, name='bookManager'),
    url(r'^editbookinfo/[0-9]+/$', admin.views.EditBookInfoPage, name='check'),
    url(r'^publish/[0-9]+/$', admin.views.PublishPage, name='publish'),
    url(r'^commentManager/[0-9]+/$', admin.views.commentManagerPage, name='commentManager'),
    url(r'^WriteChapter/[0-9]+/$', admin.views.WriteChaptersPage, name='write'),

    url(r'^uploadimg/$', admin.views.UploadImgPage),

    url(r'^userManager/$', admin.views.UserManagerPage),

    url(r'^datastatistics/$', admin.views.dataStatisticsPage),


    # 首页API请求接口
    url(r'^ShowImgViewAPI/', books.views.ShowImgViewAPI.as_view()),
    url(r'^FreeCompetitiveViewAPI/', books.views.FreeCompetitiveViewAPI.as_view()),
    url(r'^GroundCompetitiveViewAPI/', books.views.GroundCompetitiveViewAPI.as_view()),
    url(r'^HotRecommendViewAPI/', books.views.HotRecommendViewAPI.as_view()),
    url(r'^NewRecommendViewAPI/', books.views.NewRecommendViewAPI.as_view()),
    url(r'^LibraryViewAPI/', books.views.LibraryViewAPI.as_view()),
    # 排行页API请求接口
    url(r'^RankListViewAPI/', books.views.RankListViewAPI.as_view()),
    # 详情页API请求接口
    url(r'^ChaptersViewAPI/', books.views.ChaptersViewAPI.as_view()),
    url(r'^BookInfoHeadViewAPI/', books.views.BookInfoHeadViewAPI.as_view()),

    url(r'^BookInfoViewAPI/', books.views.BookInfoViewAPI.as_view()),

    url(r'^RewardViewAPI/', reward.views.RewardViewAPI.as_view()),
    url(r'^CommentViewAPI/', comment.views.CommentViewAPI.as_view()),

    url(r'^CommentUserViewAPI/', comment.views.CommentUserViewAPI.as_view()),

    url(r'^RewardBookViewAPI/', reward.views.RewardBookViewAPI.as_view()),
    url(r'^CommentBookViewAPI/', comment.views.CommentBookViewAPI.as_view()),

    # 阅读页面API请求接口
    url(r'^ReadingViewAPI/', books.views.ReadingViewAPI),

    # 图片验证码API请求接口
    url(r'^captcha/$', 'utils.captcha.views.show_captcha', name="show_captcha"),

    # 用户注册API请求接口
    url(r'^UserRegisterAPIView/', account.views.UserRegisterAPIView.as_view()),
    url(r'^UserLogoutAPIView/', account.views.UserLogoutAPIView.as_view()),
    # 用户登陆API请求接口
    url(r'^UserLoginAPIView/', account.views.UserLoginAPIView.as_view()),
    # 用户改变密码API请求接口
    url(r'^ChangePasswordAPIView/', account.views.ChangePasswordAPIView.as_view()),
    # 短信发送API请求接口
    url(r'^MessageAPIView/', account.views.MessageAPIView.as_view()),
    # 检查手机验证码API请求接口
    url(r'^CheckTokenAPIView/', account.views.CheckTokenAPIView.as_view()),

    url(r'^UserCenterAPIView/', account.views.UserCenterAPIView.as_view()),



    # 测试

    url(r'^CommentManagerViewAPI/', comment.views.CommentManagerViewAPI.as_view()),
    url(r'^CreateBookAPIView/', admin.views.CreateBookAPIView.as_view()),
    url(r'^BookListAPIView/', admin.views.BookListAPIView.as_view()),
    url(r'^CreateChapterAPIView/', admin.views.CreateChapterAPIView.as_view()),
    url(r'^DeleteBookAPIView/', admin.views.DeleteBookAPIView.as_view()),
    url(r'^ChaptersListAPIView/', admin.views.ChaptersListAPIView.as_view()),
    url(r'^DeleteChapterAPIView/', admin.views.DeleteChapterAPIView.as_view()),
    url(r'^ShowBookInfoAPIView/', admin.views.ShowBookInfoAPIView.as_view()),
    url(r'^EditBookInfoAPIView/', admin.views.EditBookInfoAPIView.as_view()),
    url(r'^EditChapterListAPIView/', admin.views.EditChapterListAPIView.as_view()),
    url(r'^ShowChapterAPIView/', admin.views.ShowChapterAPIView.as_view()),
    url(r'^WordCountAPIView/', admin.views.WordCountAPIView.as_view()),
    url(r'^ReleaseChapterAPIView/', admin.views.WordCountAPIView.as_view()),
    url(r'^CoverImgUploadAPIView/', admin.views.CoverImgUploadAPIView.as_view()),

    url(r'^ShowUserListAPIView/', admin.views.ShowUserListAPIView.as_view()),
    url(r'^EditUserAPIView/', admin.views.EditUserAPIView.as_view()),

    url(r'^DataStaticsAPIView/', statistics.views.DataStaticsAPIView.as_view()),

    # url(r'^AlipayAPIView/', admin.views.AlipayAPIView.as_view()),
]
