MENU = [
    {'name': 'Shop',
     'url': 'shop:index'},
    {'name': 'About',
     'url': 'about'},
    {'name': 'Blog',
     'url': 'blog:index',
     'drop_name': [2022, 2023],
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
