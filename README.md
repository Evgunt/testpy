# Веб-сервис для управления движением денежных средств (ДДС)

## Требования

Перед началом убедитесь, что у вас установлены:

| Инструмент | Версия                                                              |
|----------|---------------------------------------------------------------------|
| **Python** | `3.8.10` или выше ([скачать](https://www.python.org/downloads/))       |
| **pip** | Последняя версия (идёт вместе с Python)                             |

---

## 🚀 Установка и запуск проекта

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/Evgunt/testpy.git
cd testpy
```

### 2. Создайте и активируйте виртуальное окружение

```bash
# Создать виртуальное окружение
python -m venv .venv

# Активировать его
# На Windows:
.venv\Scripts\activate

# На macOS/Linux:
source .venv/bin/activate
```

> В начале строки терминала появится `(.venv)` — это означает, что окружение активировано.

### 3. Установите зависимости

```bash
pip install -r requirements.txt
```
> Если есть проблемы с установкой через файл можно использовать команды:

```bash
pip install django
pip install bootstrap4
```

### 4. Примените миграции базы данных

```bash
python manage.py migrate
```

Эта команда создаст необходимые таблицы (по умолчанию используется SQLite).

### 5. (Опционально) Загрузите начальные данные

В проекте есть фикстуры:

```bash
python manage.py loaddata fixtures/initial_data.json
```

### 6. Создайте суперпользователя (для доступа к админке)

```bash
python manage.py createsuperuser
```

Следуйте инструкциям — укажите имя пользователя, email и пароль.

### 7. Запустите сервер разработки

```bash
python manage.py runserver
```

Откройте браузер и перейдите по адресу:  
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📁 Структура проекта (ключевые файлы)

```
testPy/
├── .venv/                  # Виртуальное окружение (игнорируется в Git)
├── testapp/
│   ├── main/               # Основное приложение
│   │   ├── __init__.py     # Обязательный файл для Python-пакета
│   │   ├── admin.py        # Регистрация моделей в админке
│   │   ├── apps.py         # Конфигурация приложения
│   │   ├── forms.py        # Формы для ввода данных
│   │   ├── models.py       # Модели данных
│   │   ├── urls.py         # URL-маршруты приложения
│   │   ├── views.py        # Представления (контроллеры)
│   │   ├── templates/      # HTML-шаблоны с Bootstrap 4
│   │   └── static/         # CSS/JS
│   ├── testapp/            # Основная конфигурация Django
│   │   ├── __init__.py     # Обязательный файл для Python-пакета
│   │   ├── asgi.py         # ASGI-конфигурация (для WebSocket, если нужно)
│   │   ├── settings.py     # Настройки проекта
│   │   ├── urls.py         # Основные URL-маршруты приложения
│   │   └── wsgi.py         # WSGI-конфигурация для серверов
│   ├── manage.py           # Утилита Django
│   ├── requirements.txt    # Зависимости Python
│   └── testapp.data        # База данных
├── .gitignore              # Файл для git. Игнорирует .venv, базу данных, кэш
└── README.md               # Документация проекта
```

> ✅ **Bootstrap 4** подключён через CDN в шаблонах — локальные файлы не требуются, если не вносились изменения.

---

## 🛠️ Полезные команды

| Задача | Команда |
|-------|---------|
| Запустить сервер | `python manage.py runserver` |
| Создать миграцию | `python manage.py makemigrations` |
| Применить миграции | `python manage.py migrate` |
| Создать суперпользователя | `python manage.py createsuperuser` |
| Собрать статику (для продакшена) | `python manage.py collectstatic` |

---

## 📦 Развертывание (кратко)

Для продакшена:

1. Установите `DEBUG = False` в `settings.py`
2. Укажите `ALLOWED_HOSTS = ['ваш-домен.ру']`
3. Используйте **Gunicorn** + **Nginx**
4. Замените SQLite на **PostgreSQL**
5. Выполните: `python manage.py collectstatic`

> Подробнее: [Официальная документация Django по развертыванию](https://docs.djangoproject.com/ru/stable/howto/deployment/)
