import asyncio

import httpx


async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://facebook.com")
        print(response.text)


asyncio.run(main())
