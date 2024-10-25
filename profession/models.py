from django.db import models
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete, get_thumbnail
from tinymce.models import HTMLField


class Sector(models.Model):
    title = models.CharField(
        'Сектор',
        max_length=150,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сектор'
        verbose_name_plural = 'Сектора'


class Profession(models.Model):
    title = models.CharField(
        'Название профессии',
        max_length=150,
    )
    description = HTMLField(
        verbose_name='описание',
        help_text='Введите ваше описание профессии',
    )
    photo = models.ImageField(
        upload_to='uploads/preview/%Y/%m',
        verbose_name='картинка',
        help_text='Загрузите картинку',
        null=True,
    )
    sector = models.ForeignKey(
        Sector,
        on_delete=models.CASCADE,
        verbose_name="Сектор",
        help_text='Выберете сектор'
    )
    study = models.URLField()

    @property
    def get_img(self):
        return get_thumbnail(
            self.photo,
            '300x300',
            crop='center',
            quality=51,
        )

    def img_tmb(self):
        if self.photo:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )
        return 'нет изображений'

    img_tmb.short_description = 'Превьюшка'
    img_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'
