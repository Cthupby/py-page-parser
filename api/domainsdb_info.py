import aiohttp
import asyncio
import time


start_time = time.time()
domain_info = []
urls_list = ['losst.ru']


async def get_domain_info(session, find_url: str) -> str:
    find_url = f'https://api.domainsdb.info/v1/domains/search?domain={find_url}'
    async with session.get(find_url) as resp:
        assert resp.status == 200
        resp_json = await resp.json()
        for resp in resp_json['domains']:
            for c, data in resp.items():
                domain_info.append(data)
        return resp_json


async def load_domain_data(urls_list):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls_list:
            task = asyncio.create_task(get_domain_info(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks)


asyncio.run(load_domain_data(urls_list))

end_time = time.time() - start_time
print(domain_info)
print(f"\nExecution time: {end_time} seconds")
