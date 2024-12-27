from django.db import models
from django.db.models import UniqueConstraint
from .choices import BANNER_CHOICES, RATATION_CHOICES

class Banner(models.Model):
    blog = models.CharField('Блог', choices=BANNER_CHOICES, max_length=255)
    ratation = models.CharField('Ротация', choices=RATATION_CHOICES, max_length=255)
    pc_image = models.ImageField('Баннер для ПК версии', upload_to='slider/', blank=True, null=True)
    mb_img = models.ImageField('Баннер для мобильной версии', upload_to='slider/', blank=True, null=True)
    url = models.URLField('Укажите ссылку', max_length=200)
    date = models.DateField('Дата истечения')
    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'
        constraints = [
            UniqueConstraint(fields=['blog', 'ratation'], name='unique_blog_ratation')
        ]
