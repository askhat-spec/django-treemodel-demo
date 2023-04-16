from django import template
from games.models import Genre

register = template.Library()


@register.inclusion_tag('template_tags/genre.html', takes_context=True)
def draw_genres(context):
    context['current_url'] = context['request'].path
    try:
        genre_items = Genre.objects.filter(parent=None).prefetch_related('children')
        context['genre_items'] = genre_items
        return context
    except Genre.DoesNotExist:
        context['genre_items'] = ''
        return context
