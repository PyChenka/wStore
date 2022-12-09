from core.context_data import MENU


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
