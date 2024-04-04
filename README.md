# Описание

YaTube – проект, в котором пользовали могут создавать текстово-графические публикации, комментировать их и подписываться друг на друга. Проект продвигает концепцию свободного распространиния и общедоступности знаний  

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

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

# Спецификация

При локальном запуске документация будет доступна по адресу:

```
http://127.0.0.1:8000/redoc/
```

# Основные технические требования

Python==3.9.18

Django==3.2.16

djoser==2.1.0

pytest==6.2.4



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

