from django.contrib.auth.models import User
from django.db.models import Count
from rest_framework import serializers
from app.models import Topic, Post, Comment, Report, Friend, Profile


class UserSerializer2(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'id', "first_name", "last_name", "email", "date_joined")


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer2(many=False, read_only=False)
    karma_posts = serializers.SerializerMethodField('get_user_karma_posts')
    karma_comments = serializers.SerializerMethodField('get_user_karma_comments')
    karma_total = serializers.SerializerMethodField('get_user_karma_total')

    def get_user_karma_posts(self, profile):
        up_posts_count = Post.objects.filter(userOP=User.objects.get(username=profile.user.username)) \
            .annotate(countUp=Count("userUpVotesPost"))
        down_posts_count = Post.objects.filter(userOP=User.objects.get(username=profile.user.username)) \
            .annotate(countDown=Count("userDownVotesPost"))
        score_posts = 0
        for i in up_posts_count:
            score_posts += i.countUp
        for i in down_posts_count:
            score_posts -= i.countDown
        return score_posts

    def get_user_karma_comments(self, profile):
        up_comments_count = Comment.objects.filter(user=User.objects.get(username=profile.user.username)) \
            .annotate(countUp=Count("userUpVotesComments"))
        down_comments_count = Comment.objects.filter(user=User.objects.get(username=profile.user.username)) \
            .annotate(countDown=Count("userDownVotesComments"))
        score_comments = 0
        for i in up_comments_count:
            score_comments += i.countUp
        for i in down_comments_count:
            score_comments -= i.countDown
        return score_comments

    def get_user_karma_total(self, profile):
        return self.get_user_karma_comments(profile) + self.get_user_karma_posts(profile)

    class Meta:
        model = Profile
        fields = ('id',
                  'user',
                  'user_details',
                  'birth_date',
                  'registration_date',
                  'user_picture',
                  'gender',
                  'subscriptions',
                  'profile_info_permission',
                  'profile_friends_permission',
                  'profile_topics_permission',
                  'profile_posts_permission',
                  'profile_comments_permission',
                  'karma_posts',
                  'karma_comments',
                  'karma_total'
                  )


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(many=False, read_only=False)

    class Meta:
        model = User
        fields = ('username', 'id', "first_name", "last_name", "email", "date_joined", "profile")


class TopicSerializer(serializers.ModelSerializer):
    userCreator = UserSerializer(many=False, read_only=False)

    class Meta:
        model = Topic
        fields = ('name', 'rules', 'description', 'userCreator', 'creation_date')


class PostSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(many=False, read_only=False)
    userOP = UserSerializer(many=False, read_only=False)

    class Meta:
        model = Post
        fields = ('id',
                  'topic',
                  'title',
                  'content',
                  'clicks',
                  'userUpVotesPost',
                  'userDownVotesPost',
                  'userSaved',
                  'userHidden',
                  'date',
                  'userOP',
                  'nComments',
                  )


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=False)
    post = PostSerializer(many=False, read_only=False)

    class Meta:
        model = Comment
        fields = ('id',
                  'user',
                  'post',
                  'date',
                  'userUpVotesComments',
                  'userDownVotesComments',
                  'text',
                  'reply',
                  'nReplies'
                  )


class ReportSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=False)
    post = PostSerializer(many=False, read_only=False)

    class Meta:
        model = Report
        fields = ('id',
                  'post',
                  'user',
                  'comment',
                  'accepted'
                  )


class FriendSerializer(serializers.ModelSerializer):
    current_user = ProfileSerializer(many=False, read_only=True)

    class Meta:
        model = Friend
        fields = ('users',
                  'current_user'
                  )
