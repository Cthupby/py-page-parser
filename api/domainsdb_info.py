import aiohttp
import asyncio
import time

domain_info = []
start_time = time.time()
urls = ['http://www.losst.ru', 'http://www.losst.eu']
# url = urls.replace("http://www.","")


async def get_domain_info(session, url: str) -> str:
    find_url = f'https://api.domainsdb.info/v1/domains/search?domain={url}'
    async with session.get(find_url) as resp:
#        assert resp.status == 200
        resp_json = await resp.json()
        try:
            for resp in resp_json['domains']:
                for data in resp.values():
                    domain_info.append(data)
        except:
            domain_info.append(resp_json)
        return resp_json


async def load_domain_data(url):
    async with aiohttp.ClientSession() as session:
        tasks = []
        task = asyncio.create_task(get_domain_info(session, url))
        tasks.append(task)
        await asyncio.gather(*tasks)


for url in urls:
    asyncio.run(load_domain_data(url.replace("http://www.","")))


end_time = time.time() - start_time
print(domain_info)
print(f"\nExecution time: {end_time} seconds")
