from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок группы')
    slug = models.SlugField(unique=True, verbose_name='Слаг группы')
    description = models.TextField(verbose_name='Описание группы')

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(verbose_name='Текст поста')
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор поста'
    )
    image = models.ImageField(
        upload_to='posts/',
        null=True,
        blank=True,
        verbose_name='Поле для картинки'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True,
        null=True,
        verbose_name='Группа, принадлежащая посту'
    )

    def __str__(self):
        return self.text


class Comment(models.Model): 

    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='comments', 
        verbose_name='Автор комментария' 
    ) 
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE, 
        related_name='comments', 
        verbose_name='Объект прокомментированного поста' 
    ) 
    text = models.TextField(verbose_name='Текст комментария')
    created = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_now_add=True,
        db_index=True
    )


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        related_name="user",
        verbose_name="Подписчик",
        on_delete=models.CASCADE
    )
    following = models.ForeignKey(
        User,
        related_name="following",
        verbose_name="Автор",
        on_delete=models.CASCADE
    )
