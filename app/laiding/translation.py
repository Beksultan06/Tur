from modeltranslation.translator import register, TranslationOptions
from .models import (
    Settings,
    Values,
    Direction,
    Blog,
    Reviews,
    Services,
    Statistic
)


@register(Statistic)
class StatisticTranslation(TranslationOptions):
    fields = (
        "types",
    )


@register(Services)
class ServicesTranslation(TranslationOptions):
    fields = (
        "title",
        "description",
    )

@register(Settings)
class SettingsTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
        'title_about',
        'text1',
        'text2',
        'description_about',
        'description_about2',
        'values',
        'title_missions',
        'description_missions',
        'title_directions',
        'title_development',
        'description_development',
        'title_parrners',
        'description_parrners',
        'title_reviews',
        'title_blog',
        'description_blog',
        'title_end',
        'title_feedback',
        'description_feedback',
        'title_contact',
        'address',
        'text',
        'end_text',
        'title_statistic',
    )


@register(Values)
class ValuesTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Direction)
class DirectionTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Reviews)
class ReviewsTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
