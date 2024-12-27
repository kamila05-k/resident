# Generated by Django 5.1.3 on 2024-12-11 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.CharField(choices=[('Главное', 'Главное'), ('Популярные', 'Популярные'), ('Недвижимость', 'Недвижимость'), ('Раскошный отдых', 'Раскошный отдых'), ('Продукты', 'Продукты'), ('Интервью', 'Интервью')], max_length=255, verbose_name='Блог')),
                ('ratation', models.CharField(choices=[('1', 'Ротация 1'), ('2', 'Ротация 2'), ('3', 'Ротация 3'), ('4', 'Ротация 4'), ('5', 'Ротация 5')], max_length=255, verbose_name='Ротация')),
                ('pc_image', models.ImageField(blank=True, null=True, upload_to='slider/', verbose_name='Баннер для ПК версии')),
                ('mb_img', models.ImageField(blank=True, null=True, upload_to='slider/', verbose_name='Баннер для мобильной версии')),
                ('url', models.URLField(verbose_name='Укажите ссылку')),
                ('date', models.DateField(verbose_name='Дата истечения')),
            ],
            options={
                'verbose_name': 'Баннер',
                'verbose_name_plural': 'Баннеры',
                'constraints': [models.UniqueConstraint(fields=('blog', 'ratation'), name='unique_blog_ratation')],
            },
        ),
    ]
