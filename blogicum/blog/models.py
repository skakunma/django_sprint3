from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    is_published = models.BooleanField(
        default=True,
        null=False,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False,
        verbose_name='Добавлено'
    )

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(
        unique=True,
        verbose_name='Идентификатор',
        help_text='Идентификатор страницы для URL; разрешены символы латиницы, цифры, дефис и подчёркивание.'
    )


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


class Location(BaseModel):
    name = models.CharField(max_length=256, verbose_name='Название места')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'


class Post(BaseModel):
    title = models.CharField('Заголовок', max_length=256)
    text = models.TextField('Текст')
    pub_date = models.DateTimeField(
        'Дата и время публикации',
        help_text='Если установить дату и время в будущем '
        '— можно делать отложенные публикации.'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Автор публикации')
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL,
        null=True, verbose_name= 'Местоположение')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        null=True, verbose_name='Категория')


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
