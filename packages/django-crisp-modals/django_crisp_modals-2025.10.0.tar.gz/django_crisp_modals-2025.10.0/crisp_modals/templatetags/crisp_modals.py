from django.template import Library
from django.utils.safestring import mark_safe

register = Library()


@register.filter
def verbose_name(obj):
    return obj._meta.verbose_name


@register.filter
def object_description(obj):
    return mark_safe(f"<strong>{obj._meta.verbose_name.title()}</strong> &ndash; {obj}")


def render_list(items, root=True):
    html = '<ul class="list-unstyled">' if root else '<ul>'
    for item in items:
        if isinstance(item, list):
            html += render_list(item, root=False)
        else:
            html += f'<li>{item}</li>'
    html += '</ul>'
    return html


@register.filter(is_safe=True)
def html_list(value):
    if not isinstance(value, list):
        return value
    return mark_safe(render_list(value))


@register.filter(is_safe=True)
def list_objects(items):
    html = '<ul class="list-unstyled">'
    for item in items:
        html += f'<li>{object_description(item)}</li>'
    html += '</ul>'
    return mark_safe(html)
