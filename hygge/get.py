import aiohttp
import asyncio


class GetResponse:
    '''Async response to get json response
    ```python
    from hygge.get import GetResponse

    url = 'https://www.trustpilot.com/businessunit/search'
    params = {'country': 'dk', 'query': 'mate.bike'}

    res = GetResponse(url).get(params=params)
    info_url = f'https://www.trustpilot.com/businessunit/{res["businessUnits"][0]["id"]}/companyinfobox'
    print(GetResponse(info_url).get())
    ```
    '''

    def __init__(self, url):
        self.url = url

    async def fetch(self, session, **kwargs):
        async with session.get(self.url, **kwargs) as response:
            return await response.json()

    async def get_data(self, **kwargs):
        async with aiohttp.ClientSession() as session:
            return await self.fetch(session, **kwargs)
            

    def get(self, **kwargs):
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(self.get_data(**kwargs))

