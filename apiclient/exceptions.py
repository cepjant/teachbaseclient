""" Исключения для API Client """


class APIResponseStatusError(Exception):
    """Ошибочный статус ответа АПИ на запрос"""

    def __init__(
        self,
        response_status: int | str = None,
        reason: str = None,
        url: str = None,
        error_text: str = None,
    ):
        """При вызове исключения можно передать полученный от АПИ статус ответа и
        причину ошибки"""
        self.response_status = str(response_status) if response_status else None
        self.reason = reason
        self.url = url
        self.error_text = error_text

    def __str__(self):
        error_str = "Ошибка обращения к API"
        error_str += (
            ": status - " + self.response_status if self.response_status else ""
        )
        error_str += ". reason - " + self.reason if self.reason else ""
        error_str += ". URL: " + self.url if self.url else ""
        error_str += ". text: " + self.error_text if self.error_text else ""
        return error_str


class OAuthCreateError(APIResponseStatusError):
    """Ошибка при создани oauth токена"""


class UserCreateError(APIResponseStatusError):
    """Ошибка при создании пользователя"""


class CoursesReceiveError(APIResponseStatusError):
    """Ошибка при получении списка курсов"""


class CourseDetailReceiveError(APIResponseStatusError):
    """Ошибка при получении детальной информации о курсе"""


class CourseSessionsReceiveError(APIResponseStatusError):
    """Ошибка при получении списка сессий курса"""


class CourseSessionDetailReceiveError(APIResponseStatusError):
    """Ошибка при получении детальной информации по сессии курса"""


class RegisterUserSessionError(APIResponseStatusError):
    """Ошибка при попытке записать пользователя на сессию"""
