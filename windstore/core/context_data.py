DROP_MENU_YEARS = (2022, 2023)

MENU = [
    {
        'name': 'Shop',
        'url': 'shop:index'
    },
    {
        'name': 'About',
        'url': 'about'
    },
    {
        'name': 'Blog',
        'url': 'blog:index',
        'drop_name': DROP_MENU_YEARS,
        'drop_url': 'blog:by_year'
    },
    {
        'name': 'Contact',
        'url': 'contact:contact'
    },
]

ORDERS_COUNTRIES = (
    (None, 'Choose country'),
    ('Россия', 'Россия'),
    ('US', 'US'),
)

CONTEXT = {
    'main': {
        'title': 'Products.'
    },
    'about': {
        'subtitle': ' - About'
    },
    'blog': {
        'subtitle': ' - Blog',
        'title': 'Articles.'
    },
    'shop': {
        'subtitle': ' - Shop',
        'title': 'Shop.'
    },
    'search': {
        'subtitle': ' - Search',
        'title': 'You searched'
    },
}
