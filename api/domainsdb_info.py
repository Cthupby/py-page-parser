import aiohttp
import asyncio
import time
from urllib.parse import urlparse
from .parser import get_links


domain_info = []


async def get_domain_info(session, url: str) -> str:
    find_url = f'https://api.domainsdb.info/v1/domains/search?domain={url}'
    async with session.get(find_url) as resp:
        resp_json = await resp.json()
        try:
            for resp in resp_json['domains']:
                domain_info.append([r for r in resp.values()])
                return resp_json
        except:
            domain_info.append([None] * 10)
            return resp_json


async def load_domain_data(url):
    async with aiohttp.ClientSession() as session:
        tasks = []
        task = asyncio.create_task(get_domain_info(session, url))
        tasks.append(task)
        await asyncio.gather(*tasks)

'''
For test function

start_time = time.time()
url = 'https://losst.ru'

urls = get_links(url)
for i, url in enumerate(urls):
    u = urlparse(url).netloc.replace("www.", "")
    asyncio.run(load_domain_data(u))
    print(u)
    print(domain_info[i])
end_time = time.time() - start_time
print(f"\nExecution time: {end_time} seconds")
'''
