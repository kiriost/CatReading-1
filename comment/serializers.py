# **coding: utf-8**

from rest_framework import serializers
from .models import Comment

"""
    Author:	         成成
    Version:         0.01v
    Date:            2017/05/01
    Description:     评论的数据序列化
"""


class CommentSerializers(serializers.ModelSerializer):
    commentTime = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('userName', 'bookName', 'commentTitle', 'commentContent', 'commentTime',
                  'commentStick', 'commentEssence')

    def get_commentTime(self, obj):
        return obj.commentTime.strftime("%Y-%m-%d")


class BookInfoCommentSerializers(serializers.Serializer):
    # 用户名
    userName = serializers.CharField(max_length=30)
    # 评论标题
    commentTitle = serializers.CharField(max_length=20)
    # 评论内容
    commentContent = serializers.CharField(max_length=120)
    # # 评论时间
    # commentTime = serializers.DateTimeField()
    # 评论置顶
    commentStick = serializers.BooleanField(default=True)
    # 评论精华
    commentEssence = serializers.BooleanField(default=True)


class CommentUserSerializers(serializers.ModelSerializer):
    commentTime = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('bookId', 'bookName', 'commentTitle', 'commentContent', 'commentTime',
                  'commentStick', 'commentEssence')

    def get_commentTime(self, obj):
        return obj.commentTime.strftime("%Y-%m-%d")


class CommentManagerSerializers(serializers.ModelSerializer):
    commentTime = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('userName', 'commentTitle', 'commentContent', 'commentTime')

    def get_commentTime(self, obj):
        return obj.commentTime.strftime("%Y-%m-%d")