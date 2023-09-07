from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField

 # 프로필 이미지 등록
class User(AbstractUser):
    profile_image = ResizedImageField(
        size=[500, 500],
        crop=['middle', 'center'],
        upload_to='profile',
    )
    # post_set = ForeignKey로 인해 자동으로 생겨남
    # post_set = ManyToManyField로 또 같은 이름으로 또 생겨서 에러남 -> realated_name=으로 like_posts로 바꿔줌
    # like_posts = ManyToManyField로 인해 자동으로 생겨남

    followings = models.ManyToManyField('self', related_name='followers', symmetrical=False)
    # 원래는 user_set 자동으로 생성인데 related_name으로 인하여 followers = 로 자동생성



