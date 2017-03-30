# **coding: utf-8**
"""
    Copyright (c), 2016-2017,  beluga Tech.
    File name： view.py
    Description: 阅读应用模块的视图处理
"""


import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.views import APIView
from .models import BookInfo, BooksContent
from .serializers import(
    ChaptersListSerializers, RankListSerializers,
    FreeCompetitiveSerializers, GroundCompetitiveSerializers,
    HotRecommendSerializers, NewRecommendSerializers)

"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     免费板块的视图渲染应用
"""
class FreeCompetitiveViewAPI(APIView):
    def get(self, requset):
        # book = BookInfo.objects.filter().get()
        # bookList = BookInfo.objects.filter.all().[1:10]
        # return HttpResponse("HAHA")
        book = BookInfo.objects.all()
        serializers = FreeCompetitiveSerializers(book, many=True)
        print serializers.data
        response = JsonResponse({"freeCompetitive": json.dumps(serializers.data)})
        return HttpResponse(response)

    @ csrf_exempt
    def post(self, requset):
        book = BookInfo.objects.all()
        serializers = FreeCompetitiveSerializers(book, many=True)
        print serializers.data
        response = JsonResponse({"freeCompetitive": json.dumps(serializers.data)})
        return HttpResponse(response)


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     精品板块的视图渲染
"""
class GroundCompetitiveViewAPI(APIView):
    def get(self, request):
        book = BookInfo.objects.all()
        serializers = FreeCompetitiveSerializers(book, many=True)
        print serializers.data
        response = JsonResponse({"freeCompetitive": json.dumps(serializers.data)})
        return HttpResponse(response)

    @csrf_exempt
    def post(self, request):
        book = BookInfo.objects.all()
        serializers = FreeCompetitiveSerializers(book, many=True)
        print serializers.data
        response = JsonResponse({"freeCompetitive": json.dumps(serializers.data)})
        return HttpResponse(response)


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     热书板块的视图渲染
"""
class HotRecommendSerializers(APIView):
    def get(self, request):
        book = BookInfo.objects.all()
        serializers = FreeCompetitiveSerializers(book, many=True)
        print serializers.data
        response = JsonResponse({"freeCompetitive": json.dumps(serializers.data)})
        return HttpResponse(response)

    @csrf_exempt
    def post(self, request):
        book = BookInfo.objects.all()
        serializers = FreeCompetitiveSerializers(book, many=True)
        print serializers.data
        response = JsonResponse({"freeCompetitive": json.dumps(serializers.data)})
        return HttpResponse(response)


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     新书板块的视图渲染
"""
class NewRecommendSerializers(APIView):
    def get(self, request):
        book = BookInfo.objects.all()
        serializers = FreeCompetitiveSerializers(book, many=True)
        print serializers.data
        response = JsonResponse({"freeCompetitive": json.dumps(serializers.data)})
        return HttpResponse(response)

    @csrf_exempt
    def post(self, request):
        book = BookInfo.objects.all()
        serializers = FreeCompetitiveSerializers(book, many=True)
        print serializers.data
        response = JsonResponse({"freeCompetitive": json.dumps(serializers.data)})
        return HttpResponse(response)

"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     排行榜的视图渲染，
"""
class  RankListSerializers(APIView):
    def get(self, request):
        book = BookInfo.objects.all()
        serializers = FreeCompetitiveSerializers(book, many=True)
        print serializers.data
        response = JsonResponse({"freeCompetitive": json.dumps(serializers.data)})
        return HttpResponse(response)

    @csrf_exempt
    def post(self, request):
        book = BookInfo.objects.all()
        serializers = FreeCompetitiveSerializers(book, many=True)
        print serializers.data
        response = JsonResponse({"freeCompetitive": json.dumps(serializers.data)})
        return HttpResponse(response)


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     免费榜的视图渲染应用
"""
def ReadingViewAPI(request):

    if request.method == 'GET':
        chaptersId = request.GET['chaptersId']
        print chaptersId
        print request.GET
        bookChapter = BooksContent.objects.get(chapters_id=chaptersId)
        response = JsonResponse({'chaptersName': bookChapter.chapters_name, 'chaptersContent': bookChapter.chapters_content})
        return HttpResponse(response)
    else:
        return Http404

"""
    Author:	         cc
    Version:         0.01v
    Date:            2017/03/30
    Description:     首页页面
"""
def indexPage(request):
    return render(request, "reading/index.html")


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     阅读页面
"""
def ReadingPage(request):
    return render(request, "reading/books/Reading.html")


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     阅读页面
"""
def LibraryPage(request):
    return render(request, "reading/books/library.html")

# def Reading(request):
#     # return render(request, "reading/book/ReadingPage.html")
#     book = BookInfo.objects.all()
#     serializers = FreeCompetitiveSerializers(book, many=True)
#     print serializers.data
#     response = JsonResponse({"freeCompetitive": json.dumps(serializers.data)})
#     return HttpResponse(response)


