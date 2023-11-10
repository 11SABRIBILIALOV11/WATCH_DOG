from django import template
from menus.models import MenuItem

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    menu = MenuItem.objects.filter(title=menu_name).first()
    return build_menu(menu)


def build_menu(menu):
    if menu is None:
        return ''

    html = '<ul>'
    html += f'<li class="active"><a href="{menu.url}">{menu.title}</a>'
    html += build_submenu(menu.children.all())
    html += '</li></ul>'

    return html


def build_submenu(submenu):
    if not submenu:
        return ''

    html = '<ul>'
    for item in submenu:
        html += f'<li><a href="{item.url}">{item.title}</a>'
        html += build_submenu(item.children.all())
        html += '</li>'
    html += '</ul>'

    return html
