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

1. Web-framework:  [Django Rest Framework](https://www.django-rest-framework.org/), [Aiohttp](https://docs.aiohttp.org/en/stable/)
2. Database: [PostgreSQL](https://www.postgresql.org/)
4. Parsing: [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
