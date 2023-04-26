""" Модуль взаимодействия с API """

from typing import NoReturn
import requests

from django.conf import settings

from apiclient import exceptions


class TeachbaseGateway:
    """Шлюз для взаимодействия с сервером teachbase.ru"""

    def __init__(self):
        self._oauth_access_token = None
        self.client_id = settings.API_CLIENT_ID
        self.client_secret = settings.API_CLIENT_SECRET
        self.api_base_url = settings.API_BASE_URL

    def get_courses(self) -> list:
        """Получение списка курсов"""

        # проверяем наличие oauth-токена
        self._check_or_update_oauth_token()

        url = self.api_base_url + "/courses"
        response = requests.get(
            url, params={"access_token": self._oauth_access_token}, timeout=10
        )

        if not response.ok:
            raise exceptions.CoursesReceiveError(
                response_status=response.status_code,
                reason=response.reason,
                url=response.url,
                error_text=response.text,
            )
        return response.json()

    def get_course_details(self, course_id: int):
        """Получение детальной информации по курсу

        :param course_id: ид курса
        """
        raise NotImplementedError()

    def get_course_sessions(self, course_id: int) -> list:
        """Получение списка сессий курса"""

        # проверяем наличие oauth-токена
        self._check_or_update_oauth_token()

        url = self.api_base_url + f"/courses/{course_id}/course_sessions"

        response = requests.get(
            url, params={"access_token": self._oauth_access_token}, timeout=10
        )

        if not response.ok:
            raise exceptions.CourseSessionsReceiveError(
                response_status=response.status_code,
                reason=response.reason,
                url=response.url,
                error_text=response.text,
            )

        return response.json()

    def get_session_details(self, course_id, session_id) -> dict:
        """Получение информации о сессии (лектор, участники, время начала и окончания)

        :param course_id: ид курса
        :param session_id: ид сессии

        """

        # проверяем наличие oauth-токена
        self._check_or_update_oauth_token()

        url = self.api_base_url + f"/courses/{course_id}/course_sessions/{session_id}"
        response = requests.get(
            url, params={"access_token": self._oauth_access_token}, timeout=10
        )

        if not response.ok:
            raise exceptions.CourseSessionDetailReceiveError(
                response_status=response.status_code,
                reason=response.reason,
                url=response.url,
                error_text=response.text,
            )

        return response.json()

    def create_user(
        self,
        email: str,
        name: str,
        last_name: str,
        phone: str,
        password: str,
        description: str,
    ) -> list[dict]:
        """Создание пользователя

        :param email: user's email
        :param name: user's name
        :param last_name: user's last name
        :param phone: user's phone
        :param password: user's password
        :param description: user's description

        :return: список созданных пользователей
        """

        self._check_or_update_oauth_token()

        url = self.api_base_url + "/users/create"

        data = {
            "access_token": self._oauth_access_token,
            "users": [
                {
                    "email": email,
                    "name": name,
                    "description": description,
                    "last_name": last_name,
                    "phone": phone,
                    "role_id": 1,
                    "password": password,
                    "lang": "ru",
                }
            ],
        }

        response = requests.post(url, json=data, timeout=10)

        if not response.ok:
            raise exceptions.UserCreateError(
                response_status=response.status_code,
                reason=response.reason,
                url=response.url,
                error_text=response.text,
            )
        return response.json()

    def register_user_course_session(self, user_id: int, session_id: int) -> NoReturn:
        """Запись пользователя на сессию курса

        :param user_id: ид записываемого пользователя
        :param session_id: ид сессии, на который записываем пользователя
        """

        # проверяем наличие oauth токена
        self._check_or_update_oauth_token()

        url = self.api_base_url + f"/course_sessions/{session_id}/register"

        data = {"access_token": self._oauth_access_token, "user_id": user_id}

        response = requests.post(url, json=data, timeout=10)

        if response.ok:
            pass
        else:
            raise exceptions.RegisterUserSessionError(
                response_status=response.status_code,
                reason=response.reason,
                url=response.url,
                error_text=response.text,
            )

    def _update_oauth_token(self) -> NoReturn:
        """Получение и сохранение OAuth токена в атрибут класса"""

        url = "https://go.teachbase.ru/oauth/token"

        grant_type = "client_credentials"

        body = {
            "grant_type": grant_type,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
        response = requests.post(url, json=body, timeout=10)

        if response.ok:
            self._oauth_access_token = response.json()["access_token"]
        else:
            raise exceptions.OAuthCreateError(
                response_status=response.status_code,
                reason=response.reason,
                url=response.url,
                error_text=response.text,
            )

    def _check_or_update_oauth_token(self) -> NoReturn:
        """Проверяет, есть ли рабочий токен в атрибутах класса и при необходимости
        отправляет запрос на получение нового токена.
        Вызывается перед отправкой запроса, требующего oauth токен."""

        if not self._oauth_access_token:
            self._update_oauth_token()
