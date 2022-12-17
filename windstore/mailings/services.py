import requests
from windstore.settings import UNISENDER_API_KEY, UNISENDER_COMMON_LIST_ID


def add_to_unisender_common_list(data):
    """Добавляет email в общий список CommonList в Unisender"""

    method = 'subscribe'
    list_ids = [UNISENDER_COMMON_LIST_ID, ]
    status = 3  # без отправки письма-подтверждения

    params = {
        'format': 'json',
        'api_key': UNISENDER_API_KEY,
        'list_ids': ','.join(list_ids),
        'fields[email]': data,
        'double_optin': status,
    }
    requests.post(f'https://api.unisender.com/ru/api/{method}', params=params)
