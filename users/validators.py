import datetime

from django.core.exceptions import ValidationError


def check_if_user_older_9(value: datetime.datetime):
    diff = datetime.date.today() - value
    if diff.days > 3285:
        raise ValidationError("Запрещено регистрироваться пользователям младше 9 лет.")


def check_if_not_rambler(value: str):
    if value.split("@")[1] == "rambler.ru":
        raise ValidationError("Запрещена регистрация с почтового адреса в домене rambler.ru.")
