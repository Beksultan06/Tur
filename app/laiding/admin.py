from django.contrib import admin
from django.utils.html import format_html
from modeltranslation.admin import TranslationAdmin
from .models import (
    Settings, Values, Image, Direction, DirectionImage,
    PartnerImage, Reviews, Blog, Feedback, Services, Statistic
)

admin.site.register(Services)
admin.site.register(Statistic)

@admin.register(Settings)
class SettingsAdmin(TranslationAdmin):
    list_display = ('title', 'email', 'phone_number')
    search_fields = ('title', 'email', 'phone_number')
    list_per_page = 20

    fieldsets = (
        ('Главный баннер', {
            'fields': ('logo', 'title', 'description', 'image_back', 'telegram', 'watchap', 'inta')
        }),
        ('О нас', {
            'fields': (
                'title_about', 'text1', 'text2', 'image_about',
                'logo_about', 'image_about_blok', 'image_about_blok2',
                'description_about', 'description_about2', 'title_statistic',
                'description_parrners'
            )
        }),
        ('Ценности и миссия', {
            'fields': ('values', 'title_missions', 'description_missions')
        }),
        ('Развитие и направления', {
            'fields': ('title_directions', 'title_development', 'description_development')
        }),
        ('Партнёры, отзывы и блог', {
            'fields': ('title_parrners', 'title_reviews', 'title_blog', 'description_blog')
        }),
        ('Финальные блоки', {
            'fields': ('title_end', 'image_end', 'title_feedback', 'description_feedback')
        }),
        ('Контакты и футер', {
            'fields': ('title_contact', 'phone_number', 'email', 'address', 'text', 'end_text')
        }),
    )

    class Meta:
        verbose_name = "Главные настройки"
        verbose_name_plural = "Главные настройки"


@admin.register(Values)
class ValuesAdmin(TranslationAdmin):
    list_display = ('title', 'preview_image')
    search_fields = ('title',)

    def preview_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="object-fit: cover; border-radius: 6px;"/>',
                obj.image.url
            )
        return "—"
    preview_image.short_description = "Фото"


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'preview_image')
    readonly_fields = ('preview_image',)
    list_per_page = 20

    def preview_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="60" style="object-fit: cover; border-radius: 4px;"/>',
                obj.image.url
            )
        return "—"
    preview_image.short_description = "Превью"


class DirectionImageInline(admin.TabularInline):
    model = DirectionImage
    extra = 1
    readonly_fields = ('preview_image',)

    def preview_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="60" style="object-fit: cover; border-radius: 4px;"/>',
                obj.image.url
            )
        return "—"
    preview_image.short_description = "Фото"


@admin.register(Direction)
class DirectionAdmin(TranslationAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    inlines = [DirectionImageInline]


@admin.register(PartnerImage)
class PartnerImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'preview_image')
    readonly_fields = ('preview_image',)

    def preview_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="60" style="object-fit: contain; border-radius: 4px;"/>',
                obj.image.url
            )
        return "—"
    preview_image.short_description = "Логотип"


@admin.register(Reviews)
class ReviewsAdmin(TranslationAdmin):
    list_display = ('name', 'date', 'star', 'short_description')
    search_fields = ('name', 'description')
    list_filter = ('star',)

    def short_description(self, obj):
        return obj.description[:60] + "..." if len(obj.description) > 60 else obj.description
    short_description.short_description = "Описание"


@admin.register(Blog)
class BlogAdmin(TranslationAdmin):
    list_display = ('title', 'short_description')
    search_fields = ('title', 'description')

    def short_description(self, obj):
        return obj.description[:80] + "..." if len(obj.description) > 80 else obj.description
    short_description.short_description = "Описание"


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'short_message')
    search_fields = ('name', 'email', 'phone', 'message')
    list_per_page = 25

    def short_message(self, obj):
        return obj.message[:60] + "..." if len(obj.message) > 60 else obj.message
    short_message.short_description = "Сообщение"
