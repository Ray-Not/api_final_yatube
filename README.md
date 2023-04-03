## Описание:
Проект представляет собой API для социальной сети yatube.
Полная документация указана на эндпоинте http://server:port/redoc/
### Версия:
1.0

## Как запустить проект:
### Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:Ray-Not/api_final_yatube.git
```
```
cd api_final_yatube
```

### Cоздать и активировать виртуальное окружение:
```
python -m venv env
```
```
source env/Script/activate
```

### Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```

### Выполнить миграции:
```
python manage.py migrate
```

### Запустить проект:
```
python manage.py runserver
```

## Некоторые примеры запросов к API:
<img src="https://i.imgur.com/PouBDLR.jpg">

### Получение информации о публикации:

```
/api/v1/posts/{id}/
```

### Ответ:

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

### Получение информации о публикации:

```
/api/v1/posts/{id}/
```

### Ответ:

```
{
  "user": "string",
  "following": "string"
}
```

### Получение токена для взаимодействия с API:

```
/api/v1/token/jwt/create/
```

### Тело запроса:

```
{
  "username": "String",
  "password": "String"
}
```

### Ответ:

```
{
  "refresh": "refersh_token",
  "access": "access_token"
}
```

### Использование в headers:

```Authorization = Bearer <access_token>```