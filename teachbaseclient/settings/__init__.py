"""
Основной файл django-split-settings.

Окружение по умолчанию - `developement`.
Для изменения окружения, в файле .env:
`DJANGO_ENV=production python manage.py runserver`
"""
import os

from split_settings.tools import optional, include
from dotenv import load_dotenv


load_dotenv()

ENV = os.getenv('DJANGO_ENV') or 'development'

base_settings = [
    'components/common.py',  # стандартные настройки
    'components/database.py',  # бд

    # Выбор окружения:
    'environments/{0}.py'.format(ENV),

    # Для переопределения настроек:
    optional('environments/local.py'),
]

include(*base_settings)
