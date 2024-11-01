from django.db import models
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete, get_thumbnail
from tinymce.models import HTMLField


class Event(models.Model):
    image = models.ImageField(
        upload_to='uploads/preview/%Y/%m',
        null=True,
    )
    title = models.CharField(
        max_length=150,
        unique=True,
    )
    description = HTMLField()
    schedule = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    EVENT_TYPES = [
        (1, 'Онлайн'),
        (2, 'Оффлайн'),
    ]

    event_type = models.PositiveSmallIntegerField(
        verbose_name='тип мероприятия',
        choices=EVENT_TYPES,
        default=2,
    )

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
        return 'no img'

    img_tmb.short_description = 'image'
    img_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_on']
        verbose_name = "мероприятие"
        verbose_name_plural = "мероприятия"
