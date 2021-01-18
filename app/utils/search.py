import asyncio
import time

import aiohttp

from ..models import User

links = {
    'vk': 'https://vk.com/{}',
    'instagram': 'https://www.instagram.com/{}',
    'pinterest': 'https://www.pinterest.com/{}',
}


async def check_status(session: aiohttp.ClientSession,
                       social_network: str,
                       url: str,
                       username: str,
                       user: User
                       ):
    results = {}

    url = url.format(username)
    try:
        async with session.get(url) as resp:
            if resp.status == 200:
                results[social_network] = url
        return resp.release()
    except Exception:
        pass


async def search(user: User, username: str):
    start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [
            check_status(session, k, v, username, user)
            for k, v in links.items()
        ]
        await asyncio.gather(*tasks)
