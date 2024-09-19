# Используем базовый образ
FROM python:3.12-alpine3.20

# Копируем зависимости
COPY requirements.txt /service/requirements.txt

# Копируем все файлы проекта
COPY service /service

# Устанавливаем рабочую директорию
WORKDIR /service

# Открываем порт
EXPOSE 8000

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r /service/requirements.txt

# Добавляем пользователя
RUN adduser --disabled-password service-user

# Переключаемся на пользователя service-user
USER service-user

