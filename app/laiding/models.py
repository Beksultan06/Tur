from django.db import models
from ckeditor.fields import RichTextField
from PIL import Image as PILImage
from io import BytesIO
from django.core.files.base import ContentFile
import os


RATING_CHOICES = [
    (1, "★☆☆☆☆ (1)"),
    (2, "★★☆☆☆ (2)"),
    (3, "★★★☆☆ (3)"),
    (4, "★★★★☆ (4)"),
    (5, "★★★★★ (5)"),
]


def convert_to_webp(image_field):
    if not image_field:
        return image_field

    img = PILImage.open(image_field)
    img = img.convert("RGB")  
    buffer = BytesIO()
    img.save(buffer, format="WEBP", quality=85)

    base, _ = os.path.splitext(image_field.name)
    new_name = f"{base}.webp"
    return ContentFile(buffer.getvalue(), name=new_name)


class Settings(models.Model):
    logo = models.ImageField(upload_to='logo/', verbose_name='Логотип сайта')
    title = models.CharField(max_length=155, verbose_name='Заголовок главного баннера')
    description = RichTextField(verbose_name='Описание главного баннера')
    image_back = models.ImageField(upload_to='main/', verbose_name='Фон главного баннера')

    title_about = models.CharField(max_length=155, verbose_name='Заголовок раздела "О нас"')
    text1 = models.CharField(max_length=255, verbose_name='Текст (правая сторона)')
    text2 = models.CharField(max_length=255, verbose_name='Текст (левая сторона)')
    image_about = models.ImageField(upload_to='main/', verbose_name='Фото раздела "О нас"')
    logo_about = models.ImageField(upload_to='main/', verbose_name='Логотип в разделе "О нас"')
    image_about_blok = models.ImageField(upload_to='main/', verbose_name='Фото блока о нас (1)')
    image_about_blok2 = models.ImageField(upload_to='main/', verbose_name='Фото блока о нас (2)')
    description_about = RichTextField(verbose_name='Описание блока "О нас" (1)')
    description_about2 = RichTextField(verbose_name='Описание блока "О нас" (2)')

    values = models.CharField(max_length=155, verbose_name='Заголовок блока "Ценности"')
    title_missions = models.CharField(max_length=155, verbose_name='Заголовок блока "Миссия"')
    description_missions = RichTextField(verbose_name='Описание миссии')

    title_directions = models.CharField(max_length=155, verbose_name='Заголовок блока "Направления"')
    title_development = models.CharField(max_length=155, verbose_name='Заголовок блока "Развитие"')
    description_development = RichTextField(verbose_name='Описание блока "Развитие"')

    title_parrners = models.CharField(max_length=155, verbose_name='Заголовок блока "Партнеры"')
    description_parrners = models.CharField(
        max_length=355,
        verbose_name='Описание Партнера'
    )
    title_reviews = models.CharField(max_length=155, verbose_name='Заголовок блока "Отзывы"')
    title_blog = models.CharField(max_length=155, verbose_name='Заголовок блока "Блог"')
    description_blog = RichTextField(verbose_name='Описание блока "Блог"')

    title_end = models.CharField(max_length=155, verbose_name='Заголовок блока "Готовы к путешествию"')
    image_end = models.ImageField(upload_to='main/', verbose_name='Фото блока "Готовы к путешествию"')

    title_feedback = models.CharField(max_length=155, verbose_name='Заголовок формы обратной связи')
    description_feedback = RichTextField(verbose_name='Описание формы обратной связи')

    title_contact = models.CharField(max_length=155, verbose_name='Заголовок блока "Контакты"')
    phone_number = models.CharField(max_length=25, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Почта администратора')
    address = RichTextField(verbose_name='Адрес')
    text = models.CharField(max_length=155, verbose_name='Наименование компании')
    end_text = models.CharField(max_length=350, verbose_name='Текст нижней части сайта')
    
    telegram = models.CharField(
        max_length=355,
        verbose_name='Ссылка на Telegram '
    )
    watchap = models.CharField(
        max_length=355,
        verbose_name='Ссылка на Ватсап '
    )
    inta = models.CharField(
        max_length=355,
        verbose_name='Ссылка на Инстаграм '
    )
    title_statistic = models.CharField(
        max_length=155,
        verbose_name='Заголовок',
        blank=True, null=True
    )

    def save(self, *args, **kwargs):
        image_fields = [
            'logo', 'image_back', 'image_about', 'logo_about',
            'image_about_blok', 'image_about_blok2', 'image_end'
        ]
        for field_name in image_fields:
            image_field = getattr(self, field_name)
            if image_field and not image_field.name.lower().endswith('.webp'):
                converted = convert_to_webp(image_field)
                if converted:
                    setattr(self, field_name, converted)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Главные настройки сайта'
        verbose_name_plural = 'Главные настройки сайта'


class Values(models.Model):
    title = models.CharField(max_length=155, verbose_name='Заголовок')
    image = models.ImageField(upload_to='values', verbose_name='Изображение')

    def save(self, *args, **kwargs):
        if self.image and not self.image.name.lower().endswith('.webp'):
            self.image = convert_to_webp(self.image)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ценность'
        verbose_name_plural = 'Ценности компании'


class Image(models.Model):
    image = models.ImageField(upload_to='main', verbose_name='Фото')

    def save(self, *args, **kwargs):
        if self.image and not self.image.name.lower().endswith('.webp'):
            self.image = convert_to_webp(self.image)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Изображение галереи'
        verbose_name_plural = 'Галерея'


class Direction(models.Model):
    title = models.CharField(max_length=155, verbose_name='Заголовок')
    description = RichTextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'


class DirectionImage(models.Model):
    direction = models.ForeignKey(
        Direction,
        on_delete=models.CASCADE,
        related_name='direction',
        verbose_name='Направление'
    )
    image = models.ImageField(upload_to='direction', verbose_name='Фото')

    def save(self, *args, **kwargs):
        if self.image and not self.image.name.lower().endswith('.webp'):
            self.image = convert_to_webp(self.image)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Фото направления'
        verbose_name_plural = 'Фото направлений'


class PartnerImage(models.Model):
    image = models.ImageField(upload_to='partners', verbose_name='Логотип партнера')

    def save(self, *args, **kwargs):
        if self.image and not self.image.name.lower().endswith('.webp'):
            self.image = convert_to_webp(self.image)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'


class Reviews(models.Model):
    name = models.CharField(max_length=155, verbose_name='Имя клиента')
    date = models.CharField(max_length=155, verbose_name='Дата отзыва')
    description = models.TextField(verbose_name='Текст отзыва')
    star = models.CharField(
        max_length=25, verbose_name='Рейтинг',
        blank=True, null=True,
        help_text='Максимум 5 звезд'
    )

    def __str__(self):
        return f"{self.name} ({self.star}★)"

    class Meta:
        verbose_name = 'Отзыв клиента'
        verbose_name_plural = 'Отзывы клиентов'


class Blog(models.Model):
    title = models.CharField(max_length=155, verbose_name='Заголовок статьи')
    description = RichTextField(verbose_name='Содержание статьи')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья блога'
        verbose_name_plural = 'Блог'


class Feedback(models.Model):
    name = models.CharField(max_length=155, verbose_name='Имя пользователя')
    email = models.EmailField(verbose_name='Почта')
    phone = models.CharField(max_length=25, verbose_name='Номер телефона')
    message = models.TextField(verbose_name='Сообщение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сообщение обратной связи'
        verbose_name_plural = 'Обратная связь'


class Services(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'
        
class Statistic(models.Model):
    types = models.CharField(
        max_length=155,
        verbose_name='Тип'
    )
    statistic = models.CharField(
        max_length=25,
        verbose_name='Статистика'
    )
    
    def __str__(self):
        return self.types