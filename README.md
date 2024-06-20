# Описание

YaTube – проект, в котором пользовали могут создавать текстово-графические публикации, комментировать их и подписываться друг на друга. Проект продвигает концепцию свободного распространиния и общедоступности знаний.

Разработан REST API на Django REST Framework, обеспечивающий взаимодействие с базой данных PostgreSQL. Проект подготовлен к развертыванию в контейнерах на сервере с использованием Docker Compose.

Проект запущен и доступен по адресу: https://nbmstaging.com

Документация к API проекта доступна по адресу: https://nbmstaging.com/redoc/#tag/api

# Автор проекта

[Mikhail](https://github.com/tooMike)

# Установка

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/tooMike/api_final_yatube
```

```
cd yatube_api
```

Запустить сборку проекта:

```
docker compose up
```

Выполнить сбор статики в контейнере backend:

```
docker compose exec backend python manage.py collectstatic
```

Выполнить миграции в контейнере backend:

```
docker compose exec backend python manage.py migrate
```

Проект будет доступен по адресу

```
http://127.0.0.1:8000/
```

# Спецификация

При локальном запуске документация будет доступна по адресу:

```
http://127.0.0.1:8000/redoc/
```

# Основные технические требования

Python==3.9

# Примеры запросов к API

### Получение публикаций

Описание метода: Получить список всех публикаций. При указании параметров limit и offset выдача работает с пагинацией.

Тип запроса: `GET`

Эндпоинт: `api/v1/posts/`

Пример успешного ответа:

```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

### Создание публикации

Описание метода: Добавление новой публикации в коллекцию публикаций. Анонимные запросы запрещены.

Тип запроса: `POST`

Эндпоинт: `api/v1/posts/`

Обязательные параметры: `text`

Необязательные параметры: `image, group`

Пример запроса:

```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```

Пример успешного ответа:

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

