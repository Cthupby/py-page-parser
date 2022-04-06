# Page parser 
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

1. Web-framework: [Django Rest Framework](https://www.django-rest-framework.org/)
2. Database: [PostgreSQL](https://www.postgresql.org/)
3. Server env: [Docker](https://www.docker.com/), [Gunicorn](https://gunicorn.org/), [Nginx](https://nginx.org/)
4. Parsing: [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
5. Telegram: [Aiogram](https://docs.aiogram.dev/en/latest/)

