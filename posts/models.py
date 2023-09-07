from django.db import models
from django_resized import ResizedImageField
from django.conf import settings

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) # 수정이 될 때마다 업데이트
    # image = models.ImageField(upload_to='image/%Y/%m') # 새로추가 -> 사용하기 위해서는 pillow라는 library 필요
    image = ResizedImageField(
        size=[500, 500],
        crop=['middle', 'center'],
        upload_to='image/%Y/%m'
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # user_id = 생성 

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')


class Comment(models.Model):
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey(Post, on_delete=models.CASCADE) # 어떤 게시물과 연결이 되어있는지
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # 작성자 저장
