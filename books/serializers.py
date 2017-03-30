# **coding: utf-8**
"""
    Copyright (c), 2016-2017,  beluga Tech.
    File name： view.py
    Description: 阅读应用模块的视图处理
"""

from .models import BookInfo, BooksContent
from rest_framework import serializers

# # 阅读页序列化
# class ReadingPageSerializers(serializers.Serializer):
#     # 书名


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     详情页列表的数据序列化
"""
class ChaptersListSerializers(serializers.Serializer):
    # 书籍ID
    book_id = serializers.IntegerField(read_only=True)
    # 书籍类型
    type = serializers.IntegerField(read_only=True)
    # 书籍名
    name = serializers.CharField(max_length=20, read_only=True)


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     排行榜列表的数据序列化
"""
class RankListSerializers(serializers.Serializer):
    # 书籍ID
    book_id = serializers.IntegerField(read_only=True)
    # 书籍名
    name = serializers.CharField(max_length=20, read_only=True)




"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     免费板块的数据序列化
"""
class FreeCompetitiveSerializers(serializers.Serializer):
    # 书籍ID
    book_id = serializers.IntegerField(read_only=True)
    # 封面
    coverImg = serializers.ImageField(read_only=True)
    # 书名
    name = serializers.CharField(max_length=20, read_only=True)
    # 书籍介绍
    describe = serializers.CharField(max_length=240, read_only=True)
    # 作者名：
    author = serializers.CharField(max_length=20, read_only=True)
    # 作者ID：（暂时不加）
    # 书籍类型
    type = serializers.IntegerField(read_only=True)


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     精品板块的数据序列化
"""
class GroundCompetitiveSerializers(serializers.Serializer):
    # 书籍ID
    book_id = serializers.IntegerField(read_only=True)
    # 封面
    coverImg = serializers.ImageField(read_only=True)
    # 书名
    name = serializers.CharField(max_length=20, read_only=True)
    # 书籍介绍
    describe = serializers.CharField(max_length=240, read_only=True)
    # 作者名：
    author = serializers.CharField(max_length=20, read_only=True)
    # 作者ID：（暂时不加）
    # 书籍类型
    type = serializers.IntegerField(read_only=True)


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     热门板块的数据序列化
"""
class HotRecommendSerializers(serializers.Serializer):
    # 书籍ID
    book_id = serializers.IntegerField(read_only=True)
    # 封面
    coverImg = serializers.ImageField(read_only=True)
    # 书名
    name = serializers.CharField(max_length=20, read_only=True)
    # 书籍介绍
    describe = serializers.CharField(max_length=240, read_only=True)
    # 作者名：
    author = serializers.CharField(max_length=20, read_only=True)
    # 作者ID：（暂时不加）
    # 书籍类型
    type = serializers.IntegerField(read_only=True)


"""
    Author:	         毛毛
    Version:         0.01v
    Date:            2017/03/30
    Description:     新书板块的数据序列化
"""
class NewRecommendSerializers(serializers.Serializer):
    # 书籍ID
    book_id = serializers.IntegerField(read_only=True)
    # 封面
    coverImg = serializers.ImageField(read_only=True)
    # 书名
    name = serializers.CharField(max_length=20, read_only=True)
    # 书籍介绍
    describe = serializers.CharField(max_length=240, read_only=True)
    # 作者名：
    author = serializers.CharField(max_length=20, read_only=True)
    # 作者ID：（暂时不加）
    # 书籍类型
    type = serializers.IntegerField(read_only=True)
