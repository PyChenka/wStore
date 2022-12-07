from core.choice_settings import DROP_MENU_YEARS

MENU = [
    {'name': 'Shop',
     'url': 'shop:index'},
    {'name': 'About',
     'url': 'about'},
    {'name': 'Blog',
     'url': 'blog:index',
     'drop_name': DROP_MENU_YEARS,
     'drop_url': 'blog:by_year'},
    {'name': 'Contact',
     'url': 'contact:contact'},
    {'name': 'Sign In',
     'url': 'users:login'}
]


def menu(request):
    """
    Добавляет в контекст переменные:
    name - название сайта,
    menu - пункты меню со ссылками
    """
    return {
        'name': 'Windstore',
        'menu': MENU
    }
