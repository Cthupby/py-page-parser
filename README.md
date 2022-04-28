# Python Page parser 
### Тестовое задние для компании Пикассо

```
В качестве тестового задания вам предлагается написать парсер страницы,
который проанализирует любую web страницу и составит таблицу с найденными
ссылками.
- Парсер должен находить только ссылки в теге <a href='url'></a>
- Для каждой ссылки асинхронно добавляется информация из API
https://api.domainsdb.info/v1/domains/search?domain=НАЙДЕННЫЙ_URL
(https://api.domainsdb.info/v1/)
- Необходимые столбцы в таблице: "найденный url", "domain", "create_date",
"update_date", "country", "isDead", "A", "NS", "CNAME", "MX", "TXT"
- Реализовать поиск (фильтрацию), сортировку и пагинацию таблицы
```

## Технологии проекта:

1. Web-framework: [Django Rest Framework](https://www.django-rest-framework.org/), [Aiohttp](https://docs.aiohttp.org/en/stable/)
2. Database: [PostgreSQL](https://www.postgresql.org/)
3. Parsing: [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Установка и использование

1. Необходимо скачать проект  
2. Создать и активировать виртуальное окружение  
   ```python -m virualenv venv```  
   ```source ./venv/bin/activate```
3. Установить рекомендуемые библиотеки  
  ```pip install -r requirements.txt```
4. Запустить миграции базы данных и запустить проект  
  ```python manage.py migrate```  
  ```python manage.py runserver```  

## Реализация

> Реализация серверной части проекта - https://pypageparser.herokuapp.com/

1. Эндпоинт для выдачи и добавления web страниц  
   ```https://pypageparser.herokuapp.com/api/pages/```  
2. Эндпоинт для выдачи url найденных на конкретной web странице  
   ```https://pypageparser.herokuapp.com/api/pages/<int:pk>/links/```  
3. Эндпоинт для редактирования и удаления конкретной web страницы  
   ```https://pypageparser.herokuapp.com/api/pages/<int:pk>/```  
4. Эндпоинт для редактирования и удаления url  
   ```https://pypageparser.herokuapp.com/api/links/<int:pk>/```  
