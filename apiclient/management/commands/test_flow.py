""" Команда проверки работы клиента АПИ """

import random
import string
from typing import NoReturn

from django.core.management.base import BaseCommand

from apiclient import exceptions
from apiclient.gateways import TeachbaseGateway


class Command(BaseCommand):
    help = (
        "Проходит цикл получения информации по курсам, создании пользователя "
        "и записи пользователя на сессию курса"
    )

    def __init__(self):
        self.gateway = TeachbaseGateway()
        super().__init__()

    def handle(self, *args, **options):
        """Flow проверки работы TeachbaseGateway"""

        try:
            # создаем пользователя
            user = self.create_user()
            self._success_message(f'Создан пользователь "{user["email"]}"')

            # получаем список курсов
            courses = self.get_courses()
            course = courses[0]
            self._success_message("Получен список курсов")

            # получение список сессий курса
            course_sessions = self.get_course_sessions(course)
            session = course_sessions[0]
            self._success_message(f'Получен список сессий курса "{session["name"]}"')

            # регистрируем созданного пользователя на сессию
            self.register_user_on_session(user, session)
            self._success_message(
                f'Пользователь "{user["email"]}" записан на сессию'
                f' "{session["name"]}" курса "{course["name"]}"'
            )

            # проверяем, что пользователь зарегистрирован на сессию
            is_user_registered = self.check_user_is_registered_on_session(
                user=user, session=session
            )

            if is_user_registered:
                self._success_message("Проверка записи пользователя на сессию пройдена")
            else:
                self._error_message(
                    "Проверка записи пользователя на сессию не пройдена"
                )

        except exceptions.UserCreateError:
            self._error_message("Ошибка при создании пользователя")
            raise

        except exceptions.CourseSessionsReceiveError:
            self._error_message("Ошибка при получении сессий курса")
            raise

        except exceptions.RegisterUserSessionError:
            self._error_message("Ошибка при попытке записать пользователя на сессию")
            raise

    def create_user(self) -> dict:
        """Создание пользователя"""

        # рандомно создаем email и номер телефона
        user_email = (
            "".join(random.sample(population=string.ascii_lowercase, k=10)) + "@mail.ru"
        )
        user_phone_number = "+7" + "".join(
            random.sample(population=string.digits, k=10)
        )

        user = {
            "email": user_email,
            "name": "John",
            "last_name": "Doe",
            "phone": user_phone_number,
            "password": "qwerty",
            "description": "Corrupti natus quia recusandae.",
        }

        users = self.gateway.create_user(**user)
        created_user = users[0]
        return created_user

    def get_courses(self) -> list:
        """Получение списка курсов"""

        courses = self.gateway.get_courses()
        return courses

    def get_course_sessions(self, course: dict) -> list:
        """Получение списка курса сессий выбранного курса

        :param course: словарь с курсом, полученный из Teachbase API
        """

        course_sessions = self.gateway.get_course_sessions(course_id=course["id"])
        return course_sessions

    def register_user_on_session(self, user: dict, session: dict) -> NoReturn:
        """Запись переданного пользователя на сессию курса

        :param user: словарь с данными пользователя, полученный из Teachbase API
        :param session: словарь с данными сессии курса, полученный из Teachbase API
        """

        self.gateway.register_user_course_session(user["id"], session["id"])

    def check_user_is_registered_on_session(self, user: dict, session: dict) -> bool:
        """Проверка, что пользователь записан на сессию

        :param user: словарь с данными пользователя, полученный из Teachbase API
        :param session: словарь с данными сессии курса, полученный из Teachbase API
        """

        session_info = self.gateway.get_session_details(
            course_id=session["course"]["id"], session_id=session["id"]
        )

        for participant in session_info["participants"]:
            if participant["email"] == user["email"]:
                return True
        return False

    def _success_message(self, message: str) -> NoReturn:
        """Вывод зеленого сообщения в терминал"""

        self.stdout.write(self.style.SUCCESS(message))

    def _error_message(self, message: str) -> NoReturn:
        """Вывод красного сообщения в терминал"""

        self.stdout.write(self.style.ERROR(message))

    def _warning_message(self, message: str) -> NoReturn:
        """Вывод желтого сообщения в терминал"""

        self.stdout.write(self.style.WARNING(message))
