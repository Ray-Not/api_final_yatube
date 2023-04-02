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
```
/api/v1/posts/{id}/
```
### Response:

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
