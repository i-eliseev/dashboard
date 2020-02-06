from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse

class Image(models.Model):
    """Один ко многим - один юзер может загрузить много картинок,
    но каждая картинка может быть загружена только одним пользователем"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name = 'images_created',
                             on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True, db_index=True)

    """Многие ко многим - каждую картинку может лайкать каждый пользователь"""
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                       related_name='images_liked',
                                       blank=True)

    def __str__(self):
        return self.title

    """ПЕРЕОПРЕДЕЛЯЕМ МЕТОД SAVE, ДЛЯ СЛАГИФИКАЦИИ TITLE, ЕСЛИ СЛАГ ЯВНО НЕ УКАЗАН"""
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])

