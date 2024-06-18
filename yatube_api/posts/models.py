from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import F, Q

User = get_user_model()


class Group(models.Model):
    """Модель групп."""

    title = models.TextField()
    slug = models.SlugField()
    description = models.TextField()


class Post(models.Model):
    """Модель постов."""

    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, null=True, blank=True
    )
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)

    def __str__(self):
        return self.text[:25]

    class Meta:
        ordering = ('pub_date',)


class Comment(models.Model):
    """Модель комментариев."""

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Follow(models.Model):
    """Модель подписок."""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followers_set')
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following_set')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_follow'
            ),
            models.CheckConstraint(
                check=~Q(user=F('following')),
                name='prevent_self_follow'
            )
        ]
